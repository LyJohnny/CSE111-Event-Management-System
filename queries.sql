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
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Meeting', 'Collaboration', 'Coffee Shop', 'Heather', 5, 3);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Basketball Game', 'live', 'Home', ' ', 6, 5);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Baseball Game', 'live', 'Home', '', 6, 5);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Exercise', 'daily workout', 'Gym', ' ', 8, 6);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Walk', 'daily walk', 'Mount Fuji', ' ', 8, 6);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Run', 'daily run', 'Downtown', ' ', 4, 2);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Dinner', 'dinner with friend', 'Cheesecake Factory', 'Jack', 5, 4);
INSERT INTO Events(e_title, e_description, e_location, e_attendee, e_groupid, e_userid) VALUES ('Lunch', 'lunch with coworker', 'Poke', 'Travis', 5, 4);


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
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (1, 'Final Test', 'MATH-141', FALSE, 'High', '2022-12-17 15:00');
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
