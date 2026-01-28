import sqlite3

def login(username, password):
    # CRITICAL: Vulnerable to SQL Injection
    # Red Agent will attack this line
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    # Execute
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()