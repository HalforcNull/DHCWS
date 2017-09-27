"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from LoadBalancer import app

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


#api part
@app.route('/api/requestnewtask/<string:serverName>', methods=['GET'])
def reqNewTask(serverName):
    #TODO: find the task id from DB
    #if task id is not null
    #build command line string
    # return as a text
    return 