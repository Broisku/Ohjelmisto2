from flask import Flask, Response
from collections import OrderedDict
import json
import mysql.connector

app = Flask(__name__)

@app.route('/kenttä/<string:icao>')
def kentta(icao):
    connect = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='lentopeli',
        user='root',
        password='krHV67fruiCT8d',
        autocommit=True
    )
    cursor = connect.cursor()
    try:
        cursor.execute("select name, municipality from airport where gps_code = %s", (icao,))
        result = cursor.fetchone()
    finally:
        cursor.close()
        connect.close()

    response = OrderedDict((
        ("ICAO", icao),
        ("Name", result[0]),
        ("Municipality", result[1]),
    ))

    json_response = json.dumps(response)
    return Response(json_response, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)