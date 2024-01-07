# -*- coding: utf-8 -*-

users_sqls = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        score DOUBLE 
    );
'''