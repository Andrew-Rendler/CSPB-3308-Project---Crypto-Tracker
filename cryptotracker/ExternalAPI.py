import json
import db

from flask import Flask, Response, request
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from .CryptoCompareAPI import CryptoCompareAPI

cc_api = CryptoCompareAPI()


class BitcoinEndpoint(Resource):
    add_args = {
        "date": fields.Int(required=True),
        "price_high": fields.Float(required=True),
        "price_low": fields.Float(required=True),
        "price_open": fields.Float(required=True),
        "price_close": fields.Float(required=True),
    }

    @use_args(historical_args, location="query")
    def put(self, args) -> Response:
        price_open = request.args.get("price_open")
        price_close = request.args.get("price_close")
        price_high = rrequest.args.get("price_high")
        price_low = request.args.get("price_low")
        date = request.args.get("date")
        btc = Bitcoin(
            date=date,
            price_open=price_open,
            price_close=price_close,
            price_high=price_high,
            price_low=price_low,
        )
        db.session.add(btc)
        db.session.commit()
        return Response("success: 200", status=200, mimetype="application/json")


class HistoricalEndpoint(Resource):
    # ex: https://<host>:<port>/historical?interval=daily&coin=BTC&currency=USD&num_entries=10
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
    # ex: https://<host>:<port>/news?type=latest_news&subtype=article
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
    # ex: https://<host>:<port>/current?coin=BTC&currency=USD
    current_args = {
        "coin": fields.Str(required=True),
        "currency": fields.Str(required=True),
    }

    @use_args(current_args, location="query")
    def get(self, args: dict) -> json:
        query_string = "current+single_symbol"
        return cc_api.api_call(query_string, args).json()


class RateLimitEndpoint(Resource):
    # ex: https://<host>:<port>/ratelimit?
    def get(self):
        query_string = "ratelimit+all"
        return cc_api.api_call(query_string, {}).json()


@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)
