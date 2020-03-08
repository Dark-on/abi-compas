""" 'sweater' is a package where whole application is splited by modules
'static' is a folder where are placed all static files like css styles images and js scripts
'templates' is a folder where are placed all templates for html pages
This is an inizializator of this package (app) """

from flask import Flask

# object of the application created
app = Flask("abicompass")

from sweater import routes, models
