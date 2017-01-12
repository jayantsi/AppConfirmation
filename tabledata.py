#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute("INSERT INTO APPOINTMENTS (ID,Appointment_date,Description) \
      VALUES (1, '2017-01-08', 'California')");

conn.execute("INSERT INTO APPOINTMENTS (ID,Appointment_date,Description) \
      VALUES (2, '2017-01-03','Texas')");

conn.execute("INSERT INTO APPOINTMENTS (ID,Appointment_date,Description) \
      VALUES (3, '2010-01-25', 'Norway')");

conn.execute("INSERT INTO APPOINTMENTS (ID,Appointment_date,Description) \
      VALUES (4, '2020-01-07', 'Rich-Mond')");

print "Table created successfully";

conn.close()



