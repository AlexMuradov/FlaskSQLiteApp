import sqlite3

connection = sqlite3.connect("database2.db")

cursor = connection.cursor()
#cursor.execute("CREATE TABLE weather (date TEXT, tavg TEXT, tmin TEXT, tmax TEXT, prcp TEXT, snow TEXT, wdir TEXT, wspd TEXT, wpgt TEXT, pres TEXT, tsun TEXT)")
cursor.execute("CREATE TABLE weather(ad TEXT, soy TEXT, old INTEGER)")
cursor.execute("INSERT INTO weather VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO weather VALUES ('Jamie', 'cuttlefish', 7)")
connection.commit()
print(connection.total_changes)
connection.close()
