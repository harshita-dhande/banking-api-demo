import sqlite3

db_connection = sqlite3.connect('your_database.db')
cursor = db_connection.cursor()

user_id = None
password_hashed = "hashed_password"  # Replace with actual hashed password

query = """SELECT user_id 
              FROM users 
             WHERE username = ? AND password_hash = ?;"""
values = (user_input_username, password_hashed)

cursor.execute(query, values)
result = cursor.fetchone()

if result:
    user_id = result[0]

cursor.close()
db_connection.close()

# Process user_id as needed