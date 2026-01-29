#import the flask class from f;ask module
from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

#Define a route for the root ("/")
@app.route("/")
def home():
    #Function that handles requests to the the root URL
    return {"message":"Hello World!"}
