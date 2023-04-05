from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# App configurations 
    # Database configurations 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://stephendavid:Qwerty@2017@localhost/sports_system2'
db = SQLAlchemy(app)


# Defining models for the apps user and notifications
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


    def __repre__(self):
        return '<User %r>' % self.username




# app routing and views 
@app.route("/")
def index():
    return "Welcome to Flask"

if __name__== "__main__":
    app.run()
