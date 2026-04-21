# from pathlib import Path
# from flask import Flask
# from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_mail import Mail
# from flaskblog.config import Config   

# app = Flask(__name__)
# app.config.from_object(Config)        

# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# mail = Mail(app)

# login_manager = LoginManager(app)
# login_manager.login_view = "users.login"
# login_manager.login_message_category = "info"

# from flaskblog.main.routes import main
# from flaskblog.users.routes import users
# from flaskblog.posts.routes import posts

# app.register_blueprint(main)
# app.register_blueprint(users)
# app.register_blueprint(posts)

# with app.app_context():
#     db.create_all()

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)
#     mail.init_app(app)

#     from flaskblog.users.routes import users
#     from flaskblog.posts.routes import posts
#     from flaskblog.main.routes import main
#     app.register_blueprint(users)
#     app.register_blueprint(posts)
#     app.register_blueprint(main)

#     return app


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from flaskblog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()

login_manager.login_view = "users.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from flaskblog.main.routes import main
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    with app.app_context():
        db.create_all()

    return app