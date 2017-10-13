"""
Routes and views for the flask application.
"""

import subprocess
import csv
from datetime import datetime

from flask import render_template, request, send_file

from FlaskTestProject import app
from FlaskTestProject.bussinessLogic import (FileManager, ScriptManager,
                                             TaskManager, LoadBalancer)


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

@app.route('/taskresult/<string:task_id>')
def taskResult(task_id):
    taskManager = TaskManager.TaskManager()
    resultList = taskManager.GetResultList(task_id)
    if taskManager.taskContainsHtmlResult(task_id):
        return render_template('taskresult.html',taskId = task_id, resultList = resultList[:-1], htmlLink='/api/datafile/'+task_id+'/0', framehidden=False)
    else:
        return render_template('taskresult.html', taskId = task_id, resultList = resultList, htmlLink='', framehidden=True)
@app.route('/taskresult_htmlview/<string:task_id>')
def taskresult_htmlview(task_id):
    return


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
    lb = LoadBalancer.LoadBalancer()
    return lb.getPendingTaskCommand(server_name)

@app.route('/api/checkinassignedtask/<string:server_name>', methods=['POST'])
def post_checkinAssignedTask(server_name):
    taskManager = TaskManager.TaskManager()
    taskManager.checkinTask(server_name)
    return 'success'

@app.route('/api/datafile/<string:task_id>/<string:file_id>', methods=['GET'])
def get_datafile(task_id, file_id):
    fileManager = FileManager.FileManager()
    filePath = fileManager.GetResultFileDirectory(task_id, file_id)
    if filePath is None:
        return 'Result File Not Found'
    if fileManager.GetType(filePath) == 'html':
        return send_file(filePath, mimetype='text/html')
    return send_file(filePath, mimetype='text/csv')
