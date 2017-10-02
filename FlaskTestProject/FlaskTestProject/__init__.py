"""
The flask application package.
"""

from flask import Flask

#app.config.from_object(FlaskTestProject.serverConfig)


app = Flask(__name__)
app.config.from_object('FlaskTestProject.serverConfig.Config')

import FlaskTestProject.views
