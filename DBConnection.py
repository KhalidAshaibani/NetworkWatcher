# Connects the database

import sqlite3
from Consts import DB_NAME

conn = sqlite3.connect(DB_NAME)
