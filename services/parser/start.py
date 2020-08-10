from .config import DATABASE_URL
from .database.injectors import DB

DB.instance(DATABASE_URL).init_db()