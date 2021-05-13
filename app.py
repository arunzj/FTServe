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
@app.route('/',methods=['GET','POST'])
def index():
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
                    return redirect(url_for('table'))
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


#main
if __name__ == '__main__':

    app.secret_key='secret123'
    app.run(debug=True,threaded=True)