from flask import Flask, render_template

from models.post import Post
from views.comment import comment_app
from views.post import post_app
from models import db
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.update(
    ENV="development",
    SECRET_KEY="sdvmpsdinpfdkdvk",
    SQLALCHEMY_DATABASE_URI="sqlite:///myblog_db.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(post_app, url_prefix="/post")
app.register_blueprint(comment_app, url_prefix="/comment")


@app.get('/', endpoint="list")
def list_products():
    posts = Post.query.all()
    return render_template('posts/list.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
