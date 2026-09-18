from database.database import Database
import questionary


class Session:
    user_id = None

    def __init__(self):
        self.database = Database()

    def get_session(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        username = questionary.text("Enter your username: ").ask()
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        connection.close()

        if row:
            Session.user_id = row[0]
            print(f"\nWelcome back {username}!")
            return row[0]
        else:
            print("User not found!")
            return None

    def create_username(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        username = questionary.text("Enter new username: ").ask()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        connection.commit()
        Session.user_id = cursor.lastrowid
        connection.close()
        print("User created successfully!")
        return Session.user_id

    @classmethod
    def get(cls, key="user_id"):
        return cls.user_id