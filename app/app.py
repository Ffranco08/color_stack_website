# importing Flask class and render_template function from flask library
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder = 'static')

# Configure the PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "postgresql://frfranco@ucsd.edu:hVk@8j!6CyqN5H.@your-database-host.render.com/color_stack_website"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoid overhead

# Initialize the database
db = SQLAlchemy(app)

# @app.route("/") is a decorator provided by Flask that tells Flask that functions underneath run when requests for "/" (main/home page)
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

'''
when we run app.py, __name__ is set to __main___
port 80 is HTTP default so we set Flask to listen on port 80

* Running on all addresses (0.0.0.0), aka local server

    Flask is running on all available network interfaces. This allows other devices on the same network to access your app using your system's IP address.

* Running on http://127.0.0.1:80 (URL only accessible from this machine)
    
    This is the localhost address for your Flask app.
    You can open this URL in your browser to access your app.

* Running on http://192.168.4.156:80 (URL for all other devices on same network)
    
    This is your system's local network IP address. Devices on the same network (e.g., your phone or another computer) can access your app by visiting this URL.
'''

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80, debug = True)