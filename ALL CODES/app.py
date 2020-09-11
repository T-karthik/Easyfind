from flask import Flask ,render_template,request,redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app=Flask(__name__)

app.secret_key = 'a@12#4'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='kk#123'
app.config['MYSQL_DB']='flask'

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/home1.html')
def home1():
    return render_template('home1.html')

@app.route('/signup.html', methods=['GET','POST'])
def studentsignup():
    if request.method == 'POST':
        details = request.form
        emailid = details['email']
        username = details['username']
        password = details['password']
        confirm_password = details['conpassword']
        cur = mysql.connection.cursor()
        if password == confirm_password:
            cur.execute("INSERT INTO studenttable(email, username, password, confirmpassword) VALUES (%s, %s, %s, %s)", (emailid, username, password, confirm_password))
            mysql.connection.commit()
            cur.close()
            return render_template('home1.html')
        else:
            return ("password couldn't match")
    return render_template('signup.html')

@app.route('/studentlogin.html', methods=['GET','POST'])
def studentlogin():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM studenttable WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['1234'] = account['username']
            session['username'] = account['username']
            # Redirect to home page
    #        return ('Logged in successfully!')
            return render_template('ece.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('studentlogin.html')

@app.route('/css.html')
def studentcss():
    conn = MySQLdb.connect("localhost","root","Avinash#123","flask" )
    cursor = conn.cursor()
    cursor.execute("select * from finalpdf")
    data = cursor.fetchall() #data from database
    return render_template("css.html", value=data)


@app.route('/contactus.html')
def co():
    return render_template('contactus.html')

@app.route('/electronics.html', methods=['GET','POST'])
def electronics():
    conn = MySQLdb.connect("localhost","root","Avinash#123","flask" )
    cursor = conn.cursor()
    cursor.execute("select * from ecefield")
    data = cursor.fetchall() #data from database
    return render_template('electronics.html', value=data)






@app.route('/adminlogin.html', methods=['GET','POST'])
def admin():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['1234'] = account['username']
            session['username'] = account['username']
            # Redirect to home page
    #        return ('Logged in successfully!')
            return render_template('adminhome.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('adminlogin.html')

@app.route('/adminsubjects.html', methods=['GET','POST'])
def adminsubjects():
    return render_template('adminsubjects.html')


@app.route('/adminhome.html', methods=['GET','POST'])
def adminhome():
    return render_template('adminhome.html')




@app.route('/adminelectronics.html', methods=['GET','POST'])
def adminelectronics():
    conn = MySQLdb.connect("localhost","root","Avinash#123","flask" )
    cursor = conn.cursor()
    cursor.execute("select * from ecefield")
    data = cursor.fetchall() #
    if request.method == 'POST':
       details = request.form
       pdfname = details['pdf']
       pdflink = details['pdflink']
       wordname = details['document']
       wordlink = details['documentlink']
       youtubename = details['youtube']
       youtubelink = details['youtubelink']
       cur = mysql.connection.cursor()
       cur.execute("INSERT INTO ecefield(pdfname, pdflink, researchname, researchlink, youtubename, youtubelink) VALUES (%s, %s, %s, %s, %s, %s)", (pdfname, pdflink, wordname, wordlink, youtubename, youtubelink))
       mysql.connection.commit()
       cur.close()
    return render_template('adminelectronics.html', value=data)

@app.route('/adminstudentdata.html', methods=['GET','POST'])
def user():
    conn = MySQLdb.connect("localhost","root","Avinash#123","flask" )
    cursor = conn.cursor()
    cursor.execute("select * from studenttable")
    data = cursor.fetchall() #data from database
    return render_template("adminstudentdata.html", value=data)



@app.route('/admincss.html', methods=['GET','POST'])
def css():
    conn = MySQLdb.connect("localhost","root","Avinash#123","flask" )
    cursor = conn.cursor()
    cursor.execute("select * from finalpdf")
    data = cursor.fetchall() #
    if request.method == 'POST':
        details = request.form
        pdfname = details['pdf']
        pdflink = details['pdflink']
        wordname = details['document']
        wordlink = details['documentlink']
        youtubename = details['youtube']
        youtubelink = details['youtubelink']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO finalpdf(pdfname, pdflink, researchname, researchlink, youtubename, youtubelink) VALUES (%s, %s, %s, %s, %s, %s)", (pdfname, pdflink, wordname, wordlink, youtubename, youtubelink))
        mysql.connection.commit()
        cur.close()
    return render_template('admincss.html', value=data)



if __name__=='__main__':
    app.run(debug=True,port="4000")
