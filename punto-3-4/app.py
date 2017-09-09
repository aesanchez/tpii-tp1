# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request
from sensors import Sensores
from getinformation import getinformation

app = Flask(__name__, static_url_path='/static')

#### Init Code ####
muestreo = 1
filename ="data"
mis_sensores = Sensores()
mis_sensores.start(filename, muestreo)
#### End Init Code ####

# Define la ruta con la que se ingresara desde el browser
@app.route('/')
def index():
    information = getinformation(filename, 10)
    return render_template('index.html', muestreo = muestreo, information = information)

@app.route('/', methods=['POST'])
def handle_muestreo():
    if request.method == 'POST':
        data = request.form
        global muestreo
        muestreo = data["muestreo"]
        global filename
        information = getinformation(filename, 10)
        global mis_sensores
        mis_sensores.change_sampling(muestreo)
        return render_template('index.html', muestreo = muestreo, information = information)

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=86)