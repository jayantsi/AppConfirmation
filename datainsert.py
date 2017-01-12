#!/usr/bin/python

import sqlite3




conn.execute('''CREATE TABLE APPOINTMENTS
       (ID integer primary key,
	Appointment_date         DATE    NOT NULL,
        Description        CHAR(100));''')
print "Table created successfully";

conn.commit()
print "Records created successfully";
conn.close()
