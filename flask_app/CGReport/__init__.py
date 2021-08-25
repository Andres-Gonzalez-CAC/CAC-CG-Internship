from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = "c1de43de66c4735395e8266506fb58c8676634e7f2cd9f9916029659b32bc680"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Building_Information.sqlite3"
db = SQLAlchemy(app)
import CGReport.routes
