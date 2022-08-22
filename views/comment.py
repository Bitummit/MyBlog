from flask import Blueprint, render_template, request, url_for, redirect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from views.forms.comment import CommentForm
from models import Post, db, Comment

comment_app = Blueprint("comment_app", __name__)


@comment_app.route('/add/?post_id=<int:post_id>', methods=["GET", "POST"], endpoint='add')
def add_comment(post_id):
    form = CommentForm()
    if request.method == "GET":
        return render_template("comments/add.html", form=form)

    if not form.validate_on_submit():
        return render_template('comments/add.html', form=form), 400

    comment_text = form.data['text']
    comment = Comment(text=comment_text, post_id=post_id)
    db.session.add(comment)
    try:
        db.session.commit()
    except IntegrityError:
        print('Cant add new post!')
        db.session.rollback()
        raise BadRequest

    url_product = url_for('post_app.detail', post_id=post_id)
    return redirect(url_product)
