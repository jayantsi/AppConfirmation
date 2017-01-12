
# Appointments and Confirmations (dynamic web application)

The source code and required files are stored in the zip file. 

This application allows user to take an appointment on the desired date and save it. All the appointments once entered are stored in the database. Users can view all the exisitng appointments and they can even search particular appointment in the search field. 

Executed in the local host: http://127.0.0.1:5000/ 

##Files included:

main.py (main python script that has imported required libraries and has main modules to get and save appointments)

-templates 
	- index.html (Contains the front-end html file and Jquery scripts in it)

createdb.py
	- created and connected to database "test.db".

datainsert.py 
	- inserted data values to check if the database was running fine.

tabledata.py
	- created table "appointments" in the test.db by assigning column names and their datatypes.


* For this application to run: you need to install flask, sqllite3 in the VMware(ubuntu - Linux). 

1. First check if the database is created.select 
2. Check the table schema and the data values inserted in it. 
3. Then Check if the front-end is properly connected to database; and they are connected to the server. 
4. Run the file in localhost:5000/ 

## Links & Resources:

During the development of this web application, I have debugged my code by going through,

1. stackoverflow.com 
2. Google developers group
3. dba.stackexchange.com
4. Debugger tool 
5. RESTClient (downloaded the restful client web service to validate the posted data)

To check the values in the table in database: 
commands:
  > sqlite3 test.db
  > select * from appointments;
To run the application: 
  > python main.py (then open the localhost server) 

# SCreenshots are attached with the file.

* It is a successfully tested, debugged and executed application. It can be further improved by providing new features to the application.

#Thank you--


