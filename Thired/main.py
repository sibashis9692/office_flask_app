from flask import Flask, request, redirect, Response, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///radha.db"

db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)

    def __repr__(self) -> str:
        return f"{self.sno} {self.username}"
    

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")


        print(username)
        print(email)
        print(password)

        data = User(username = username, email = email, password = password)
        db.session.add(data)
        db.session.commit()

        # return Response(f"Yes Your data is Now saved:- This is the your given username {username}, and this is your given email {email}, and this is your given password {password}")
        return redirect('/')
    else:
        data = User.query.all()

        print(data)
        
        return render_template("index.html", datas = data)



app.run(debug=True)