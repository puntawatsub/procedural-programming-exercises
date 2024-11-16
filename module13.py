from flask import Flask, request, jsonify
import math
import mysql.connector

app = Flask(__name__)


def is_prime(number: int) -> bool:
    num_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            num_list.append(i)
    if len(num_list) == 2 and (1 in num_list and number in num_list):
        return True
    else:
        return False


@app.route("/prime_number/<value>")
def prime_number(value):
    return jsonify({
        "Number": int(value),
        "isPrime": is_prime(int(value))
    })

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='user1',
    password='password',
    autocommit=True
)

cursor = connection.cursor()

@app.route('/airport/<ICAO>')
def airport(ICAO):
    ICAO = ICAO.upper()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (ICAO, ))
    results = cursor.fetchall()
    if len(results) != 1:
        return jsonify({
            "message": 'airport not found',
            "code": 400
        }), 400
    else:
        return jsonify({
            "ICAO": ICAO,
            "Name": results[0][0],
            "Location": results[0][1]
        }), 200
app.run(host='127.0.0.1', port=5000)






if __name__ == '__main__':
        # task1()
        task2()
