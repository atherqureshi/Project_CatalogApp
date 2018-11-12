#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


# Render homepage
# Show categories on the left, and latest items in middle
@app.route('/')
@app.route('/home/')
def home():
    categories = session.query(Category).order_by(Category.name)
    latest_items = session.query(Item).order_by(Item.id)
    return render_template('home.html', categories=categories, items=latest_items)


# TO DO | Return serialized JSON of joined dataset (all categories + items within them)
@app.route('/JSON')
def json():
	all_data = session.query(Category,Item).filter(Category.id == Item.category_id)
	return None


@app.route('/categories/JSON')
def category_json():
    categories = session.query(Category)
    return jsonify(categories=[category.serialize for category in categories.all()])


@app.route('/catalog/<category>')
@app.route('/<category>')
def show_category(category):
	# Get the ID for the category entered, to grab the appropriate items per each category
	category_id = (session.query(Category).filter_by(name=category).one()).id
	items = session.query(Item).filter_by(category_id=category_id).all()
	cat_list = session.query(Category).order_by(Category.name)
	return render_template('show_category.html', items=items, category=category, all_categories=cat_list)


@app.route('/catalog/<category>/<item>')
@app.route('/<category>/<item>')
def show_item(category, item):
	item = session.query(Item).filter_by(name=item).one()
	return render_template('show_item.html', item=item)


def login():
	return ""

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)