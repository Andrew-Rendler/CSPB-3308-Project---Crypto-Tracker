from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()


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


@dataclass
class Ethereum(db.Model):
    __tablename__ = "ethereum_table"

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
        return "<Ethereum %r %r %r %r %r>" % (
            self.price_open,
            self.price_close,
            self.price_high,
            self.price_low,
            self.date,
        )


@dataclass
class Dogecoin(db.Model):
    __tablename__ = "dogecoin_table"

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
        return "<Dogecoin %r %r %r %r %r>" % (
            self.price_open,
            self.price_close,
            self.price_high,
            self.price_low,
            self.date,
        )


#         from flask_sqlalchemy import SQLAlchemy
# from dataclasses import dataclass

# db = SQLAlchemy()


# @dataclass
# class Bitcoin(db.Model):
#     __tablename__ = "bitcoin_table"

#     time: str
#     open: float
#     close: float
#     high: float
#     low: float
#     volumefrom: float
#     volumeto: float

#     time = db.Column(db.Int, primary_key=True, nullable=False)
#     close = db.Column(db.Float)
#     high = db.Column(db.Float)
#     open = db.Column(db.Float)
#     low = db.Column(db.Float)
#     volumefrom: db.Column(db.Float)
#     volumeto: db.Column(db.Float)

#     def __init__(
#         self,
#         time,
#         price_open,
#         price_close,
#         price_high,
#         price_low,
#         volume_from,
#         volume_to,
#     ):
#         self.time = time
#         self.open = price_open
#         self.close = price_close
#         self.high = price_high
#         self.low = price_low
#         self.volumefrom = volume_from
#         self.volumeto = volume_to

#     def __repr__(self):
#         return "<Bitcoin %r %r %r %r %r>" % (
#             self.open,
#             self.close,
#             self.high,
#             self.low,
#             self.time,
#         )


# @dataclass
# class Ethereum(db.Model):
#     __tablename__ = "ethereum_table"

#     time: str
#     open: float
#     close: float
#     high: float
#     low: float
#     volumefrom: float
#     volumeto: float

#     time = db.Column(db.Int, primary_key=True, nullable=False)
#     close = db.Column(db.Float)
#     high = db.Column(db.Float)
#     open = db.Column(db.Float)
#     low = db.Column(db.Float)
#     volumefrom: db.Column(db.Float)
#     volumeto: db.Column(db.Float)

#     def __init__(
#         self,
#         time,
#         price_open,
#         price_close,
#         price_high,
#         price_low,
#         volume_from,
#         volume_to,
#     ):
#         self.time = time
#         self.open = price_open
#         self.close = price_close
#         self.high = price_high
#         self.low = price_low
#         self.volumefrom = volume_from
#         self.volumeto = volume_to

#     def __repr__(self):
#         return "<Ethereum %r %r %r %r %r>" % (
#             self.open,
#             self.close,
#             self.high,
#             self.low,
#             self.time,
#         )


# @dataclass
# class Dogecoin(db.Model):
#     __tablename__ = "dogecoin_table"

#     time: str
#     open: float
#     close: float
#     high: float
#     low: float
#     volumefrom: float
#     volumeto: float

#     time = db.Column(db.Int, primary_key=True, nullable=False)
#     close = db.Column(db.Float)
#     high = db.Column(db.Float)
#     open = db.Column(db.Float)
#     low = db.Column(db.Float)
#     volumefrom: db.Column(db.Float)
#     volumeto: db.Column(db.Float)

#     def __init__(
#         self,
#         time,
#         price_open,
#         price_close,
#         price_high,
#         price_low,
#         volume_from,
#         volume_to,
#     ):
#         self.time = time
#         self.open = price_open
#         self.close = price_close
#         self.high = price_high
#         self.low = price_low
#         self.volumefrom = volume_from
#         self.volumeto = volume_to

#     def __repr__(self):
#         return "<Dogecoin %r %r %r %r %r>" % (
#             self.open,
#             self.close,
#             self.high,
#             self.low,
#             self.time,
#         )