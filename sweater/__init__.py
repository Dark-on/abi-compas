"""
'sweater' is a package where whole application is splited by modules
'static' is a folder where are placed all static files like css styles images and js scripts
'templates' is a folder where are placed all templates for html pages
This is an inizializator of this package (app)
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# object of the application created
app = Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = "mysql//root:pass@localhost/abicompass"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from sweater import routes, models
