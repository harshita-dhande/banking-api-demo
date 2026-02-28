import sqlite3

def query_database(user_input):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Using parameterized queries with placeholders (?)
    query = "SELECT * FROM users WHERE username=?"
    cursor.execute(query, (user_input,))
    return cursor.fetchall()

# Example usage
user_input = 'example_user'
results = query_database(user_input)