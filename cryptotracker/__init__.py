import os
from flask import Flask, Response, render_template, request, jsonify, redirect, url_for, flash, send_from_directory
from flask_restful import Api

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
#!!important
##UNCOMMENT TO RUN ON SERVER
from .models import db, Bitcoin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# TODO: Figure out the custom module imports
from .CryptoCompareAPI import CryptoCompareAPI
from .ErrorHandler import ErrorHandler
from .CryptoData import CryptoData
from .CryptoNews import CryptoNews

#!!important
##UNCOMMENT TO RUN ON SERVER
from .ExternalAPI import *
from .InternalAPI import *

# app context objects
cryptocompare_api = CryptoCompareAPI()
error_handler = ErrorHandler()
cryptodata = CryptoData()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #!!important
    # UNCOMMENT TO RUN ON SERVER
    app.config['SECRET_KEY'] = '14941313be0b30eff24fe4fb35b3b52a180aa46cacb5174b'
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://dev:password@localhost:5432/dev"
    app.config["SQLALCHEMY_TRACK+MODIFICATIONS"] = False
    db.init_app(app)

    ####db = SQLAlchemy(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    migrate = Migrate(app, db)
    api = Api(app)
    api.add_resource(HistoricalEndpoint, "/historical")
    api.add_resource(NewsEndpoint, "/news")
    api.add_resource(CurrentEndpoint, "/current")
    api.add_resource(RateLimitEndpoint, "/ratelimit")
    api.add_resource(AddBitcoinEndpoint, "/add-bitcoin")
    api.add_resource(AddEthereumEndpoint, "/add-ethereum")
    api.add_resource(AddDogecoinEndpoint, "/add-dogecoin")
    api.add_resource(GetBitcoinEndpoint, "/get-bitcoin")
    api.add_resource(GetEthereumEndpoint, "/get-ethereum")
    api.add_resource(GetDogecoinEndpoint, "/get-dogecoin")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    bits = db.Column(db.Float)
    ethers = db.Column(db.Float)
    doges = db.Column(db.Float)

    def __repr__(self):
        return "<User %r %r %r %r %r>" % (
            self.id,
            self.username,
            self.bits,
            self.ethers,
            self.doges,
        )

    ####db.create_all()

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/")
    def index():
        # examples of api calls. A string must be passed with following format
        #   - single argument: expr_1
        #   - multi argument: expr_1+expr_2
        # pass an empty dict if there are no endpoint args
        # res = cryptocompare_api.api_call("ratelimit+all", {})
        # pass a dict with endpoint args
        # kwargs = {"coin": "BTC", "currency": "USD", "num_entries": "30"}
        # res = cryptocompare_api.api_call("historical+daily", kwargs)
        # return res.json()
        cn = CryptoNews.getData()
        if (current_user.is_authenticated):
            return render_template("index.html", len=len(cn), news=cn, logged_in=current_user.is_authenticated, user=current_user)
        return render_template("index.html", len=len(cn), news=cn, logged_in=current_user.is_authenticated)

    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username=username).first()
            if not user:
                flash("An account has not yet been created with that username.")
                return redirect(url_for('login'))
            elif not check_password_hash(user.password, password):
                flash("Incorrect password.")
                return redirect(url_for('login'))
            else:
                login_user(user)
                return redirect(url_for('index'))
        return render_template("login.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            if User.query.filter_by(username=request.form.get('username')).first():
                #User already exists
                flash("An account with this username already exists.")
                return redirect(url_for('signup'))

            hashpass = generate_password_hash(
                request.form.get('password'),
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = User(
                name = request.form.get("name"),
                username = request.form.get("username"),
                password = hashpass,
                bits = 0,
                ethers = 0,
                doges = 0,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))
        return render_template("signup.html", logged_in=current_user.is_authenticated)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route("/portfolio", methods=["GET", "POST"])
    @login_required
    def portfolio():
        if request.method == "POST":
            current_user.bits = request.form["bits"]
            current_user.ethers = request.form["ethers"]
            current_user.doges = request.form["doges"]
            db.session.commit()

        #### NEED TO MULTIPLY BY ACTUAL VALUE OF COINS
        portfolio = current_user.bits * 60000
        portfolio += current_user.doges * .30
        portfolio += current_user.ethers * 2000
        portfolio = "{:,.2f}".format(portfolio)
        return render_template("portfolio.html", user=current_user, value=portfolio)


    # testing -- rendering html and displaying BTC data from API call
    @app.route("/test")
    def test():
        dic = {}
        dic = cryptodata.getDic()
        return render_template("test.html", info=dic)

    @app.route("/getbitcoin")
    def getbitcoin():
        btc = Bitcoin.query.all()
        print(jsonify(btc), btc)
        return jsonify(btc)

    @app.route("/test2")
    def test2():
        return render_template("test.html", info=CryptoNews.getData())

    @app.route("/form")
    def form():
        return render_template("form.html")

    return app
