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
    print('\n')

def login(_conn):
    global currentUserID
    inp = input('Enter 1 to create account or 2 to login: \n')
    print('\n')
    if inp == '1':
        cur = _conn.cursor()
        firstName = input('Enter first name: \n')
        lastName = input('Enter last name: \n')
        email = input('Enter email: \n')
        cur.execute("""
                INSERT INTO Users(u_firstname, u_lastname, u_email, u_isactive) VALUES (?,?,?,?)
                """, (firstName, lastName, email, True))
        _conn.commit()
        currentUserID = cur.lastrowid
        print('Account Created Successfully \n')

    if inp == '2': 
        cur = _conn.cursor()
        email = input('Enter login email: \n')
        print('\n')
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
                print('Login Success \n')
                print('\n')
                return True

        print("login failed \n")
        return False

def eventManagement(_conn):
    while True:

        cur = _conn.cursor()
        inp = input('Enter 1 to manage Events, Enter 2 to manage Reminders, Enter 3 to manage Meetings, Enter 4 to manage Groups: \n')
        print('\n')
        if inp == '1':
            inp1 = input('Enter 1 to view all Events, Enter 2 to edit Events, Enter 3 to delete Events, Enter 4 to filter Events by Group: \n')
            print('\n')
            if inp1 == '1':
                cur.execute("""
                        SELECT e_title, e_description, e_location, e_attendee FROM Events WHERE e_userid = ?
                        """, (currentUserID,)) 
                _conn.commit()
                print(cur.fetchall(), '\n')
                print('\n')
                continue

            if inp == '2':
                cur1 = _conn.cursor()
                cur1.execute("""
                        SELECT r_title FROM Reminders WHERE r_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

            if inp == '3':
                cur2 = _conn.cursor()
                cur2.execute("""
                        SELECT m_title FROM Meetings WHERE m_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

        if inp == '2':
            inp2 = input('Enter 1 to view all Reminders, Enter 2 to edit Reminders, Enter 3 to delete Reminders, Enter 4 to filter Reminders by Priority: \n')
            print('\n')
            cur3 = _conn.cursor()
            if inp2 == '1':
                cur3.execute("""
                        SELECT r_title, r_description, r_date, r_priority FROM Reminders WHERE r_userid = ?
                        """, (currentUserID,)) 
                _conn.commit()
                print(cur3.fetchall(), '\n')
                print('\n')
                continue

            if inp2 == '2':
                cur4 = _conn.cursor()
                cur4.execute("""
                        SELECT r_title FROM Reminders WHERE r_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

            if inp2 == '3':
                cur5 = _conn.cursor()
                cur5.execute("""
                        SELECT m_title FROM Meetings WHERE m_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

        if inp == '3':
            inp3 = input('Enter 1 to view all Meetings, Enter 2 to edit Meetings, Enter 3 to delete Meetings: \n')
            print('\n')
            cur6 = _conn.cursor()
            if inp3 == '1':
                cur6.execute("""
                        SELECT m_title, m_attendee, m_link FROM Meetings WHERE m_userid = ?
                        """, (currentUserID,)) 
                _conn.commit()
                print(cur6.fetchall(), '\n')
                print('\n')
                continue

            if inp3 == '2':
                cur7 = _conn.cursor()
                cur7.execute("""
                        SELECT r_title FROM Meetings WHERE r_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

            if inp3 == '3':
                cur8 = _conn.cursor()
                cur8.execute("""
                        SELECT m_title FROM Meetings WHERE m_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

        if inp == '4':
            inp4 = input('Enter 1 to view all Groups, Enter 2 to edit Groups, Enter 3 to delete Groups: \n')
            print('\n')
            if inp4 == '1':
                cur9 = _conn.cursor()
                cur9.execute("""
                        SELECT g_title, g_type FROM Groups
                        """)
                _conn.commit()
                print(cur9.fetchall(), '\n')
                print('\n')
                continue

            if inp4 == '2':
                cur10 = _conn.cursor()
                cur10.execute("""
                        SELECT r_title FROM Meetings WHERE r_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

            if inp4 == '3':
                cur11 = _conn.cursor()
                cur11.execute("""
                        SELECT m_title FROM Meetings WHERE m_userid = ?
                        """, (currentUserID))
                _conn.commit()
                continue

def main():
    database = r"project.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        if login(conn):
            eventManagement(conn)

if __name__ == '__main__':
    main()
