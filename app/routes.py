# -*- coding: utf-8 -*-
from app import acompass
from flask import render_template, flash, redirect, url_for
# from app.forms import LoginForm


@acompass.route('/')
@acompass.route('/index')
def index():

    return render_template('index.html')


@acompass.route('/spec-test')
def spec_test():

    return render_template('spec-test.html')


@acompass.route('/filter-universities')
def filter_universities():

    return render_template('filter-universities.html')
