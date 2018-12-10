import csv
import mysql.connector
import os

print ("In")

#CONNECTION DATABASE
mydb = mysql.connector.connect(host='localhost', user='root', passwd='<< >>', db='banking')
cursor = mydb.cursor()

#cursor.execute ('DELETE FROM banking.requests')
#cursor.execute ('DELETE FROM banking.emails')

with open(r'C:\Users\BFSVMADMIN\Desktop\BFS_Hackathon\To_Predict\Cons_Pred_Output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for rows in csv_reader:
        cursor.execute('INSERT INTO banking.emails(id,textmessage,category ) VALUES(%s,"%s", "%s")',rows)
    mydb.commit()
	#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")

os.system('python C:/Python37/Project/Project/app/services/Main.py')
