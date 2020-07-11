# Imports:
from flask import Flask, render_template, request, redirect, url_for, session,flash,make_response,session
import datetime
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
import twilio
from twilio.rest import Client


# Configs:
app = Flask(__name__)

app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'b12wunhvgwb3vymtqngg-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'umo0wrj8n1rqnx90'
app.config['MYSQL_PASSWORD'] = 'ETintB86zfDXSCCMrspY'
app.config['MYSQL_DB'] = 'b12wunhvgwb3vymtqngg'
mysql = MySQL(app)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


# @app.before_request
# def before_request():
#     if request.url.startswith('http://'):
#         url = request.url.replace("http://","https://",1)
#         code = 301
#         return redirect(url,code=code)


# Routes:
@app.route('/customer/login', methods=['GET', 'POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM customer WHERE username = %s AND password = %s', (username, password,))
        customer = cursor.fetchone()
        if customer:
            session['loggedin'] = True
            session['id'] = customer['cus_id']
            session['username'] = customer['username']
            session['mobile'] = customer['mobileno']
            session['region'] = customer['region']
            return redirect(url_for('customer_display'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('cuslogin.html',msg=msg)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/shop/login', methods=['GET', 'POST'])
def login1():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM shop WHERE username = %s AND password = %s', (username, password,))
        shop = cursor.fetchone()
        if shop:
            session['loggedin'] = True
            session['id'] = shop['shopid']
            session['username'] = shop['username']
            session['mobile'] = shop['mobile']
            session['region'] = shop['region']
            session['address'] = shop['address']
            session['shop_name'] = shop['shop_name']
            session['owner_name'] = shop['owner_name']
            return redirect(url_for('display'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('shoplogin.html',msg=msg)