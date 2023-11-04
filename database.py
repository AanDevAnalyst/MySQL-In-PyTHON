import mysql.connector

config = {
    'user': 'root',
    'password': '09036259681',
    'host': 'local host'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()