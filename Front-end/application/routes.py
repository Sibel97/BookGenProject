from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Books
import requests


# home route
@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/Generate', methods = ['GET'])
def Generate():
    Genre = requests.get('http://genre-api:5001/get_Genre').text
    Author = requests.get('http://Author-api:5002/get_Author').text
    result = requests.post('http://Book-api:5003/get_book', json = {"Author": Author, "Genre": Genre})
    return render_template('layout.html', Genre = Genre , Author = Author, result = result.text)

