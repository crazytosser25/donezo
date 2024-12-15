"""Start app"""

from flask import Flask, render_template

from app.db import db


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SQLALCHEMY_DATABASE_URI="sqlite:///base.sqlite3")

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html"), 200


@app.errorhandler(404)
def handle_404(e):
    return render_template("404.html", content=e), 404
