from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def landing_page():
    name = "Mari_Ladli - Radha"
    return render_template("index.html",name=name)

app.run(debug=True)