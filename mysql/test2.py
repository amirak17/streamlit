import db 
import streamlit as st
cursor, db = db.get_connection()

sql = 'SELECT * FROM posts'
cursor.execute(sql)
rows = cursor.fetchall()

# all rows
for i in range(0, len(rows)):
    st.write(rows[i]['title'])
