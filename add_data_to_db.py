import pandas as pd
import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'host': 'localhost',         # your database host ip address
    'port': '5432',              # default PostgreSQL port
    'user': 'postgres',          # a user within Postgres
    'password': 'mypassword',    # password to access DB
    'dbname': 'airlinedb',       # Database name
}


# Read the CSV file
data = pd.read_csv('Flights_Schedule.csv')


# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    for index, row in data.iterrows():
        cursor.execute(
            sql.SQL("""
                INSERT INTO flights (
                    id, flight_no, airline_code, airline_name,
                    origin, destination, departure_scheduled, arrival_scheduled,
                    status, delay_minutes, delay_reason,
                    terminal, gate, aircraft_type,
                    seats_total, seats_booked, fare_inr
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """),
            (
                row["id"],
                row["flight_no"],
                row["airline_code"],
                row["airline_name"],
                row["origin"],
                row["destination"],
                row["departure_scheduled"],
                row["arrival_scheduled"],
                row["status"],
                row["delay_minutes"],
                row["delay_reason"],
                row["terminal"],
                row["gate"],
                row["aircraft_type"],
                row["seats_total"],
                row["seats_booked"],
                row["fare_inr"]
            )
        )

    # Commit the transaction
    conn.commit()
    print(f"\nData inserted successfully.\n")


except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()

