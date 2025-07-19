# app/db.py

from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = app.config['MYSQL_HOST']
    app.config['MYSQL_USER'] = app.config['MYSQL_USER']
    app.config['MYSQL_PASSWORD'] = app.config['MYSQL_PASSWORD']
    app.config['MYSQL_DB'] = app.config['MYSQL_DB']
    
    mysql.init_app(app)
