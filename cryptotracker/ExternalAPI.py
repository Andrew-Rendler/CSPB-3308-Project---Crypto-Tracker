import json
from flask import Flask
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from .CryptoCompareAPI import CryptoCompareAPI

cc_api = CryptoCompareAPI()


class HistoricalEndpoint(Resource):
    historical_args = {
        "interval": fields.Str(required=True),
        "coin": fields.Str(required=True),
        "currency": fields.Str(required=True),
        "num_entries": fields.Int(required=True),
    }

    @use_args(historical_args, location="query")
    def get(self, args) -> json:
        query_string = "historical+"
        query_string += args["interval"]

        payload = {
            "coin": args["coin"],
            "currency": args["currency"],
            "num_entries": args["num_entries"],
        }
        return cc_api.api_call(query_string, payload).json()


class NewsEndpoint(Resource):
    news_args = {
        "type": fields.Str(required=True),
        "subtype": fields.Str(required=True),
    }

    @use_args(news_args, location="query")
    def get(self, args: dict) -> json:
        # TODO: need a better way to iterate through unrequired query params
        # turn args into OrderedDict so it can be iterated through properly
        query_string = "news"
        query_string += "+"
        query_string += args["type"]
        if args["subtype"] != "none":
            query_string += "+"
            query_string += args["subtype"]
        return cc_api.api_call(query_string, {}).json()


class CurrentEndpoint(Resource):
    current_args = {
        "coin": fields.Str(required=True),
        "currency": fields.Str(required=True),
    }

    @use_args(current_args, location="query")
    def get(self, args: dict) -> json:
        query_string = "current+single_symbol"
        return cc_api.api_call(query_string, args).json()


class RateLimitEndpoint(Resource):
    def get(self):
        query_string = "ratelimit+all"
        return cc_api.api_call(query_string, {}).json()


@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)
