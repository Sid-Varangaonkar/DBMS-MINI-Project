import mysql.connector

def databaseConnection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="India@1234",
        database="Inventory_management"
    )

    cursor = conn.cursor(dictionary=True)
    return cursor, conn
