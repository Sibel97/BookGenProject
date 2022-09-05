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
    Genre = requests.get('http://localhost:5001/get_Genre').text
    Author = requests.get('http://localhost:5002/get_Author').text
    result = requests.post('http://localhost:5003/get_book', json = {"Author": Author, "Genre": Genre})
    # book = Books( Title = result.text, Author = Author.text, Genre= Genre.text)
    # db.session.add(book)
    # db.session.commit()
    # last = Books.query.order_by(Books.id.desc()).limit(1).all()
    return render_template('layout.html', Genre = Genre , Author = Author, result = result.text)


# @app.route('/PreviousBooks', methods=['GET'])
# def Previous():
#     books = map(str,Books.query.all())
#     return render_template('books.html', books = books)