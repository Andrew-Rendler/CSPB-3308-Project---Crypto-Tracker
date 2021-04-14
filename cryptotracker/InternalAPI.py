import json
from flask import Flask, Response, request, jsonify
from flask_restful import Resource, reqparse
from .models import db, Bitcoin, Ethereum, Dogecoin


class GetBitcoinEndpoint(Resource):
    def get(self) -> Response:
        btc = Bitcoin.query.all()
        return jsonify(btc)


class GetEthereumEndpoint(Resource):
    def get(self) -> Response:
        btc = Ethereum.query.all()
        return jsonify(btc)


class GetDogecoinEndpoint(Resource):
    def get(self) -> Response:
        btc = Dogecoin.query.all()
        return jsonify(btc)