import sqlite3

class StudentModel:
    def __init__(self, db_name='Project.db'):
        self.conn = sqlite3.connect(db_name)
        