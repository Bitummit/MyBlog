import datetime
from .comment import Comment
from .database import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, default=datetime.datetime.utcnow())
    comments = db.relationship(Comment)

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id},  title={self.title})"

    def __repr__(self):
        return str(self)
