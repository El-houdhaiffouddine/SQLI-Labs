from app import app, db, Employee

with app.app_context():

     db.drop_all()
     db.create_all()

     employees = [Employee(
       'Alice',
       'alice@cybersecurity.fr',
       '202-555-5555',
       '04-01-1956',
       '75000.00'
      ),
     Employee(
       'Bob',
       'bob@cybersecurity.fr',
       '323-867-5309',
       '12-31-1984',
       '40000.00'
      )]

     for employee in employees:
        db.session.add(employee)
        db.session.commit()