from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    #vuelvo a comprobar
    if request.method =='POST':
        data = request.form
        var1 = data["var1"]
        var2 = data["var2"]
        result = int(var1) + int(var2)
        return render_template('result.html', result = result)

if __name__ == "__main__":
    app.run(host='localhost', port=80)