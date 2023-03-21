from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt

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



@app.route('/register', methods=['POST', "GET"])
def register():
    if request.method == "POST":
    # Get data from request
        fullName = request.form.get('fullName')
        password = request.form.get('password')
        email = request.form.get('email')
        phNumber = request.form.get('phNumber')
        
        # Hash password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Insert new user into database
        session = Session()
        try : 
            user = User(fullName = fullName,password=hashed_password, email = email,phNumber = phNumber)
            session.add(user)
            session.commit()
        except:
            session.rollback()
            return jsonify({'error': 'Username already exists!'}), 409
        finally:
            session.close()
        
        # Return success message
        return jsonify({'message': 'User registered successfully!'})
    else : 
        return render_template("index.html")



@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        aadharNum = request.form.get("aadhar")
    return render_template("index.html")

@app.route("/cards")
def cards():
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
