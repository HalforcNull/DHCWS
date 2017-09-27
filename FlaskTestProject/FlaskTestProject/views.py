"""
Routes and views for the flask application.
"""

import subprocess
from datetime import datetime

from flask import render_template, request

from FlaskTestProject import app
from FlaskTestProject.bussinessLogic import (FileManager, ScriptManager,
                                             TaskManager)


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

#Pages
#TOBE DELETE
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

@app.route('/scriptlist')
def scriptlist():
    sm = ScriptManager.ScriptManager()
    return render_template(
        'scriptlist.html',
        title='Script List',
        message = 'This is all script now in the server, pick up one and start a new task.',
        scriptList = sm.getScriptList()
    )

@app.route('/tasksetup/<string:script_id>')
def tasksetup(script_id):
    tm = TaskManager.TaskManager()
    scriptRequiredDataFiles = ['reqFile1', 'reqFile2', 'reqFile3']
    scriptRequiredDataInputs = ['reqValue1', 'reqValue2', 'reqValue3']
    return render_template(
        'tasksetup.html',
        title='Setup Task',
        taskId=tm.getNewTask(script_id, '1'),
        year=datetime.now().year,
        reqFiles = scriptRequiredDataFiles,
        reqInputs = scriptRequiredDataInputs,
        urlFileUpload = '/api/useruploadfile',
        urlTaskSubmit = '/tasksubmit'
    )

@app.route('/tasksubmit', methods=['POST'])
def post_taskSubmit():
    parms = (request.form['field_1'], request.form['field_2'], request.form['field_3'])
    tm = TaskManager.TaskManager()
    tm.updateTaskParms(request.form['task_id'], parms)
    resultCode = tm.activeTask(request.form['task_id'])
    
    if resultCode == 1:
        return render_template('taskactivesuccess.html')
    
    return render_template('taskactivefail.html')

@app.route('/testScript')
def testRun():
    subprocess.call(['C:/Program Files/R/R-3.4.1/bin/RScript', 'C:/DemoScriptFolder/Sleep30s.R'], shell=False)
    return render_template('testshowvalue.html', values=('success'))

#API SECTION
@app.route('/api/scriptdescription/<string:script_name>', methods = ['GET'])
def get_scriptdescription(script_name):
    return "put description here" 

@app.route('/api/scriptsourcecode/<string:script_name>', methods = ['GET'])
def get_scriptsourcecode(script_name):
    return "put source code here"

@app.route('/api/useruploadfile', methods=['POST'])
def post_userUploadFile():
    fileManager = FileManager.FileManager()
    return fileManager.UploadFileForGivenTask(request.files['file'], request.form['task_id'], request.form['file_id'])

@app.route('/api/requestnewtask/<string:server_name>', methods=['GET'])
def get_requestNewTask(server_name):
    taskManager = TaskManager.TaskManager()
    return taskManager.getFirstPendingTask(server_name)

@app.route('/api/checkinassignedtask/<string:server_name>', methods=['POST'])
def post_checkinAssignedTask(server_name):
    taskManager = TaskManager.TaskManager()
    return taskManager.checkinTask(server_name)

