from flask import Flask, request
from wtforms.validators import required

from example.forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    form = LoginForm(request.form)
    return render_template("index.html",
                           form=form)


app.run()
