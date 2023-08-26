from flask import Flask, request
#from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
        host="mydb",
        user="root",
        password="helloworld"
        )

#mycursor = mydb.cursor()

@app.route("/")
def hello_world():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    para = ""
    for x in mycursor:
        para += f"<p>{x}</p>"

    return para

app.run(host="0.0.0.0", port=5400)
