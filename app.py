from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'app'
app.config['MYSQL_PASSWORD'] = 'app1234'
app.config['MYSQL_DB'] = 'ftserve'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)


#Login Form (Main)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        cur=mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE user_name= %s ",[username])
        
        if result > 0:
            record = cur.fetchone()
            passwordx = record['password']
            #if password correct
            if passwordx == password:
                #if it is service
                if record['type'] == 'service':
                    session['type'] = record['type']
                    session['user_name']=username
                    return redirect(url_for('service'))
                elif record['type'] == 'chef':
                    session['type'] = record['type']
                    session['user_name']=username
                    return redirect(url_for('chef'))
                elif record['type'] == 'accounts':
                    session['user_name']=username
                    return redirect(url_for('accounts'))
                else:
                    return 'Under Construction'
        #if password incorrect   
            else:
                msg='wrong password'
                return render_template('msg.html',msg=msg)
    #if username wrong
        else:

            return 'no user'
 
    return render_template('index.html')

@app.route('/',methods=['GET'])
def index():
    return redirect(url_for('login'))


@app.route('/catalogue/category/<string:id>',methods=['GET'])
def menu(id):
    cur = mysql.connection.cursor()
    result=cur.execute("select * from items where category=%s",[id])
    items=cur.fetchall()
    return render_template('catalogue/catalogue.html',items=items)

@app.route('/catalogue/category',methods=['GET'])
def menu_default():
    return redirect(url_for('menu',id='starter'))

@app.route('/service',methods=['GET'])
def service():
    cur=mysql.connection.cursor()
    result = cur.execute(" SELECT o.order_ID,i.name,t.table_ID,o.status,o.quantity FROM customers c INNER JOIN orders o ON c.customer_ID=o.customer_ID INNER JOIN  tables t ON c.table_ID=t.table_ID INNER JOIN items i ON o.item_ID=i.item_ID WHERE c.status='AC' and o.status!='SRVD' ")
    orders=cur.fetchall()
    result = cur.execute("SELECT * FROM users WHERE user_name=%s",[session['user_name']])
    user=cur.fetchone()
    result = cur.execute("SELECT * FROM customers WHERE status='AC'")
    customers=cur.fetchall()
    result=cur.execute("SELECT COUNT(*) count FROM orders WHERE status='SRVD'")
    serv_order=cur.fetchone()
    return render_template('service/service_hompage.html',orders=orders,user=user,customers=customers,serv_order=serv_order)


#main
if __name__ == '__main__':

    app.secret_key='secret123'
    app.run(debug=True,threaded=True)