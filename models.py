from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from app import app

db = SQLAlchemy()
# migrate = Migrate(app, db)


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    fcuser_id = db.Column(db.Integer, db.ForeignKey('fcuser.id'), nullable=False)
    title = db.Column(db.String(256))
    tstamp = db.Column(db.DateTime, server_default=db.func.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'tstamp': self.tstamp
        }


class Fcuser(db.Model):
    __tablename__ = 'fcuser'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32))
    password = db.Column(db.String(20))
    todos = db.relationship('Todo', backref='fcuser', lazy=True)