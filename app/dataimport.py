import http.client
import ssl
import json
import sqlite3
from datetime import date, timedelta

today = date.today()
yesterday = date.today()-timedelta(days = 1)
d1 = today.strftime("%Y-%m-%d")
d0 = yesterday.strftime("%Y-%m-%d")

ssl._create_default_https_context = ssl._create_unverified_context

def importData():
    conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")

    headers = {'x-rapidapi-key': "71709e029cmshd066fbc13e4647ap1c03ddjsndaad257b537b",'x-rapidapi-host': "meteostat.p.rapidapi.com"}
    conn.request("GET", "/stations/daily?station=10382&start=" + d1 + "&end=" + d1, headers=headers)
    res = conn.getresponse()
    data = res.read()
    jsonData = json.loads(data)

    insertValue = jsonData['data']
    s=""
    for key, value in jsonData['data'][0].items():
        s+=str("'%s'," % value)

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO weather VALUES (%s)" %s[:-1])
    connection.commit()
    connection.close()

def displayData():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM weather")
    rows = cursor.fetchall()
    connection.close()
    return(rows)
