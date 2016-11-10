#!/usr/bin/python
import commands
import MySQLdb
import os

path = "/home/pi/mazi/"

#Connect to data base local.mazizone.eu/phpmyadmin/
db  = MySQLdb.connect(host = "localhost",
                      user = "limesurvey",
                      passwd = "mazilime",
                      db = "mazi_survey")


cur = db.cursor()

cur.execute("SELECT * FROM lime_surveys_languagesettings")

#Take id from new active survey
for row in cur.fetchall():
    survey_id = str(row[0])

#Connect to new survey
cur.execute("SELECT * FROM lime_survey_" + survey_id)
#cur.execute("SELECT * FROM lime_survey_884936")

for row in cur.fetchall():
    #Receives the user IP address, if it has answer the survey 
    if str(row[8]) != "None":
          ip = str(row[7])
          #Run unblock_user.py for user with spesific IP
          os.system("sudo python '%s'unblock_user.py '%s'" % (path, ip))

db.close()


