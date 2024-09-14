from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CarDue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_no = db.Column(db.String(50), nullable=False)
    model_name = db.Column(db.String(100), nullable=False)
    part_required = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    dealership = db.Column(db.String(100), nullable=False)


class Part(db.Model):
    part_no = db.Column(db.String(100), primary_key=True)
    part_name = db.Column(db.String(100), nullable=False)
