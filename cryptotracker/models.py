from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from flask_login import (
    UserMixin,
)

db = SQLAlchemy()


@dataclass
class Bitcoin(db.Model):
    __tablename__ = "bitcoin_table"

    time: str
    priceopen: float
    close: float
    high: float
    low: float
    volumefrom: float
    volumeto: float

    time = db.Column(db.Integer, primary_key=True, nullable=False)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    priceopen = db.Column(db.Float)
    low = db.Column(db.Float)
    volumefrom = db.Column(db.Float)
    volumeto = db.Column(db.Float)

    def __init__(
        self,
        time,
        priceopen,
        close,
        high,
        low,
        volumefrom,
        volumeto,
    ):
        self.time = time
        self.priceopen = priceopen
        self.close = close
        self.high = high
        self.low = low
        self.volumefrom = volumefrom
        self.volumeto = volumeto

    def __repr__(self):
        return "<Bitcoin %r %r %r %r %r>" % (
            self.priceopen,
            self.close,
            self.high,
            self.low,
            self.time,
        )


@dataclass
class Ethereum(db.Model):
    __tablename__ = "ethereum_table"

    time: str
    priceopen: float
    close: float
    high: float
    low: float
    volumefrom: float
    volumeto: float

    time = db.Column(db.Integer, primary_key=True, nullable=False)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    priceopen = db.Column(db.Float)
    low = db.Column(db.Float)
    volumefrom = db.Column(db.Float)
    volumeto = db.Column(db.Float)

    def __init__(
        self,
        time,
        priceopen,
        close,
        high,
        low,
        volumefrom,
        volumeto,
    ):
        self.time = time
        self.priceopen = priceopen
        self.close = close
        self.high = high
        self.low = low
        self.volumefrom = volumefrom
        self.volumeto = volumeto

    def __repr__(self):
        return "<Ethereum %r %r %r %r %r>" % (
            self.priceopen,
            self.close,
            self.high,
            self.low,
            self.time,
        )


@dataclass
class Dogecoin(db.Model):
    __tablename__ = "dogecoin_table"

    time: str
    priceopen: float
    close: float
    high: float
    low: float
    volumefrom: float
    volumeto: float

    time = db.Column(db.Integer, primary_key=True, nullable=False)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    priceopen = db.Column(db.Float)
    low = db.Column(db.Float)
    volumefrom = db.Column(db.Float)
    volumeto = db.Column(db.Float)

    def __init__(
        self,
        time,
        priceopen,
        close,
        high,
        low,
        volumefrom,
        volumeto,
    ):
        self.time = time
        self.priceopen = priceopen
        self.close = close
        self.high = high
        self.low = low
        self.volumefrom = volumefrom
        self.volumeto = volumeto

    def __repr__(self):
        return "<Dogecoin %r %r %r %r %r>" % (
            self.priceopen,
            self.close,
            self.high,
            self.low,
            self.time,
        )


@dataclass
class User(UserMixin, db.Model):
    id: int
    name: str
    username: str
    password: str
    bits: float
    ethers: float
    doges: float

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    bits = db.Column(db.Float)
    ethers = db.Column(db.Float)
    doges = db.Column(db.Float)

    def __repr__(self):
        return "<User %r %r %r %r %r>" % (
            self.id,
            self.username,
            self.bits,
            self.ethers,
            self.doges,
        )
