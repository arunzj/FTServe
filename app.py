from typing import ItemsView
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging,jsonify,make_response
#from data import Articles
import json
from flask_mysqldb import MySQL
from werkzeug.utils import html
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'mysql-instance1.ctrffvygguml.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '04812340484'
app.config['MYSQL_DB'] = 'ftserve'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL()
mysql.init_app(app)

#Login Form (Main)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE user_name= %s ",[username])
        record = cur.fetchone()
        if result>0:
            passwordx = record['password']
            #if password correct
            if passwordx == password:
                #if it is service
                if record['type'] == 'service':
                    session['type'] = 'service'
                    session['user_name']=username
                    return redirect(url_for('service'))
                elif record['type'] == 'back-house':
                    session['type'] = 'back-house'
                    session['user_name']=username
                    return redirect(url_for('back_house'))
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

@app.route('/service/newOrder/customerID/<string:id>',methods=['GET','POST'])
def new_order(id,msg=None):
    cur = mysql.connection.cursor()
    if request.method=='GET':
        result=cur.execute("select * from items where category='starter' ")
        items=cur.fetchall()
        result=cur.execute("select * from customers where customer_ID=%s",[id])
        customer=cur.fetchone()
        return render_template('/service/new_order/catalogue.html',items=items,customer=customer,msg=msg)
    else:
        item_ID=request.form['item_ID']
        quantity=request.form['quan']
        sql = "INSERT INTO orders (item_ID, quantity, customer_ID) VALUES (%s, %s,%s)"
        para = (item_ID,quantity,id)
        cur.execute(sql, para)
        mysql.connection.commit()
        return redirect(url_for('new_order',id=id,msg='Success'))

#back of house home page
@app.route('/back-house',methods=['GET'])
def back_house():
    cur=mysql.connection.cursor()
    result = cur.execute("Select o.order_ID,i.name,o.quantity,o.status from orders o inner join items i on o.item_ID=i.item_ID where o.status in ('OTkN','PRNG','PRPD')")
    order_info=cur.fetchall()
    return render_template('/back-of-house/back_house_hompage.html',order_info=order_info)
   

# api for info
@app.route('/getVacantTables')
def vacant_tables():
    cur = mysql.connection.cursor()
    result=cur.execute("select * from tables where status='VA' ")
    records=json.dumps(cur.fetchall())
    
    return jsonify(records)

#main
if __name__ == '__main__':

    app.secret_key='secret123'
    app.run(debug=True,threaded=True)