import db; cursor, db = db.get_connection()
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='MyWorkAds - City & Service Ads Count', page_icon='https://activetechsystems.com/wp-content/uploads/2025/03/ats-fav-300.png', layout="wide"
)

st.html('<h1>MyWorkAds - City & Service Ads Count</h1>')

# city chart
sql = """
    SELECT c.city, COUNT(*) AS count 
    FROM ad a, city c 
    WHERE a.city_id = c.id
    GROUP BY c.city
    ORDER BY Count DESC;
"""

cursor.execute(sql)
rows = cursor.fetchall()

city = []
count = []
for i in range(0, len(rows)):
    city.append(rows[i]['city'])
    count.append(rows[i]['count'])

st.html('<h3>City Ads Count</h3>')

city_chart_data = pd.DataFrame(count, city)
st.bar_chart(city_chart_data)


# service chart
sql = """
    SELECT s.service_title, COUNT(*) AS count 
    FROM ad a, service s
    WHERE a.service_id = s.id
    GROUP BY s.service_title
    ORDER BY Count DESC;
"""

cursor.execute(sql)
rows = cursor.fetchall()

service = []
count = []
for i in range(0, len(rows)):
    service.append(rows[i]['service_title'])
    count.append(rows[i]['count'])

st.html('<h3>Service Ads Count</h3>')

service_chart_data = pd.DataFrame(count, service)
st.bar_chart(service_chart_data)
