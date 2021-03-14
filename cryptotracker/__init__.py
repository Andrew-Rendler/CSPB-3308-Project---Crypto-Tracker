import os

# TODO: Figure out the module imports
from .CryptoCompareAPI import CryptoCompareAPI
from flask import Flask

cryptocompare_api = CryptoCompareAPI()


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
        res = cryptocompare_api._api_call("ratelimit+all", {})

        # pass a dict with endpoint args
        # kwargs = {"coin": "BTC", "currency": "USD", "num_entries": "30"}
        # res = cryptocompare_api._api_call("historical_daily", kwargs)
        return res.json()

    return app
