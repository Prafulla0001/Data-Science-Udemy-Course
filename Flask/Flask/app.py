from flask import Flask
'''
It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World, I am Prafulla Mandal"

@app.route("/index")
def index():
    return "Welcome to the index page"

@app.route("/home")
def home():
    return "Welcome to the home page"

if __name__ == "__main__" : 
    app.run(debug = True) # debug = True makes it possible to edit the code and extract the changes immediately to the webpage instead of restarting the code again and again