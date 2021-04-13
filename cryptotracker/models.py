from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()


@dataclass
class Bitcoin(db.Model):
    __tablename__ = "bitcoin_table"

    time: str
    open: float
    close: float
    high: float
    low: float
    volumefrom: float
    volumeto: float

    time = db.Column(db.Integer, primary_key=True, nullable=False)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    open = db.Column(db.Float)
    low = db.Column(db.Float)
    volumefrom: db.Column(db.Float)
    volumeto: db.Column(db.Float)

    def __init__(
        self,
        time,
        price_open,
        price_close,
        price_high,
        price_low,
        volume_from,
        volume_to,
    ):
        self.time = time
        self.open = price_open
        self.close = price_close
        self.high = price_high
        self.low = price_low
        self.volumefrom = volume_from
        self.volumeto = volume_to

    def __repr__(self):
        return "<Bitcoin %r %r %r %r %r>" % (
            self.open,
            self.close,
            self.high,
            self.low,
            self.time,
        )


@dataclass
class Ethereum(db.Model):
    __tablename__ = "ethereum_table"

    time: str
    open: float
    close: float
    high: float
    low: float
    volumefrom: float
    volumeto: float

    time = db.Column(db.Integer, primary_key=True, nullable=False)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    open = db.Column(db.Float)
    low = db.Column(db.Float)
    volumefrom: db.Column(db.Float)
    volumeto: db.Column(db.Float)

    def __init__(
        self,
        time,
        price_open,
        price_close,
        price_high,
        price_low,
        volume_from,
        volume_to,
    ):
        self.time = time
        self.open = price_open
        self.close = price_close
        self.high = price_high
        self.low = price_low
        self.volumefrom = volume_from
        self.volumeto = volume_to

    def __repr__(self):
        return "<Ethereum %r %r %r %r %r>" % (
            self.open,
            self.close,
            self.high,
            self.low,
            self.time,
        )


@dataclass
class Dogecoin(db.Model):
    __tablename__ = "dogecoin_table"

    time: str
    open: float
    close: float
    high: float
    low: float
    volumefrom: float
    volumeto: float

    time = db.Column(db.Integer, primary_key=True, nullable=False)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    open = db.Column(db.Float)
    low = db.Column(db.Float)
    volumefrom: db.Column(db.Float)
    volumeto: db.Column(db.Float)

    def __init__(
        self,
        time,
        price_open,
        price_close,
        price_high,
        price_low,
        volume_from,
        volume_to,
    ):
        self.time = time
        self.open = price_open
        self.close = price_close
        self.high = price_high
        self.low = price_low
        self.volumefrom = volume_from
        self.volumeto = volume_to

    def __repr__(self):
        return "<Dogecoin %r %r %r %r %r>" % (
            self.open,
            self.close,
            self.high,
            self.low,
            self.time,
        )