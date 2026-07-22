from database.connection import DatabaseConnection


class Repository:

    def __init__(self):

        self.db = DatabaseConnection()

        self.cursor = self.db.cursor()

    def commit(self):

        self.db.commit()

    def close(self):

        self.db.close()
        