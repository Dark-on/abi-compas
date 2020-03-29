""" This file contains URI routes
connected with functions and content """

from flask import render_template

from sweater import app


@app.route('/index')
@app.route('/')
def index():
    """ function for main page of this application """

    return render_template('index.html')


@app.route('/abi-test')
def abi_test():
    """ function for profession test of this application """

    return render_template('abi-test.html')
