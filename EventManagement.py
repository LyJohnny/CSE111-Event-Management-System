import sqlite3
from sqlite3 import Error
import json

currentUserID = ''

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def login(_conn):
    inp = input('Enter 0 to create account or 1 to login: ')
    if inp == '0':
        cur = _conn.cursor()
        firstName = input('Enter first name: ')
        lastName = input('Enter last name: ')
        email = input('Enter email: ')
        cur.execute("""
                INSERT INTO Users(u_firstname, u_lastname, u_email, u_isactive) VALUES (?,?,?,?)
                """, (firstName, lastName, email, True))
        _conn.commit()
        currentUserID = cur.lastrowid
        print('Account Created Successfully')
    if inp == '1': 
        cur = _conn.cursor()
        email = input('Enter login email: ')
        sql = """
            SELECT u_email FROM Users;
        """
        cur.execute(sql)

        cur1 = _conn.cursor()
        cur1.execute("""
                SELECT u_id FROM Users WHERE u_email = ?
                """, (email,))
        _conn.commit()
        currentUserID = cur1.fetchone()[0]

        rows = cur.fetchall()
        rows = tuple(rows)
        for i in rows:
            if email in i:
                print("Login Success")
                return True

        print("login failed")
        return False

def eventsList(_conn):
    cur = _conn.cursor()
    inp = input('Enter 0 to view or 1 to login: ')
    sql = """
        SELECT e_title FROM Events;
    """
    cur.execute(sql)
    rows = cur.fetchall()

def main():
    database = r"project.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        if login(conn):
            eventsList(conn)

if __name__ == '__main__':
    main()
