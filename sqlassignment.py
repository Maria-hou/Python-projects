#
# Python: 3.9.0
#
# Author: Maria Hou
#
# Purpose:  This program utilizes the sqlite3 module and
#           creates a database and a table, and the populates
#           that table with data that fits a specific criteria.
#           The data is then returned to the user.

import sqlite3

fileList = ('information.docs', 'Hello.txt', 'myImage.png',\
            'myMoive.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

def create_table(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")

def insert_data(conn):
    cur = conn.cursor()
    for file in fileList:

        # This retrieves all the files that have the extension of .txt
        if file[-4:] == '.txt':
            filename = file,                # This ensures that the data is presented as a tuple
            cur.execute("INSERT INTO tbl_files(col_fname)\
                VALUES(?)", filename)

def print_data(conn):
    cur = conn.cursor()

    # This gets the data from each row in the column col_fname from the table tbl_filesw
    for row in cur.execute("SELECT col_fname FROM tbl_files"):
        display_name = row[0]  
        print("File name: {}\n".format(display_name))

def main():
    conn = sqlite3.connect('assignment.db')
    with conn:
        create_table(conn)
        insert_data(conn)
        print_data(conn)
        conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

