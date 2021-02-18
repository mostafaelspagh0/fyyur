from app import db


class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    cities = db.relationship('City', backref='state', lazy=True)
