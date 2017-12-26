#!/usr/bin/python3

# Turn on debug mode. Basically what this does is outputs problems with python
# to the browser
import cgitb
cgitb.enable()
# to output problems to a logfile instead, comment out the above line and
# uncomment the line below
# cgitb.enable(display=0, logdir="/path/to/logdir")

# Print necessary headers.
print("Content-Type: text/html")
print()
print("<h1>index.py works!</h1>")

import mysql.connector

cnx = mysql.connector.connect(option_files='/var/webconfig/mission-tracker.cnf')
cursor = cnx.cursor()
query = ("SELECT * FROM wards")
cursor.execute(query)

print("ward_id stake_id name", end="<br>")
for (primary_key, stake_key, name) in cursor:
  print(primary_key, stake_key, name,
          sep="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
          end="<br>")

cursor.close()
cnx.close()


