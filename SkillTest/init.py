import sqlite3


db = sqlite3.connect("skilltest.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE exam (exam_id INTEGER NOT NULL, exam_name varchar(250) NOT NULL, question_id integer PRIMARY KEY AUTOINCREMENT, question varchar(250) NOT NULL, option_1 varchar(250), option_2 varchar(250),option_3 varchar(250),option_4 varchar(250),answer varchar(250))")
cursor.execute("CREATE TABLE user (user_id INTEGER PRIMARY KEY AUTOINCREMENT, user_name varchar(250) NOT NULL, exam_1 varchar(250)"
               ",exam_2 varchar(250),exam_3 varchar(250),exam_4 varchar(250),password varchar(250))")
