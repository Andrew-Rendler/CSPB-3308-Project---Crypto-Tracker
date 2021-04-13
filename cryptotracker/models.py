from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()


class CryptoModel(db.Model):
    __tablename__ = "crypto_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}:{self.price}"


@dataclass
class Bitcoin(db.Model):
    __tablename__ = "bitcoin_table"

    date: str
    price_open: float
    price_close: float
    price_high: float
    price_low: float

    date = db.Column(db.String(), primary_key=True, nullable=False)
    price_open = db.Column(db.Float)
    price_close = db.Column(db.Float)
    price_high = db.Column(db.Float)
    price_low = db.Column(db.Float)

    def __init__(self, date, price_open, price_close, price_high, price_low):
        self.date = date
        self.price_open = price_open
        self.price_close = price_close
        self.price_high = price_high
        self.price_low = price_low

    def __repr__(self):
        return "<Bitcoin %r %r %r %r %r>" % (
            self.price_open,
            self.price_close,
            self.price_high,
            self.price_low,
            self.date,
        )


class Ethereum(db.Model):
    __tablename__ = "ethereum_table"

    date = db.Column(db.String(), primary_key=True, nullable=False)
    price_open = db.Column(db.Float)
    price_close = db.Column(db.Float)
    price_high = db.Column(db.Float)
    price_low = db.Column(db.Float)

    def __init__(self, date, price_open, price_close, price_high, price_low):
        self.date = date
        self.price_open = price_open
        self.price_close = price_close
        self.price_high = price_high
        self.price_low = price_low

    def __repr__(self):
        return "<Ethereum %r>" % self.price_open


class Dogecoin(db.Model):
    __tablename__ = "dogecoin_table"

    date = db.Column(db.String(), primary_key=True, nullable=False)
    price_open = db.Column(db.Float)
    price_close = db.Column(db.Float)
    price_high = db.Column(db.Float)
    price_low = db.Column(db.Float)

    def __init__(self, date, price_open, price_close, price_high, price_low):
        self.date = date
        self.price_open = price_open
        self.price_close = price_close
        self.price_high = price_high
        self.price_low = price_low

    def __repr__(self):
        return "<Dogecoin %r>" % self.price_open
