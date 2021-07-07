from flask import Flask, render_template
from dataimport import *

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/import")
def route2():
    importData();
    return "Data imported"

@app.route('/display')
def hey():
    dat = displayData();
    return render_template('base.html', dat=dat)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
