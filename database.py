import sqlite3

def get_all_vehicles():

    conn = sqlite3.connect("vehicles.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, price, fuel, seats,
           category, mileage, transmission
    FROM vehicles
    """)

    vehicles = cursor.fetchall()

    conn.close()

    return vehicles