"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskTestProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api/test/test1', methods = ['GET'])
def get_test1():
    return "helloWorld" 

@app.route('/demo/demomenu')
def demoMenu():
    """Render the demo Menu page"""
    prelim_names = ['Carla', 'Aly', 'Ivuoma']
    return render_template(
        'demomenu.html',
        title='Demo Menu',
        year=datetime.now().year,
        message='My Demo Menu',
        names = prelim_names
    )

 