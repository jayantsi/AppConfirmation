from flask import Flask
from flask import Response
from flask import render_template
from flask import request

import sqlite3
import json
import collections

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def demo():
    if request.method=='POST':
        Appointment_date = request.form['Appointment_date']
	Description = request.form['Description']
        return render_template('index.html', name=name)
    else:
        return render_template('index.html')


@app.route('/appointments', methods=['GET'])
def getAppointments():
	with sqlite3.connect('test.db') as conn:
		cursor = conn.cursor();
		search = request.args.get('search');
		cursor.execute("SELECT * FROM APPOINTMENTS WHERE DESCRIPTION LIKE '%"+search+"%'")
		data = cursor.fetchall()
		#return json.dumps(data)
		objects_list = []
		for row in data:
		    d = collections.OrderedDict()
		    #d['id'] = row.id
		    d['Appointment_date'] = row[1]
		    d['Description'] = row[2]
		    
		    objects_list.append(d)
		 
		j = json.dumps(objects_list);
		return Response(j, mimetype='application/json')
		#return j

@app.route('/appointments', methods=['POST'])
def saveAppointments():
	conn = sqlite3.connect('test.db')
	c = conn.cursor();
	data = request.json;
	row = (data.get('Appointment_date'),data.get('Description'))
  	c.execute('insert into APPOINTMENTS(Appointment_date,Description) values (?,?)', row);
	conn.commit();
	c2 = conn.cursor();
	c2.execute("SELECT * FROM APPOINTMENTS")
		
	rows = c2.fetchall();
	objects_list = []
	for row in rows:
	    d = collections.OrderedDict()
	    #d['id'] = row.id
	    d['Appointment_date'] = row[1]
	    d['Description'] = row[2]
	    
	    objects_list.append(d)
	 
	j = json.dumps(objects_list)
	return (j)
	
        

if __name__ == '__main__':
    app.run()
