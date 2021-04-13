import json
from flask import Flask, Response, request
from flask_restful import Resource, reqparse
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from .CryptoCompareAPI import CryptoCompareAPI
from .models import db, Bitcoin, Ethereum, Dogecoin

cc_api = CryptoCompareAPI()
req_parse = reqparse.RequestParser()


class AddBitcoinEndpoint(Resource):
    def post(self) -> Response:
        args = req_parse.parse_args()
        print(request.args)
        _open = float(request.args.get("open"))
        close = float(request.args.get("close"))
        high = float(request.args.get("high"))
        low = float(request.args.get("low"))
        time = int(request.args.get("time"))
        volumefrom = float(request.args.get("volumefrom"))
        volumeto = float(request.args.get("volumeto"))
        print(_open)
        btc = Bitcoin(
            time=time,
            _open=_open,
            close=close,
            high=high,
            low=low,
            volumefrom=volumefrom,
            volumeto=volumeto,
        )
        db.session.add(btc)
        print(btc)
        # handle errors here try/except
        db.session.commit()
        return Response("success: 200", status=200, mimetype="application/json")


class AddEthereumEndpoint(Resource):
    def post(self) -> Response:
        args = req_parse.parse_args()
        _open = float(request.args.get("open"))
        close = float(request.args.get("close"))
        high = float(request.args.get("high"))
        low = float(request.args.get("low"))
        time = int(request.args.get("time"))
        volumefrom = float(request.args.get("volumefrom"))
        volumeto = float(request.args.get("volumeto"))
        eth = Ethereum(
            time=time,
            open=_open,
            close=close,
            high=high,
            low=low,
            volumefrom=volumefrom,
            volumeto=volumeto,
        )
        db.session.add(eth)
        db.session.commit()
        return Response("success: 200", status=200, mimetype="application/json")


class AddDogecoinEndpoint(Resource):
    def post(self) -> Response:
        args = req_parse.parse_args()
        _open = float(request.args.get("open"))
        close = float(request.args.get("close"))
        high = float(request.args.get("high"))
        low = float(request.args.get("low"))
        time = int(request.args.get("time"))
        volumefrom = float(request.args.get("volumefrom"))
        volumeto = float(request.args.get("volumeto"))
        doge = Dogecoin(
            time=time,
            open=_open,
            close=close,
            high=high,
            low=low,
            volumefrom=volumefrom,
            volumeto=volumeto,
        )
        db.session.add(doge)
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
