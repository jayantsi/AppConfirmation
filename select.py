#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, Appointment_date, Description  from APPOINTMENTS")
for row in cursor:
   print "ID = ", row[0]
   print "Appointment_date = ", row[1]
   print "Description = ", row[2], "\n"

print "Operation done successfully";
conn.close() 


