import sqlite3

def get_user_by_id(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Validate and escape user input
    escaped_user_id = sqlite3.escape_string(str(user_id))
    cursor.execute("SELECT * FROM users WHERE id = ?", (escaped_user_id,))
    user = cursor.fetchone()
    conn.close()
    return user