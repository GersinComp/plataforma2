from pyPackage import app
from flask import render_template


@app.route('/')
def dashboard():
    return render_template('dashboard.html')
