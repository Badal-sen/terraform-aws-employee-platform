from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Deployment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application = db.Column(db.String(100))
    version = db.Column(db.String(50))
    environment = db.Column(db.String(50))
    status = db.Column(db.String(50))
    deployed_by = db.Column(db.String(100))