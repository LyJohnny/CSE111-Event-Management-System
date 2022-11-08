CREATE TABLE IF NOT EXISTS Events (
    e_location VARCHAR(255) NOT NULL,
    e_attendees VARCHAR(255) NOT NULL,
    e_creator VARCHAR(255) NOT NULL,
    e_title VARCHAR(255) NOT NULL,
    e_description VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Reminders (
    r_recurring BOOLEAN NOT NULL,
    r_priority VARCHAR(255) NOT NULL,
    r_title VARCHAR(255) NOT NULL,
    e_description VARCHAR(255) NOT NULL,
    e_date datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS Status (
    s_draft VARCHAR(255) NOT NULL,
    s_open BOOLEAN NOT NULL,
    s_closed BOOLEAN NOT NULL,
    s_ongoing BOOLEAN NOT NULL,
    s_past BOOLEAN NOT NULL,
    s_cancelled BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS Groups (
    g_title VARCHAR(255) NOT NULL,
    g_type VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Meetings (
    m_attendee VARCHAR(255) NOT NULL,
    m_title VARCHAR(255) NOT NULL,
    m_description VARCHAR(255) NOT NULL,
    m_location VARCHAR(255) NOT NULL,
    m_creator VARCHAR(255) NOT NULL,
    m_link VARCHAR(255) NOT NULL
); 

CREATE TABLE IF NOT EXISTS User (
    u_firstname VARCHAR(255) NOT NULL,
    u_lastname VARCHAR(255) NOT NULL,
    u_email VARCHAR(255) NOT NULL,
    u_bio VARCHAR(255) NOT NULL,
    u_isactive BOOLEAN NOT NULL
);
