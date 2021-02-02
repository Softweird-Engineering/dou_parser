import os


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL')

    BOT_API = os.getenv('BOT_API')
    ADMIN_ID = int(os.getenv('ADMIN_ID'))
    INIT_DB = bool(os.getenv('INIT_DB').lower() == 'true')
