from flask import Blueprint, jsonify, render_template, request, url_for, redirect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest

from views.forms.post import PostForm
from models import Post, db, Comment

post_app = Blueprint("post_app", __name__)


@post_app.get('/<int:post_id>/', endpoint="detail")
def get_post(post_id):
    post = Post.query.get_or_404(post_id, description='No such post!')
    comments = Comment.query.filter_by(post_id=post.id)
    return render_template('posts/detail.html', post=post, comments=comments)


@post_app.route('/add/', methods=["GET", "POST"], endpoint='add')
def add_post():
    form = PostForm()
    if request.method == "GET":
        return render_template("posts/add.html", form=form)

    if not form.validate_on_submit():
        return render_template('posts/add.html', form=form), 400

    post_title = form.data['title']
    post_text = form.data['text']
    post = Post(title=post_title, text=post_text)
    db.session.add(post)
    try:
        db.session.commit()
    except IntegrityError:
        print('Cant add new post!')
        db.session.rollback()
        raise BadRequest

    url_product = url_for('post_app.detail', post_id=post.id)
    return redirect(url_product)
