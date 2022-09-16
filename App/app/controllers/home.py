from app import app
from flask import render_template, redirect, url_for, session

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')