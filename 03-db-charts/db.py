# pip install mysql-connector-python

import mysql.connector

def get_connection():
    conn = mysql.connector.connect(host="host", user="user", password="some_pass", db="test", port=3306)
    cursor = conn.cursor(buffered=True, dictionary=True)
    return cursor, conn
