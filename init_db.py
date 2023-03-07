#!/usr/bin/env python3

import sqlite3

connect = sqlite3.connect('database.db')

with open('schema.sql') as f:
	connect.executescript(f.read())

	connect.commit()
	connect.close()
