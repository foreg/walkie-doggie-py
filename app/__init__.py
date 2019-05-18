from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
from flask_uploads import UploadSet, IMAGES, configure_uploads
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import logging


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

images = UploadSet('images', IMAGES)
configure_uploads(app, (images,))
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

scheduler = BackgroundScheduler()
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

from app.models import *
from app import routes
