# create_db.py
from main import app, db  # Replace `your_flask_app_file` with the name of your Flask app file

with app.app_context():
    db.create_all()
    print("Database and tables created.")
