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
    s_ongoing BOOLEAN NOT NULL,
    s_cancelled BOOLEAN NOT NULL
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

INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (1, 'Midterm 1', 'MATH-141', FALSE, 'High', '2022-11-17 13:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (1, 'Final Test', 'MATH-141', FALSE, 'High', '2022-12-17 15:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (3, 'Code Review', 'Team code review', TRUE, 'Medium', '2022-11-15 10:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (5, 'Product Launch', 'Watch Party', FALSE, 'High', '2022-11-26 09:00');
INSERT INTO Reminders(r_userid, r_title, r_description,  r_recurring,  r_priority, r_date) VALUES (4, 'Meeting', 'Team meeting', TRUE, 'High', '2022-12-05 11:00');
