from flask import (Flask, render_template)
app = Flask(__name__)

@app.route("../templates/index.html")
def home():
    return render_template("index.html")

@app.route("../templates/mentalhealth.html")
def data():

    return render_template("mentalhealth.html")

@app.route("../templates/detecting.html")
def map():

    return render_template("detecting.html")
    
if __name__ == "__main__":
    app.run()
