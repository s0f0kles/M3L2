from logic import DB_Manager
from config import database

if __name__ == '__main__':
    manager = DB_Manager(database)
   # manager.create_tables()
    manager.default_insert()
    manager.insert_project([(1, 'Tsyplonok_kjutBot', 'https://github.com/s0f0kles/Tsyplonok_kjutBot.git', 5)])
    manager.update_projects('descripcion', ('Telegram bot'), 'Tsyplonok_kjutBot', 1)