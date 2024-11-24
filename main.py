from logic import DB_Manager
from config import database

if __name__ == '__main__':
    manager = DB_Manager(database)
    manager.create_tables()