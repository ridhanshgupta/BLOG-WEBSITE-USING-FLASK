from pathlib import Path
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SECRET_KEY"] = "b310c5a1d69dfc89caf329e2382c4438"

BASE_DIR = Path(app.root_path).parent
DB_PATH = BASE_DIR / "instance" / "site.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH.as_posix()}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail()

login_manager = LoginManager(app)
login_manager.login_view = "login"

login_manager.login_view = "login"
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True

app.config["MAIL_USERNAME"] = "guptaridhansh@gmail.com"
app.config["MAIL_PASSWORD"] = "webumvdqqaqmhblj"

mail.init_app(app)

from flaskblog import routes
from flaskblog.models import Post, User

with app.app_context():
    db.create_all()
