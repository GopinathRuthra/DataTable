#app.py
from flask import Flask, render_template, json, request, redirect
# from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from datetime import datetime
import sqlite3
  
app = Flask(__name__)
  
app.secret_key = "caircocoders-ednalan-2020"
  
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'testingdb'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# mysql = MySQL(app)
  
@app.route('/')
def main():
    return redirect('/useradmin')
    
@app.route('/useradmin')
def useradmin():
    # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    con = sqlite3.connect("testingdb.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()  
    result = cur.execute("SELECT * FROM employee")
    employee = cur.fetchall()
    print(employee)
    return render_template('useradmin.html', employee=employee)
 
@app.route('/updateemployee', methods=['POST'])
def updateemployee():
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        con = sqlite3.connect("testingdb.db")
        cur = con.cursor()
        if name == 'name':
           cur.execute("UPDATE employee SET name = ? WHERE id = ? ", (value, pk))
        elif name == 'email':
           cur.execute("UPDATE employee SET email = ? WHERE id = ? ", (value, pk))
        elif name == 'phone':
           cur.execute("UPDATE employee SET phone = ? WHERE id = ? ", (value, pk))
        # mysql.connection.commit()
        con.commit()
        cur.close()
        return json.dumps({'status':'OK'})
             
if __name__ == '__main__':
    app.run(debug=True)