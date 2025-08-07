from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'yashu_ece'
mysql = MySQL(app)


@app.route("/index", methods=["GET"])  
def index():
    sql = f"SELECT * FROM people"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return render_template("index.html", results = results)

@app.route("/about", methods=["GET"])  
def about():
    return render_template("about.html")


@app.route("/post", methods=["GET"])  
def blog():
    return render_template("post.html")

@app.route("/contact", methods=["GET"])  
def contact():
    return render_template("contact.html")

if __name__ == '__main__':  
    app.run()     