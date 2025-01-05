from . import app #app object from __init__.py
from flask import render_template, request

# Homepage route
@app.route("/")
def Hello_ColorStack():
    return render_template('home.html')

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission
        username = request.form['username']
        password = request.form['password']
        return f"Username: {username}, Password: {password}"
    else: 
        return render_template('login.html')