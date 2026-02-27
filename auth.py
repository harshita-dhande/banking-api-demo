class UserDAO:
    def _get_user(self, user_input):
        # balance between security and readability
        return self._db.execute("SELECT * FROM users WHERE username = %s", (user_input,))

# Usage
dao = UserDAO()
user = dao.get_user("admin")