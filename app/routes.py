# -*- coding: utf-8 -*-
from app import application
from flask import render_template, flash, redirect, url_for
# from app.forms import LoginForm


@application.route('/')
@application.route('/index')
def index():

    return render_template('index.html')


@application.route('/spec-test')
def spec_test():

    return render_template('spec-test.html')


@application.route('/filter-universities')
def filter_universities():

    return render_template('filter-universities.html')
