from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/techstack')
def techstack():
    return render_template('techstack.html')

@app.route('/workflow')
def workflow():
    return render_template('workflow.html')

@app.route('/references')
def references():
    return render_template('references.html')