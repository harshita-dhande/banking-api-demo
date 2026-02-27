import sqlite3
from typing import Tuple

connection = sqlite3.connect('auth.db')
cursor = connection.cursor()
query = "SELECT * FROM users WHERE username = ?"
params: Tuple[str] = (user_input,)
cursor.execute(query, params)