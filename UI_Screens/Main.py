#import request
import sys
import os
import mysql.connector
import webbrowser

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) #create the Flask app

#CONNECTION DATABASE
mydb = mysql.connector.connect(host='<< >>', user='<< >>', passwd='<< >>', db='<< >>')
cursor = mydb.cursor()

@app.route('/')
def emails(): 
		cursor.execute('select id,textmessage,category from emails')
		data = cursor.fetchall()
		mydb.commit()
		return render_template("Dashboard.html", data=data)
		return data
		
@app.route('/Request', methods=['POST','GET'])
def Request():
	if request.method == 'POST':
		cursor.callproc('ServiceRequestsPopulate')
		cursor.execute('select SRID,textmessage,assignedto,date,status from Requests')
		request_data = cursor.fetchall()
		mydb.commit()
		return render_template("Request.html", request_data=request_data)
		return request_data 
	else:
		return render_template("NotFound.html")
	
webbrowser.open("http://127.0.0.1:5000/");
if __name__ == '__main__':
    app.run()
