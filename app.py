from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/user1/employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  phone = db.Column(db.String(12))
  birth = db.Column(db.String(10))
  salary = db.Column(db.Numeric(10,2))

  def __init__(self, name, email, phone, birth, salary):
    self.name = name
    self.email = email
    self.phone = phone
    self.birth = birth
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
  #Imput validation with allowed list of characters
  allowed_list = r"^[a-zA-Z0-9\s]{1,10}$"
  #Escaping malicious characters
  escaped_characters = r"['\"-;()%=`#,]"

  if name:
  
     if bool(re.match(allowed_list,name)) and len(name) in range(1,10):
       
       with db.engine.connect() as conn:
        
          #Removing malicious characters
          name = re.sub(escaped_characters,"",name)

          f_name = f"%{name}%"
          param = [{"f_name":f_name}]
               
          query = text("SELECT * FROM Employee WHERE name LIKE :f_name")
          #parameterized query
          results = conn.execute(query, param).fetchall()

          return render_template('employees.html', employees=results)
     else:

       return render_template("redirect.html")
       
  else:

    return redirect( url_for('home'))


if __name__ == '__main__':
  app.run(host='172.20.10.2', debug=False)