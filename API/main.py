from flask import Flask, render_template, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), nullable = False)
    first_name = db.Column(db.String(200), nullable = False)
    last_name = db.Column(db.String(200), nullable = False)
    avatar = db.Column(db.String(1000), nullable = False)



# Get List User
@app.route('/all_user/')
def list_user():
    url = "https://reqres.in/api/users?page=2"

    responce = requests.get(url)
    data = responce.json()

    for d in data['data']:

        print(data['data'])

        user_exists = User.query.filter_by(id=d['id']).first()

        if(not user_exists):
            save_user = User(id = d['id'], email = d['email'], first_name = d['first_name'], last_name = d['last_name'], avatar = d['avatar'])
            db.session.add(save_user)
            db.session.commit()
        else:
            print(f"This id {d['id']} is alrady existed")

    return render_template("all_users.html", datas = data['data'])


# Get Singel User
@app.route('/single_user/<int:id>/')
def single_user(id):
    url = f"https://reqres.in/api/users/{id}"

    responce = requests.get(url)
    data = responce.json()

    print(data)
    
    return render_template("single_user.html", datas = data['data'])


# For create a user
@app.route('/new_user/', methods = ['GET', 'POST'])
def new_user():


    if(request.method == 'POST'):

        url = "https://reqres.in/api/users"

        name = request.form.get("name")
        job = request.form.get("job")


        headers = {
            'Content_type' : 'application/json'
        }

        body = {
            "name" : name,
            "job" : job
        }

        responce = requests.post(url, headers = headers, data=body)

        return jsonify(responce.json())

    if(request.method == 'GET'):
        return render_template("create_user.html")

app.run(debug=True)