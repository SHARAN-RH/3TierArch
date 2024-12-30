from flask import Flask, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="database",
    user="root",
    password="root",
    database="corporates_db"
)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    cursor = db.cursor()
    query = "INSERT INTO corporates (name, email, address) VALUES (%s, %s, %s)"
    values = (data['name'], data['email'], data['address'])
    cursor.execute(query, values)
    db.commit()
    return "Corporate details saved successfully!", 200
