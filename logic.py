import sqlite3
from config import token, database


class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        con = sqlite3.connect(self.database)
        with con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS projects(
                    project_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    project_name TEXT NOT NULL,
                    description TEXT,
                    url TEXT,
                    status_id INTEGER,
                    FOREIGN KEY (status_id) REFERENCES status(status_id)
                    )
                """)
            
            con.execute("""CREATE TABLE IF NOT EXISTS skills(
                    skill_id INTEGER PRIMARY KEY,
                    skill_name TEXT
                    )
                """)
            
            con.execute("""CREATE TABLE IF NOT EXISTS project_skills(
                    project_id INTEGER,
                    skill_id INTEGER,
                    FOREIGN KEY(project_id) REFERENCES projects(project_id),
                    FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
                    )
                """)
            
            con.execute("""CREATE TABLE IF NOT EXISTS status(
                    status_id INTEGER PRIMARY KEY,
                    status_name TEXT
                    )
                """)

            con.commit()
            print("База данных успешно создана.")

