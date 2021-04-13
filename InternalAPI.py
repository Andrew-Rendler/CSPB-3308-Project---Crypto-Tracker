import json
from flask import Flask, Response, request
from flask_restful import Resource, reqparse
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from .CryptoCompareAPI import CryptoCompareAPI
from .models import db, Bitcoin, Ethereum, Dogecoin

cc_api = CryptoCompareAPI()
req_parse = reqparse.RequestParser()


class GetBitcoinEndpoint(Resource):
    def get(self) -> Response:
        btc = Bitcoin.query.all()
        print(btc)
