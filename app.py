from flask import Flask,render_template,request,redirect,url_for
from flaskext.mysql import MySQL 

app = Flask(__name__)
mysql = MySQL()
app.config['TEMPLATES_AUTO_RELOAD']=True 

app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jilan3476'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_HOST'] = 'database.cd6r8d9nxxja.us-east-1.rds.amazonaws.com'
mysql.init_app(app)


@app.route('/',methods=['GET','POST'])
def register():
    if request.method=="POST":
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']
        company = userdetails['company']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO flasktab(name,email,company) VALUES (%s,%s,%s)",(name,email,company))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/data')
    return render_template("index.html")

@app.route('/data')
def display():
    conn = mysql.connect()
    cur =conn.cursor()
    results = cur.execute("SELECT * FROM flasktab")
    if results>0:
        results=cur.fetchall()
        return render_template('display.html',results=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

