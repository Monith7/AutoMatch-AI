import sqlite3
import os

# Delete old database if it exists
if os.path.exists("vehicles.db"):
    os.remove("vehicles.db")

conn = sqlite3.connect("vehicles.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    fuel TEXT,
    seats INTEGER,
    category TEXT,
    mileage TEXT,
    transmission TEXT
)
""")

vehicles = [
    ("Maruti Alto K10", 450000, "Petrol", 5, "Hatchback", "24 kmpl", "Manual"),
    ("Maruti Swift", 800000, "Petrol", 5, "Hatchback", "24 kmpl", "Manual"),
    ("Maruti Baleno", 900000, "Petrol", 5, "Hatchback", "22 kmpl", "Automatic"),
    ("Hyundai Grand i10", 750000, "Petrol", 5, "Hatchback", "21 kmpl", "Manual"),
    ("Hyundai i20", 950000, "Petrol", 5, "Hatchback", "20 kmpl", "Automatic"),

    ("Tata Punch", 700000, "Petrol", 5, "SUV", "20 kmpl", "Manual"),
    ("Tata Nexon", 1200000, "Petrol", 5, "SUV", "17 kmpl", "Automatic"),
    ("Tata Curvv", 1500000, "Petrol", 5, "SUV", "18 kmpl", "Automatic"),
    ("Hyundai Venue", 1100000, "Petrol", 5, "SUV", "18 kmpl", "Automatic"),
    ("Hyundai Creta", 1500000, "Diesel", 5, "SUV", "21 kmpl", "Automatic"),
    ("Kia Sonet", 1200000, "Petrol", 5, "SUV", "18 kmpl", "Automatic"),
    ("Kia Seltos", 1600000, "Petrol", 5, "SUV", "18 kmpl", "Automatic"),
    ("Mahindra XUV 3XO", 1300000, "Petrol", 5, "SUV", "20 kmpl", "Automatic"),
    ("Mahindra Scorpio N", 1800000, "Diesel", 7, "SUV", "16 kmpl", "Manual"),
    ("Mahindra XUV700", 2000000, "Diesel", 7, "SUV", "17 kmpl", "Automatic"),
    ("Toyota Fortuner", 3500000, "Diesel", 7, "SUV", "14 kmpl", "Automatic"),
    ("MG Hector", 1800000, "Petrol", 5, "SUV", "15 kmpl", "Automatic"),
    ("MG ZS EV", 2200000, "Electric", 5, "SUV", "461 km range", "Automatic"),

    ("Honda City", 1400000, "Petrol", 5, "Sedan", "18 kmpl", "Automatic"),
    ("Volkswagen Virtus", 1600000, "Petrol", 5, "Sedan", "19 kmpl", "Automatic"),
    ("Skoda Slavia", 1550000, "Petrol", 5, "Sedan", "18 kmpl", "Automatic"),
    ("Hyundai Verna", 1700000, "Petrol", 5, "Sedan", "19 kmpl", "Automatic"),

    ("Toyota Innova Hycross", 2500000, "Hybrid", 7, "MPV", "23 kmpl", "Automatic"),
    ("Maruti Ertiga", 1200000, "Petrol", 7, "MPV", "20 kmpl", "Manual"),
    ("Kia Carens", 1600000, "Petrol", 7, "MPV", "18 kmpl", "Automatic")
]

cursor.executemany("""
INSERT INTO vehicles
(name, price, fuel, seats, category, mileage, transmission)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", vehicles)

conn.commit()
conn.close()

print("Database Created Successfully!")