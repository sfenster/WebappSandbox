'''
Created on Jan 5, 2020

@author: ScottFenstermaker
'''
from flask import Flask, render_template
import socket
import requests
#print(socket.gethostbyname(socket.getfqdn(socket.gethostname())))
template_dir="./app4-flask-website/templates"

app = Flask(__name__, template_folder=template_dir) #templates not in root app dir

@app.route('/')
def home():
    return render_template("home.html")
  
@app.route('/about')  
def about():
    return "About Page content goes here!"

  
#Threading code below is not from the lesson, but necessary to run on colab
import threading
threading.Thread(target=app.run, kwargs={'host':'0.0.0.0','port':80}).start() 