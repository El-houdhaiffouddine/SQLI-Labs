from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  phone = db.Column(db.String(12))
  dob = db.Column(db.String(10))
  salary = db.Column(db.Numeric(10,2))

  def __init__(self, name, email, phone, dob, salary):
    self.name = name
    self.email = email
    self.phone = phone
    self.dob = dob
    self.salary = salary

  def __repr__(self):
    return '<Employee %r>' % self.name

@app.route('/',methods=['GET'])
def home():
    
    query = request.args.get('search',[])
    
    if query:

      return redirect( url_for('employees', search=query))
    
    else:

      return render_template('employees.html')

@app.route('/employee', methods=['GET'])
def employees():

  name = request.args.get('search', [])
  if name:
  
     with db.engine.connect() as conn:
       
        query = text("SELECT * FROM Employee WHERE name LIKE '%"+ name +"%'")
        results = conn.execute(query).fetchall()
        return render_template('employees.html', employees=results)
  else:

    return redirect( url_for('home'))


if __name__ == '__main__':
  app.run(host='172.20.10.2', debug=False)