# app/__init__.py

from flask import Flask
from flask_mysqldb import MySQL
import config

app = Flask(__name__, static_folder='static')
app.secret_key = config.SECRET_KEY

# MySQL configuration
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
import os

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize MySQL
mysql = MySQL(app)

# Import routes (so they can register with the global app instance)
from app import routes  # make sure this is at the end
