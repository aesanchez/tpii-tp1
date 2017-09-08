# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request
from sensors import run
import threading
from getinformation import getinformation
import os

app = Flask(__name__, static_url_path='/static')
#by default
muestreo = 1
def init():
    muestreo = 1
    filename = "data"
    #delete previous file
    if os.path.isfile(filename):
        os.remove(filename)
    if os.path.isfile(filename+".lock"):
        os.remove(filename+".lock")
    sensores = threading.Thread(target = run, args=(muestreo, filename))
    sensores.daemon = True  
    sensores.start()
init()
# Define la ruta con la que se ingresara desde el browser
@app.route('/')
def index():
    information = getinformation("data", 10)
    return render_template('index.html', muestreo = muestreo, information = information)

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=86)