import sqlite3
from sqlite3 import Error
import os
import pandas as pd


folder_path = "/Users/markusmuller/python/projects/content-db"
print(folder_path)

df = pd.read_csv(os.path.join(folder_path, 'gmail/data/KDnuggets/KDnuggets_data.csv'))
print(df.columns)
# print(df.info())

url_list = df['url'].values.tolist()
title_list = df['title'].values.tolist()
summary_list = df['summary'].values.tolist()
content_list = df['content'].values.tolist()
tag_list = df['tag'].values.tolist()

def createTable():
    try:
        # connect to db 
        con = sqlite3.connect('test.db')
        # query to create table
        sqlite_create_table_query = '''
            CREATE TABLE content (
            url TEXT,
            title TEXT,
            summary TEXT,
            content TEXT,
            tag TEXT);
        '''
        cursor = con.cursor()
        print("Successfully Connected to SQLIite")
        cursor.execute(sqlite_create_table_query)
        con.commit()
        print("SQLite table created")

    except Error as e:
        print("Error while creating a sqlite table", e)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")


def insertValuesTables():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        print('connected to db')

        insert_with_param = '''
        INSERT INTO content (
        url, title, summary, content, tag)
        VALUES(?, ?, ?, ?, ?);
        '''
        for x in range(len(url_list)):
            data_tuple = (url_list[x], title_list[x], summary_list[x], content_list[x], tag_list[x])
            cur.execute(insert_with_param, data_tuple)
            print(f"data inserted: {x}")
        con.commit()
        print("variables succesfully inserted into table")
        cur.close()

    except Error as e:
        print("Failed to insert variables into sqlite table")
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")

createTable()
insertValuesTables()
