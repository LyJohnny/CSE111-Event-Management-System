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
            inp1 = input('Enter 1 to view all Events, Enter 2 to edit Events, Enter 3 to delete Events, Enter 4 to filter Events by Group, Enter 5 to add Events, Enter 6 to filter ongoing Events : ')
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

                inp2 = input('Enter the Event you wish to update: ')
                inp4 = input('Enter the table you want to edit (Title, Description, Location, Attendee): ')
                # print('\n')

                if inp4 == 'Title':
                    cur1 = _conn.cursor()
                    cur2 = _conn.cursor()

                    edTitle = input('Enter the updated Event title: ')
                    sql1 = """ 
                    UPDATE Events SET e_title = ? WHERE e_title = ?

                    """
                    cur1.execute(sql1,[edTitle, inp2])
                    _conn.commit()

                    sql2 = """ 
                     UPDATE Status SET s_title = ? WHERE s_title = ?

                     """
                    cur2.execute(sql2,[edTitle, inp2])
                    _conn.commit()

                    print('Event:', inp2, 'has updated', inp4, 'to:', edTitle)
                    print('++++++++++++++++++++++++++++++++++ \n')
                if inp4 == 'Description':
                    cur2 = _conn.cursor()
                    edDesc = input('Enter the updated description: ')
                    sql2 = """ 
                    UPDATE Events SET e_description = ? WHERE e_title = ?

                    """
                    cur2.execute(sql2,[edDesc, inp2])
                    _conn.commit()
                    print('Event:', inp2, 'has updated', inp4, 'to:', edDesc)
                    print('++++++++++++++++++++++++++++++++++ \n')

                if inp4 == 'Location':
                    cur3 = _conn.cursor()
                    edLocation = input('Enter the updated location: ')
                    sql3 = """ 
                    UPDATE Events SET e_location = ? WHERE e_title = ?

                    """
                    cur3.execute(sql3,[edLocation, inp2])
                    _conn.commit()
                    print('Event:', inp2, 'has updated', inp4, 'to:', edLocation)
                    print('++++++++++++++++++++++++++++++++++ \n')    

                if inp4 == 'Attendee':
                    cur4 = _conn.cursor()
                    edAttendee = input('Enter the updated attendee: ')
                    sql4 = """ 
                    UPDATE Events SET e_attendee = ? WHERE e_title = ?

                    """
                    cur4.execute(sql4,[edAttendee, inp2])
                    _conn.commit()
                    print('Event:', inp2, 'has updated', inp4, 'to:', edAttendee)
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

            if inp1 == '6':
                print('++++++++++++++++++++++++++++++++++ \n')
                cur16 = _conn.cursor()
                sql = '''
                        SELECT e_title, e_description, e_location, e_attendee FROM Events INNER JOIN Status on Events.e_title = Status.s_title WHERE Status.s_ongoing = 1 AND Events.e_userid = ?
                        ''' 
                cur16.execute(sql, [currentUserID]) 
                l = '{:>10}{:>23}{:>28}{:>22}'.format('Title','Description','Location','Attendee')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur16.fetchall()
                for row in rows:
                    l = '{:>10}{:>30}{:>25}{:>16}'.format(row[0],row[1],row[2],row[3])
                    print(l)

                print('++++++++++++++++++++++++++++++++++ \n')

                continue



            # -----------------------------------------------------Reminders (inp2) --------------------------------------------------------------#

        if inp == '2':
            inp2 = input('Enter 1 to view all Reminders, Enter 2 to edit Reminders, Enter 3 to delete Reminders, Enter 4 to filter Reminders by Priority, Enter 5 to add Reminders: ')
            print('++++++++++++++++++++++++++++++++++ \n')
            cur3 = _conn.cursor()
            if inp2 == '1':
                cur3.execute("""
                        SELECT r_title, r_description, r_priority, r_date FROM Reminders WHERE r_userid = ?
                        """, (currentUserID,)) 
                _conn.commit()
                l = '{:>10}{:>25}{:>25}{:>16}'.format('Title','Description','Priority','Date')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur3.fetchall()
                for row in rows:
                    l = '{:>10}{:>25}{:>14}{:>34}'.format(row[0],row[1],row[2],row[3])
                    print(l)

                print('++++++++++++++++++++++++++++++++++ \n')
                continue

            if inp2 == '2':
                inp2 = input('Enter the Reminder you wish to update: ')
                inp4 = input('Enter the table you want to edit (Title, Description, Priority, Date): ')
                # print('\n')

                if inp4 == 'Title':
                    cur1 = _conn.cursor()
                    edTitle = input('Enter the updated Reminder title: ')
                    sql1 = """ 
                    UPDATE Reminders SET r_title = ? WHERE r_title = ?

                    """
                    cur1.execute(sql1,[edTitle, inp2])
                    _conn.commit()
                    print('Reminder:', inp2, 'has updated', inp4, 'to:', edTitle)
                    print('++++++++++++++++++++++++++++++++++ \n')
                if inp4 == 'Description':
                    cur2 = _conn.cursor()
                    edDesc = input('Enter the updated description: ')
                    sql2 = """ 
                    UPDATE Reminders SET r_description = ? WHERE r_title = ?

                    """
                    cur2.execute(sql2,[edDesc, inp2])
                    _conn.commit()
                    print('Reminder:', inp2, 'has updated', inp4, 'to:', edDesc)
                    print('++++++++++++++++++++++++++++++++++ \n')

                if inp4 == 'Priority':
                    cur3 = _conn.cursor()
                    edPriority = input('Enter the updated Reminder priority: ')
                    sql3 = """ 
                    UPDATE Reminders SET r_priority = ? WHERE r_title = ?

                    """
                    cur3.execute(sql3,[edPriority, inp2])
                    _conn.commit()
                    print('Reminder:', inp2, 'has updated', inp4, 'to:', edLocation)
                    print('++++++++++++++++++++++++++++++++++ \n')    

                if inp4 == 'Date':
                    cur4 = _conn.cursor()
                    edDate = input('Enter the updated Reminder date: ')
                    sql4 = """ 
                    UPDATE Events SET r_date = ? WHERE r_title = ?

                    """
                    cur4.execute(sql4,[edDate, inp2])
                    _conn.commit()
                    print('Reminder:', inp2, 'has updated', inp4, 'to:', edDate)
                    print('++++++++++++++++++++++++++++++++++ \n')        
  
                continue

            if inp2 == '3':
                delRmdr = input('Enter the title of the Reminder you wish to delete: ')
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
            inp3 = input('Enter 1 to view all Meetings, Enter 2 to edit Meetings, Enter 3 to delete Meetings, Enter 4 to add a Meeting: ')
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
                inp2 = input('Enter the Meeting you wish to update: ')
                inp4 = input('Enter the table you want to edit (Title, Attendee, Link): ')
                # print('\n')

                if inp4 == 'Title':
                    cur1 = _conn.cursor()
                    edTitle = input('Enter the updated Meeting title: ')
                    sql1 = """ 
                    UPDATE Meetings SET m_title = ? WHERE m_title = ?

                    """
                    cur1.execute(sql1,[edTitle, inp2])
                    _conn.commit()
                    print('Meeting:', inp2, 'has updated', inp4, 'to:', edTitle)
                    print('++++++++++++++++++++++++++++++++++ \n')
                if inp4 == 'Attendee':
                    cur2 = _conn.cursor()
                    edAttendee = input('Enter the updated attendee: ')
                    sql2 = """ 
                    UPDATE Meetings SET m_attendee = ? WHERE m_title = ?

                    """
                    cur2.execute(sql2,[edAttendee, inp2])
                    _conn.commit()
                    print('Meeting:', inp2, 'has updated', inp4, 'to:', edAttendee)
                    print('++++++++++++++++++++++++++++++++++ \n')

                if inp4 == 'Link':
                    cur3 = _conn.cursor()
                    edLink = input('Enter the updated Meeting Link: ')
                    sql3 = """ 
                    UPDATE Meetings SET m_link = ? WHERE m_title = ?

                    """
                    cur3.execute(sql3,[edLink, inp2])
                    _conn.commit()
                    print('Meeting:', inp2, 'has updated', inp4, 'to:', edLink)
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

            if inp3 == '4':
                 title = input('Enter the Meeting title: \n')
                 attend = input('Enter the Meeting Attendee: \n')
                 link = input('Enter the Meeting Link: \n')
                 print('++++++++++++++++++++++++++++++++++ \n')
                 cur17 = _conn.cursor()
                 sql = '''
                         INSERT INTO Meetings (m_title, m_attendee, m_userid, m_link)
                         VALUES(?,?,?,?)
                         ''' 
                 cur17.execute(sql, [title, attend, currentUserID, link]) 
                 _conn.commit()
                 print('New Meeting titled:',title, 'created successfully!')

                 print('++++++++++++++++++++++++++++++++++ \n')

                 continue 
            # -----------------------------------------------------Groups (inp4) --------------------------------------------------------------#

        if inp == '4':
            inp4 = input('Enter 1 to view all Groups, Enter 2 to edit Groups, Enter 3 to delete Groups, Enter 4 to add Groups: ')
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
                inp2 = input('Enter the Group you wish to update: ')
                inp4 = input('Enter the table you want to edit (Title, Type): ')
                # print('\n')

                if inp4 == 'Title':
                    cur1 = _conn.cursor()
                    edTitle = input('Enter the updated Group title: ')
                    sql1 = """ 
                    UPDATE Groups SET g_title = ? WHERE g_title = ?

                    """
                    cur1.execute(sql1,[edTitle, inp2])
                    _conn.commit()
                    print('Group:', inp2, 'has updated', inp4, 'to:', edTitle)
                    print('++++++++++++++++++++++++++++++++++ \n')
                if inp4 == 'Type':
                    cur2 = _conn.cursor()
                    edType = input('Enter the updated Group Type: ')
                    sql2 = """ 
                    UPDATE Groups SET g_type = ? WHERE g_title = ?

                    """
                    cur2.execute(sql2,[edType, inp2])
                    _conn.commit()
                    print('Group:', inp2, 'has updated', inp4, 'to:', edType)
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

            if inp4 == '4':
                 title = input('Enter the Group title: \n')
                 typeG = input('Enter the Group type: \n')
                 print('++++++++++++++++++++++++++++++++++ \n')
                 cur18 = _conn.cursor()
                 sql = '''
                         INSERT INTO Groups (g_title, g_type)
                         VALUES(?,?)
                         ''' 
                 cur18.execute(sql, [title, typeG]) 
                 _conn.commit()
                 print('New Group titled:',title, 'created successfully!')

                 print('++++++++++++++++++++++++++++++++++ \n')

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
