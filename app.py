from flask import Flask
import requests
import json
import sqlite3

app = Flask(__name__)

def get_bird(state: str):
    conn = sqlite3.connect("./birds.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sql = f"select * from birds where abbreviation = '{state.upper()}';"
    row = cursor.execute(sql)
    res = row.fetchall()
    list_accumulator = []
    print("Number of results:" + str(len(res)))
    for item in res:
        list_accumulator.append({k: item[k] for k in item.keys()})
    return json.dumps(list_accumulator)

def get_weather(state: str):
    request_url = f"https://api.weather.gov/alerts/active?area={state.upper()}"
    r = requests.get(request_url)
    return r.json()


@app.get('/')
def birds_and_weather():
    return "Add a 2 letter state param to learn about birds and the weather challenges they face.", \
           200, \
           {'Content-Type': 'text/html; charset=utf-8'}


@app.get('/<state>')
def bird(state):
    bird_info = get_bird(state)
    weather_info = get_weather(state)
    return {"status": 200,"bird_information": bird_info,"weather_information": weather_info}
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
