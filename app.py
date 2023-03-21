from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///users.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phNumber = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create database tables if they don't exist
Base.metadata.create_all(engine)





@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/cards", methods = ["POST", "GET"])
def cards():
    if request.method == "POST":
        aadharNum = request.form.get("aadhar")

        url = "https://alanaktion-faker-v1.p.rapidapi.com/person/%7Bgender%7D"

        querystring = {"locale":"en_US"}

        headers = {
            "X-RapidAPI-Key": "b4f68bc2c2mshe608a930ef4fc28p185c1djsn645ce3f43579",
            "X-RapidAPI-Host": "alanaktion-faker-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

        return render_template("cards.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


@app.route("/report-accident", methods = ["POST", "GET"])
def accident():
    return render_template("accident.html")

@app.route("/contacts")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/raise-issue")
def raise_issue():
    return render_template("issue.html")

@app.route("/report-voilation")
def report_voilation():
    return render_template("/report-voilation.html")



if __name__ == '__main__':
    app.run(debug=True)
