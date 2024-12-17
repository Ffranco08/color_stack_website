# importing Flask class from flask library
from flask import Flask

app = Flask(__name__)

# @app.route("/") is a decorator provided by Flask that tells Flask that functions underneath run when requests for "/" (main page)
@app.route("/")
def hello_world():
    return "Hello, Frankie!"

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