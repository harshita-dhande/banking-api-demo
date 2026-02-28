# auth.py, line 4
import sqlite3

def authenticate_user(username, password):
    # Validate inputs
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Parameterized query with input validation
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Example usage:
try:
    auth_user("john_doe", "secure_password")
except ValueError as e:
    print(e)