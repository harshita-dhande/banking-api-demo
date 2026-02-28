def query_users(username):
    # Using parameterized queries with placeholders (?)
    return "SELECT * FROM users WHERE username = ?"