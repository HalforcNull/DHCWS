"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskTestProject import app

#PREMADE CODES
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

#demo Section

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


#API SECTION
@app.route('/api/scriptdescription/<string:script_name>', methods = ['GET'])
def get_scriptdescription(script_name):
    return "hello put description here" 

@app.route('/api/scriptsourcecode/<string:script_name>', methods = ['GET'])
def get_scriptsourcecode(script_name):
    return "hello put source code here"