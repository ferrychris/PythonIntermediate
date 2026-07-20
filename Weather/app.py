import requests
import sqlite3
import json

URL = "https://data.api.xweather.com/conditions/new%20york%2C%20ny?client_id=WP7UJChbE9Dhw8LjWBrTj&{CLIENT_ID}"
response = requests.get(URL)
data= response.json()
print(data)

conn = sqlite3.connect('crypto.db')
cursor = conn.cursor()
try: 
    conn = sqlite3.connect('crypto.db')
    print("Data connected")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_conditions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        state TEXT,
        temperature_f REAL,
        humidity INTEGER,
        condition TEXT,
        date_recorded TEXT
    );
'''
)
weather_info = data["response"][0]
city_name =weather_info["place"]["name"]
state_name=weather_info["place"]["state"]
periods = weather_info["periods"][0]
temperature = periods["tempF"]
humidity=periods["humidity"]
condition = periods["weather"]
date_recorded= periods["dateTimeISO"]
# current_period=weather_info["current_period"]


cursor.execute(""" 
            INSERT INTO weather_conditions (
                city,
                state,
                temperature_f,
                humidity,
                condition,
                date_recorded
            )
            VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?   
            ) """ , (city_name,
            state_name, temperature, humidity, condition, date_recorded))


conn.commit()
conn.close()
print("Data inserted into the database")


cursor.execute("SELECT *FROM weather_conditions")
results=cursor.fetchall()
print(results)

# print("Data inserted successfully!")

# if response.status_code == 200:
#     print("Data Inserted")
# else:
#     print(f"Error: {response.status_code}")

# |Read
cursor.execute("SELECT * FROM weather_conditions")
results = cursor.fetchall()
print(results)

# conn.close()

# update
cursor.execute("""
                UPDATE weather_conditions
                SET 
                temperature_f = 75
                WHERE city = 'new york'
""")
conn.commit()

print("Data updated successfully!")


# UPdateNewYork
cursor.execute("UPDATE weather_conditions SET temperature_f = 80 WHERE city = 'new york'")
conn.commit()

# delete newyork
cursor.execute("DELETE FROM weather_conditions WHERE city = 'new york'")
try:
    cursor.execute("DELETE FROM weather_conditions WHERE city = 'new york'")
    conn.commit()
except sqlite3.Error as e:
    print(f"Error deleting data: {e}")
conn.commit()


cursor.execute("SELECT * FROM weather_conditions")
results = cursor.fetchall()
print(results)
print("Data deleted successfully!")

conn.close()
