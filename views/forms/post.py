from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3)])
    text = TextAreaField('Text', validators=[DataRequired(), Length(min=10)])


