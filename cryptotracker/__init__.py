import os
from flask import Flask, Response, render_template, request, jsonify
from flask_restful import Api

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

# app context objects
cryptocompare_api = CryptoCompareAPI()
error_handler = ErrorHandler()
cryptodata = CryptoData()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #!!important
    # UNCOMMENT TO RUN ON SERVER
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://dev:password@localhost:5432/dev"
    app.config["SQLALCHEMY_TRACK+MODIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    api.add_resource(HistoricalEndpoint, "/historical")
    api.add_resource(NewsEndpoint, "/news")
    api.add_resource(CurrentEndpoint, "/current")
    api.add_resource(RateLimitEndpoint, "/ratelimit")
    api.add_resource(AddBitcoinEndpoint, "/add-bitcoin")
    api.add_resource(AddEthereumEndpoint, "/add-ethereum")
    api.add_resource(AddDogecoinEndpoint, "/add-dogecoin")

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
        # res = cryptocompare_api.api_call("ratelimit+all", {})
        cn = CryptoNews.getData()
        return render_template("index.html", len=len(cn), news=cn)
        # pass a dict with endpoint args
        # kwargs = {"coin": "BTC", "currency": "USD", "num_entries": "30"}
        # res = cryptocompare_api.api_call("historical+daily", kwargs)
        # return res.json()

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

    @app.route("/calc")
    def calc():
        return render_template("calc.html")

    @app.route("/form")
    def form():
        return render_template("form.html")

    return app
