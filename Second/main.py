from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100))
    password = db.Column(db.String(200), nullable = False)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return render_template("forms.html")
    
    elif(request.method == 'POST'):

        print("Yes Yes I am here")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")


        print(username)
        print(email)
        print(password)


        data = User(username = username, email = email, password = password)
        db.session.add(data)
        db.session.commit()

        return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)