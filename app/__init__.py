from flask import Flask
from config import Config
from .marvel.routes import marvel
from .models import login,db
from flask_migrate import Migrate, migrate

app=Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(marvel)

db.init_app(app)
migrate = Migrate(app,db)

login.init_app(app)
login.login_view='marvel.signin'
login.login_message='Please sign in to view this page'
login.login_message_category='danger'


from . import routes

from . import models
