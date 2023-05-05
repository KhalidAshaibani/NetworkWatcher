# Connects the database

import sqlite3

DB_NAME = "/lib/NetworkWatcher/NetworkWatcher.db"
conn = sqlite3.connect(DB_NAME)