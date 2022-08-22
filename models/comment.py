import datetime
from .database import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, default=datetime.datetime.utcnow())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id})"

    def __repr__(self):
        return str(self)
