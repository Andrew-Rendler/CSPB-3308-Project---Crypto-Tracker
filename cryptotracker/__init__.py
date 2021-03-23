import os
from flask import Flask, render_template
# TODO: Figure out the module imports
from .CryptoData import CryptoData
# TODO: Figure out the custom module imports
from .CryptoCompareAPI import CryptoCompareAPI
from .ErrorHandler import ErrorHandler

# app context objects
cryptocompare_api = CryptoCompareAPI()
cryptodata = CryptoData()
error_handler = ErrorHandler()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

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

    return app
