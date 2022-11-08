CREATE TABLE IF NOT EXISTS Events (
    e_title VARCHAR(255) NOT NULL,
    e_description VARCHAR(255) NOT NULL,
    e_location VARCHAR(255) NOT NULL,
    e_attendee VARCHAR(255) NOT NULL,
    e_groupid INTEGER NOT NULL,
    e_userid INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Reminders (
    r_userid INTEGER NOT NULL,
    r_title VARCHAR(255) NOT NULL,
    r_description VARCHAR(255) NOT NULL,
    r_recurring BOOLEAN NOT NULL,
    r_priority VARCHAR(255) NOT NULL,
    r_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Status (
    s_title VARCHAR(255) NOT NULL,
    s_draft BOOLEAN NOT NULL,
    s_open BOOLEAN NOT NULL,
    s_ongoing BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS Groups (
    g_id INTEGER NOT NULL,
    g_title VARCHAR(255) NOT NULL,
    g_type VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Meetings (
    m_title VARCHAR(255) NOT NULL,
    m_attendee VARCHAR(255) NOT NULL,
    m_userid INTEGER NOT NULL,
    m_link VARCHAR(255) NOT NULL
); 

CREATE TABLE IF NOT EXISTS Users (
    u_id INTEGER NOT NULL,
    u_firstname VARCHAR(255) NOT NULL,
    u_lastname VARCHAR(255) NOT NULL,
    u_email VARCHAR(255) NOT NULL,
    u_isactive BOOLEAN NOT NULL
);

INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Lunch With Bob', 'Catch up', 'Central Park', 'Bob', 1 , 1);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Coffee With Bruce', 'Catch up', 'Starbucks', 'Bruce', 1, 1);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Meeting', 'Collaboration', 'Coffee Shop', 'Heather', 4, 3);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Basketball Game', 'live', 'Home', ' ', 3, 5);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Baseball Game', 'live', 'Home', '', 4, 5);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Exercise', 'daily workout', 'Gym', ' ', 2, 6);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Walk', 'daily walk', 'Mount Fuji', ' ', 3, 6);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Run', 'daily run', 'Downtown', ' ', 1, 2);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Dinner', 'dinner with friend', 'Cheesecake Factory', 'Jack', 3, 4);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Lunch', 'lunch with coworker', 'Poke', 'Travis', 4, 4);

UPDATE Events
SET e_title = 'Dinner with Jack' 
WHERE e_groupid = 5 AND e_userid = 4;


UPDATE Events
SET e_description = 'Discuss startup idea',
e_location = 'Starbucks on 5th avenue'
WHERE
e_title = 'Coffee With Bruce';


UPDATE Events
SET e_description = 'daily run to Central park',
e_attendee = 'Jacky', e_location = 'Downtown Manhattan'
WHERE
e_title = 'Run';

DELETE FROM Events
WHERE e_title = 'Exercise' AND e_location = 'GYM';


INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (1, 'Midterm 1', 'MATH-141', FALSE, 'High', '2022-11-17 13:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (2, 'Final Test', 'MATH-141', FALSE, 'High', '2022-12-17 15:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (3, 'Code Review', 'Team code review', TRUE, 'Medium', '2022-11-15 10:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (5, 'Product Launch', 'Watch Party', FALSE, 'High', '2022-11-26 09:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (4, 'Meeting', 'Team meeting', TRUE, 'High', '2022-12-05 11:00');

UPDATE Reminders
SET r_description = 'CSE 111'
WHERE
r_title = 'Final Test';

UPDATE Reminders
SET r_priority = 'Medium'
WHERE
r_title = 'Product Launch' AND r_description = 'Watch Party';

INSERT INTO Groups(g_title, g_type, g_id) VALUES ('Birthdays', 'Personal', 1);
INSERT INTO Groups(g_title, g_type, g_id) VALUES ('Fall Schedule', 'School', 2);
INSERT INTO Groups(g_title, g_type, g_id ) VALUES ('Company Events', 'Work', 3);
INSERT INTO Groups(g_title, g_type, g_id ) VALUES ('Holidays', 'Other', 4);

INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Monthly spending report', 'Sarah', 3, 'RZHX12');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Movie Night', 'Jimmy', 7, 'JSLA23');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Baking Showdown', 'Burt', 2, 'UWXM39');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Math tutoring session', 'Slappy', 1, 'MSJW98');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Charades', 'Ronald', 5, 'ZTKL43');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Book reviews', 'Tom', 4, 'RPBN42');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Project update overview','Harry', 6, 'KHJA32');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Keyboard building guide','Richard', 9, 'LMJA23');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Resume Building Workshop', 'Jessica', 8, 'HUWA39');
INSERT INTO Meetings(m_title, m_attendee, m_userid, m_link) VALUES ('Drawing and Painting', 'Britney', 10, 'MFIG25');

INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('1', 'Jack', 'Harlow', 'jharlow69@gmail.com', TRUE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('2', 'Travis', 'Scott', 'travvypatty420@yahoo.com', TRUE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('3', 'Drizzy', 'Drake', 'loverboy2000@gmail.com', TRUE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('4', '21', 'Savage', 'savage21@yahoo.com', FALSE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('5', 'Ye', 'West', 'kwest420@gmail.com', FALSE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('6', 'Lebron', 'James', 'lemickey3000@gmail.com', TRUE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('7', 'Barack', 'Obama', 'bobama420@gmail.com', FALSE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('8', 'George', 'Bush', 'gbush2008@yahoo.com', TRUE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('9', 'Dua', 'Lipa', 'dualipareal@gmail.com', FALSE);
INSERT INTO Users(u_id, u_firstname, u_lastname, u_email, u_isactive ) VALUES ('10', 'Andrew', 'Tate', 'andrewt420@gmail.com', FALSE);

INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Lunch With Bob', FALSE, TRUE, FALSE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Coffee With Bruce', FALSE, FALSE, TRUE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Meeting', FALSE, TRUE, TRUE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Basketball Game', FALSE, TRUE, TRUE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Baseball Game', FALSE, TRUE, TRUE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Exercise', FALSE, TRUE, FALSE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Walk', FALSE, FALSE, FALSE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Run', FALSE, FALSE, FALSE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Dinner', FALSE, FALSE, FALSE);
INSERT INTO Status(s_title, s_draft, s_open, s_ongoing) VALUES ('Lunch', FALSE, TRUE, FALSE);

--1 Print users that created events
SELECT DISTINCT u_firstname, u_lastname
FROM Users
INNER JOIN Events on Users.u_id = Events.e_userid
ORDER BY u_firstname;

--2 Print events that include live sports
SELECT e_title
FROM Events
WHERE e_description LIKE '%' ||'live'|| '%';

--3 Print users that created reminders 
SELECT DISTINCT u_firstname, u_lastname
FROM Users
INNER JOIN Reminders on Users.u_id = Reminders.r_userid
ORDER BY u_firstname DESC;

--4 Print all ongoing events that were created by Jack Harlow
SELECT s_title
FROM Status
INNER JOIN Events on Status.s_title = Events.e_title
WHERE s_ongoing = TRUE AND Events.e_userid = 1;

--5 Print all users that created events that belong to the "Personal" calendar group
SELECT DISTINCT u_firstname, u_lastname
FROM Users
INNER JOIN Events on Users.u_id = Events.e_userid
INNER JOIN Groups on Events.e_groupid = Groups.g_id
WHERE Events.e_groupid = 1
ORDER BY u_firstname;

--6 Print all reminders after 11-17-2022
SELECT r_title, strftime('%Y-%m-%d', Reminders.r_date) as "Date"
FROM Reminders
WHERE Date > strftime('%Y-%m-%d', '2022-11-17');

--7 Print all meetings created by users that created events 
SELECT DISTINCT m_title 
FROM Meetings
INNER JOIN Users on Meetings.m_userid = Users.u_id
INNER JOIN Events on Users.u_id = Events.e_userid
ORDER BY m_title; 

--8 Print all users that created High priority Reminders 
SELECT DISTINCT u_firstname, u_lastname
FROM Users
INNER JOIN Reminders on Reminders.r_userid = Users.u_id
WHERE Reminders.r_priority = 'High';

--9 Print all open events that belong to the "Personal" group calendar
SELECT e_title
FROM Events
INNER JOIN Groups on Groups.g_id = Events.e_groupid
INNER JOIN Status on Status.s_title = Events.e_title 
WHERE Status.s_open = TRUE AND Events.e_groupid = 1; 

--10 Print all recurring events created by users that created events in group 1 
SELECT Events.e_title, Users.u_firstname, Users.u_lastname
FROM Events 
INNER JOIN Users on Events.e_userid = Users.u_id
INNER JOIN Groups on Groups.g_id = Events.e_groupid
INNER JOIN Status on Status.s_title = Events.e_title
WHERE Status.s_ongoing = TRUE AND Events.e_groupid = 1;


-- #11 Find events where Travis attends and Poke is involved for lunch

SELECT e_title 
FROM 
Events
WHERE 
e_attendee = 'Travis' AND e_description LIKE '%'||'lunch'||'%' AND e_location = 'Poke';


-- #12 List all the meetings that involve 'building' in their title and sort by reverse alphabetical order
SELECT m_title
FROM Meetings
WHERE
m_title LIKE '%'||'building'||'%' 
ORDER BY m_title DESC;


-- #13 List all events created by people with the user ID 5 and involves Baseball. Print their full name at the end.
SELECT e_title, u_firstname, u_lastname
FROM
Users
INNER JOIN Events ON Users.u_id = Events.e_userid
WHERE
u_id = 5 AND e_title LIKE '%'||'Baseball'||'%';

-- #14 List all the active users that have a gmail account. Print and sort by their last names alphabetically.

SELECT u_id, u_lastname
FROM
Users
WHERE u_isactive = 1 AND u_email LIKE '%'||'gmail.com'||'%'
ORDER BY u_lastname ASC;

-- #15 Count how many events were created by people with user ID 4. 
SELECT COUNT(*)
FROM 
Events
INNER JOIN Users ON Events.e_userid = Users.u_id
WHERE u_id = 4;


--16 Print the user who created reminders after 11-15-2022
SELECT u_firstname, strftime('%Y-%m-%d', Reminders.r_date) as "Date"
FROM Reminders
INNER JOIN Users ON Reminders.r_userid = Users.u_id
WHERE Date > strftime('%Y-%m-%d', '2022-11-15');

--17 Print the event description with Group ID 1 where the events are open
SELECT e_description
FROM Events
INNER JOIN Groups ON Groups.g_id = Events.e_groupid
INNER JOIN Status ON Status.s_title = Events.e_title 
WHERE Status.s_open = TRUE AND Events.e_groupid = 1; 

--18 Find the user that created events that have group ID 1. Print their last name and order alphabetically.
SELECT DISTINCT u_lastname
FROM Users
INNER JOIN Events on Users.u_id = Events.e_userid
INNER JOIN Groups on Events.e_groupid = Groups.g_id
WHERE Events.e_groupid = 1
ORDER BY u_lastname ASC;

--19 Print the events that have descriptions that include the letter D. 
SELECT e_title
FROM Events
WHERE e_description LIKE '%'||'d'||'%';

--20 Find the last name of who created medium priority reminders that are recurring
SELECT DISTINCT u_lastname
FROM Users
INNER JOIN Reminders ON Reminders.r_userid = Users.u_id
WHERE Reminders.r_priority = 'Medium' AND Reminders.r_recurring = TRUE;
