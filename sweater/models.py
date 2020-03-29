""" Contains all database logic """

from sweater import db


class City(db.Model):
    """ Represents table 'City' """

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(128), unique=True, nullable=False)

class University(db.Model):
    """ Represents table 'University' """

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    # TODO: create field description
    # description = db.Column()
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship('City', backref=db.backref('universities', lazy=True))

class Speciality(db.Model):
    """ Represents table 'University' """

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    # TODO: create field description
    # description = db.Column()
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    university = db.relationship('University', backref=db.backref('specialities', lazy=True))
