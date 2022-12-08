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
    inp = input('Enter 1 to create account or 2 to login: ')
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
        email = input('Enter login email: ')
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
                print('Login Success')
                print('++++++++++++++++++++++++++++++++++ \n')
                return True

        print("Login failed")
        return False

def eventManagement(_conn):
    while True:

        cur = _conn.cursor()
        inp = input('Enter 1 to manage Events, Enter 2 to manage Reminders, Enter 3 to manage Meetings, Enter 4 to manage Groups: ')
        print('++++++++++++++++++++++++++++++++++ \n')
        if inp == '0':
            quit()
            # -----------------------------------------------------Events (inp1) --------------------------------------------------------------#
        if inp == '1':
            inp1 = input('Enter 1 to view all Events, Enter 2 to edit Events, Enter 3 to delete Events, Enter 4 to filter Events by Group, Enter 5 to add Events: ')
            print('++++++++++++++++++++++++++++++++++ \n')
            if inp1 == '1':
                cur.execute("""
                        SELECT e_title, e_description, e_location, e_attendee FROM Events WHERE e_userid = ?
                        """, (currentUserID,)) 
                _conn.commit()
                l = '{:>10}{:>23}{:>28}{:>22}'.format('Title','Description','Location','Attendee')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur.fetchall()
                for row in rows:
                    l = '{:>10}{:>30}{:>25}{:>16}'.format(row[0],row[1],row[2],row[3])
                    print(l)
                
                print('++++++++++++++++++++++++++++++++++ \n')

                continue

            if inp1 == '2':
                inp2 = input('Enter the Event title you wish to update: ')
                inp3 = input('Enter the updated Event title: ')
                print('\n')
                cur1 = _conn.cursor()
                cur1.execute("""
                        UPDATE Events SET e_title = ? WHERE e_title = ?
                        """, [inp3, inp2])
                _conn.commit()
                print('Event:', inp2, 'has been updated to:', inp3)
                print('++++++++++++++++++++++++++++++++++ \n')
                continue

            if inp1 == '3':
                delEvnt = input('Enter the Event title you wish to delete: ')
                cur2 = _conn.cursor()
                cur2.execute("""
                        DELETE FROM Events WHERE e_title = ? AND e_userid = ?
                        """, [delEvnt,currentUserID])
                _conn.commit()
                print('You have successfully deleted Event: ', delEvnt)
                continue

            if inp1 == '4':
                inp2 = input('Enter the Group type you wish to filter your Events by: ')
                print('++++++++++++++++++++++++++++++++++ \n')
                cur12 = _conn.cursor()
                sql = '''
                        SELECT e_title, e_description, e_location, e_attendee FROM Events INNER JOIN Groups on Groups.g_id = Events.e_groupid WHERE Groups.g_type = ? AND Events.e_userid = ?
                        ''' 
                cur12.execute(sql, [inp2, currentUserID]) 
                l = '{:>10}{:>23}{:>28}{:>22}'.format('Title','Description','Location','Attendee')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur12.fetchall()
                for row in rows:
                    l = '{:>10}{:>30}{:>25}{:>16}'.format(row[0],row[1],row[2],row[3])
                    print(l)
                
                print('++++++++++++++++++++++++++++++++++ \n')

                continue

            if inp1 == '5':
                title = input('Enter the Event title: \n')
                descr = input('Enter the Event Description: \n')
                loc = input('Enter Event Location: \n')
                attend = input('Enter any Event Attendee: \n')
                grpId = input ('Enter a number from 1-4 for which Event Group you want to add this event to (1: Personal, 2: School, 3: Work, 4: Other): \n')
                print('++++++++++++++++++++++++++++++++++ \n')
                cur13 = _conn.cursor()
                sql = '''
                        INSERT INTO Events (e_title, e_description, e_location, e_attendee, e_groupid, e_userid)
                        VALUES(?,?,?,?,?,?)
                        ''' 
                cur13.execute(sql, [title, descr, loc, attend,grpId,currentUserID]) 
                _conn.commit()
                print('New Event titled:',title, 'created successfully!')

                print('++++++++++++++++++++++++++++++++++ \n')

                continue

            # -----------------------------------------------------Reminders (inp2) --------------------------------------------------------------#

        if inp == '2':
            inp2 = input('Enter 1 to view all Reminders, Enter 2 to edit Reminders, Enter 3 to delete Reminders, Enter 4 to filter Reminders by Priority, Enter 5 to add Reminders: ')
            print('++++++++++++++++++++++++++++++++++ \n')
            cur3 = _conn.cursor()
            if inp2 == '1':
                cur3.execute("""
                        SELECT r_title, r_description, r_date, r_priority FROM Reminders WHERE r_userid = ?
                        """, (currentUserID,)) 
                _conn.commit()
                l = '{:>10}{:>25}{:>25}{:>16}'.format('Title','Description','Priority','Date')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur3.fetchall()
                for row in rows:
                    l = '{:>10}{:>25}{:>25}{:>14}'.format(row[0],row[1],row[2],row[3])
                    print(l)
                
                print('++++++++++++++++++++++++++++++++++ \n')
                continue

            if inp2 == '2':
                inp1 = input('Enter the Reminder title you wish to update: ')
                inp3 = input('Enter the updated Reminder title: ')
                print('\n')
                cur4 = _conn.cursor()
                cur4.execute("""
                        UPDATE Reminders SET r_title = ? WHERE r_title = ?
                        """, [inp3, inp1])
                _conn.commit()
                print('Reminder:', inp1, 'has been updated to:', inp3)
                print('++++++++++++++++++++++++++++++++++ \n')
                continue

            if inp2 == '3':
                delRmdr = input('Enter the tilte of the Reminder you wish to delete: ')
                cur5 = _conn.cursor()
                cur5.execute("""
                        DELETE FROM Reminders WHERE r_title = ? AND r_userid = ?
                        """, [delRmdr,currentUserID])
                _conn.commit()
                print('You have successfully deleted Reminder: ', delRmdr)
                continue

            if inp2 == '4':
                inp4 = input('Enter the Priority type you wish to filter your Events by: ')
                print('\n')
                cur14 = _conn.cursor()
                sql = '''
                        SELECT r_title, r_description, r_priority, r_date FROM Reminders WHERE Reminders.r_priority = ? AND Reminders.r_userid = ?
                        ''' 
                cur14.execute(sql, [inp4, currentUserID])
                l = '{:>10}{:>25}{:>20}{:>16}'.format('Title','Description','Priority','Date')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur14.fetchall()
                for row in rows:
                    l = '{:>10}{:>25}{:>17}{:>26}'.format(row[0],row[1],row[2],row[3])
                    print(l)
                
                print('++++++++++++++++++++++++++++++++++ \n')

            if inp2 == '5':
                title = input('Enter the Reminder title: \n')
                descr = input('Enter the Reminder Description: \n')
                recur = input('Is this a recurring reminder? (0 for No, 1 for Yes): \n')
                priority = input('What is the priority of this reminder (low, medium or high)?: \n')
                date = input ('Enter the date and time for the reminder (YYYY-MM-DD HH:MM): \n')
                print('++++++++++++++++++++++++++++++++++ \n')
                cur15 = _conn.cursor()
                sql = '''
                        INSERT INTO Reminders (r_userid, r_title, r_description, r_recurring, r_priority, r_date)
                        VALUES(?,?,?,?,?,?)
                        ''' 
                cur15.execute(sql, [currentUserID, title, descr, recur, priority, date]) 
                _conn.commit()
                print('New Reminder titled:',title, 'created successfully!')

                print('++++++++++++++++++++++++++++++++++ \n')

                continue
            # -----------------------------------------------------Meetings (inp3) --------------------------------------------------------------#

        if inp == '3':
            inp3 = input('Enter 1 to view all Meetings, Enter 2 to edit Meetings, Enter 3 to delete Meetings: ')
            print('++++++++++++++++++++++++++++++++++ \n')
            cur6 = _conn.cursor()
            if inp3 == '1':
                cur6.execute("""
                        SELECT m_title, m_attendee, m_link FROM Meetings WHERE m_userid = ?
                        """, (currentUserID,)) 
                _conn.commit()
                l = '{:>10}{:>35}{:>23}'.format('Title','Attendee','Link')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur6.fetchall()
                for row in rows:
                    l = '{:>10}{:>30}{:>25}'.format(row[0],row[1],row[2])
                    print(l)
                
                print('++++++++++++++++++++++++++++++++++ \n')
                continue

            if inp3 == '2':
                inp1 = input('Enter the Meeting title you wish to update: ')
                inp2 = input('Enter the updated Meeting title: ')
                print('\n')
                cur7 = _conn.cursor()
                cur7.execute("""
                        UPDATE Meetings SET m_title = ? WHERE m_title = ?
                        """, [inp2, inp1])
                _conn.commit()
                print('Meeting:', inp1, 'has been updated to:', inp2)
                print('++++++++++++++++++++++++++++++++++ \n')
                continue
                
            if inp3 == '3':
                delMtng = input('Enter the title of the Meeting you wish to delete: ')
                cur8 = _conn.cursor()
                cur8.execute("""
                        DELETE FROM Meetings WHERE m_title = ? AND m_userid = ?
                        """, [delMtng,currentUserID])
                _conn.commit()
                print('You have successfully deleted Meeting: ', delMtng)
                continue
            # -----------------------------------------------------Groups (inp4) --------------------------------------------------------------#

        if inp == '4':
            inp4 = input('Enter 1 to view all Groups, Enter 2 to edit Groups, Enter 3 to delete Groups: ')
            print('++++++++++++++++++++++++++++++++++ \n')
            if inp4 == '1':
                cur9 = _conn.cursor()
                cur9.execute("""
                        SELECT g_title, g_type FROM Groups
                        """)
                _conn.commit()
                l = '{:>10}{:>30}'.format('Title','Type')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur9.fetchall()
                for row in rows:
                    l = '{:>10}{:>30}'.format(row[0],row[1])
                    print(l)
                
                print('++++++++++++++++++++++++++++++++++ \n')
                continue

            if inp4 == '2':
                inp1 = input('Enter the Group title you wish to update: ')
                inp2 = input('Enter the updated Group title: ')
                print('\n')
                cur10 = _conn.cursor()
                cur10.execute("""
                        UPDATE Groups SET g_title = ? WHERE g_title = ?
                        """, [inp2, inp1])
                _conn.commit()
                print('Group:', inp1, 'has been updated to:', inp2)
                print('++++++++++++++++++++++++++++++++++ \n')
                continue

            if inp4 == '3':
                delGrp = input('Enter the title of the Meeting you wish to delete: ')
                cur11 = _conn.cursor()
                cur11.execute("""
                        DELETE FROM Groups WHERE g_title = ? 
                        """, [delMtng])
                _conn.commit()
                print('You have successfully deleted Group: ', delGrp)
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