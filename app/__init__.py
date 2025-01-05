from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize the app and the database
app = Flask(__name__, template_folder='../templates', static_folder= '../static')  # Adjusted path to templates
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import routes after initializing app to avoid circular imports
from . import routes, models