import os
from flask import Flask, Response, render_template, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db, CryptoModel, Bitcoin, Ethereum, Dogecoin

# TODO: Figure out the custom module imports
from .CryptoCompareAPI import CryptoCompareAPI
from .ErrorHandler import ErrorHandler
from .CryptoData import CryptoData
from .ExternalAPI import *

# app context objects
cryptocompare_api = CryptoCompareAPI()
error_handler = ErrorHandler()
cryptodata = CryptoData()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_mapping(
    #    SECRET_KEY="dev",
    #    DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    #)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dev:password@localhost:5432/dev"
    app.config["SQLALCHEMY_TRACK+MODIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    api.add_resource(HistoricalEndpoint, "/historical")
    api.add_resource(NewsEndpoint, "/news")
    api.add_resource(CurrentEndpoint, "/current")
    api.add_resource(RateLimitEndpoint, "/ratelimit")

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
        res = cryptocompare_api.api_call("ratelimit+all", {})

        # pass a dict with endpoint args
        # kwargs = {"coin": "BTC", "currency": "USD", "num_entries": "30"}
        # res = cryptocompare_api.api_call("historical+daily", kwargs)
        return res.json()

    # testing -- rendering html and displaying BTC data from API call
    @app.route("/test")
    def test():
        kwargs = {"coin": "BTC", "currency": "USD", "num_entries": "30"}
        cryptodata.apiCall("historical+daily", kwargs)
        dic = {}
        dic = cryptodata.getDic()
        return render_template("data.html", info=dic)
    
    @app.route('/form')
    def form():
        return render_template('form.html')


    @app.route('/add-btc', methods = ["POST"])
    def add_btc():
        price_open = float(request.args.get("price_open"))
        price_close = float(request.args.get("price_close"))
        price_high = float(request.args.get("price_high"))
        price_low = float(request.args.get("price_low"))
        date = int(request.args.get("date"))
        btc = Bitcoin(date=date, price_open=price_open, price_close=price_close, price_high=price_high, price_low=price_low)
        db.session.add(btc)
        db.session.commit()
        return Response("success: 200", status=200, mimetype="application/json")


    @app.route('/add-eth', methods = ["POST"])
    def add_eth():
        price_open = float(request.args.get("price_open"))
        price_close = float(request.args.get("price_close"))
        price_high = float(request.args.get("price_high"))
        price_low = float(request.args.get("price_low"))
        date = int(request.args.get("date"))
        eth = Ethereum(date=date, price_open=price_open, price_close=price_close, price_high=price_high, price_low=price_low)
        db.session.add(eth)
        db.session.commit()
        return Response("success: 200", status=200, mimetype="application/json")


    @app.route('/add-doge', methods = ["POST"])
    def add_doge():
        price_open = float(request.args.get("price_open"))
        price_close = float(request.args.get("price_close"))
        price_high = float(request.args.get("price_high"))
        price_low = float(request.args.get("price_low"))
        date = int(request.args.get("date"))
        dc = Dogecoin(date=date, price_open=price_open, price_close=price_close, price_high=price_high, price_low=price_low)
        db.session.add(dc)
        db.session.commit()
        return Response("success: 200", status=200, mimetype="application/json")


    @app.route('/add-crypto', methods = ['POST', 'GET'])
    def add_crypto_to_db():
        if request.method == "POST":
            price_high = request.form["price_high"]
            price_open = request.form["price_open"]
            price_low = request.form["price_low"]
            price_close = request.form["price_close"]
            return "in here"
        return "now in here"

    return app
