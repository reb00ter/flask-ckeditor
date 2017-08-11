from wtforms import BooleanField, StringField, Form
from wtforms.validators import DataRequired

from flask_ckeditor.fields import CKEditorField


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    text = CKEditorField('text')