from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask import render_template, request, flash, redirect, url_for
from yt import download_video
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("CONFIG_KEY")

Bootstrap(app)


class YtForm(FlaskForm):
    link = StringField("Link")
    submit = SubmitField("Submit")


@app.route('/', methods=["GET", "POST"])
def main():
    form = YtForm()
    if form.validate_on_submit():
        download_video(form.link.data)
        return form.link.data
    return render_template('index.html', form=form)
