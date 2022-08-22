from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired(), Length(min=10)])


