import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='user1',
        password='password',
        autocommit=True
)

cursor = connection.cursor()

def task1():
    icao = input("ICAO: ").upper()
    sql = 'SELECT name, municipality FROM airport WHERE ident = %s'
    cursor.execute(sql, (icao, ))
    response = cursor.fetchall()
    if len(response) == 1:
        print(f"name: {response[0][0]}")
        print(f"location: {response[0][1]}")

def task2():
    iso_country = input("ISO country code: ").upper()
    sql = 'SELECT name, type FROM airport WHERE iso_country = %s ORDER BY type'
    cursor.execute(sql, (iso_country, ))
    response = cursor.fetchall()
    if len(response) > 0:
        for airport in response:
            print(f"name: {airport[0]}, type: {airport[1]}")

def task3():
    icao1 = input("ICAO 1: ").upper()
    icao2 = input("ICAO 2: ").upper()
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s OR ident = %s'
    cursor.execute(sql, (icao1, icao2))
    response = cursor.fetchall()
    if len(response) == 2:
        lat1 = response[0][0]
        lon1 = response[0][1]
        lat2 = response[1][0]
        lon2 = response[1][1]
        location1 = (lat1, lon1)
        location2 = (lat2, lon2)
        distance = geodesic(location1, location2).km
        print(f"distance: {distance} km")



if __name__ == '__main__':
    task1()
    task2()
    task3()