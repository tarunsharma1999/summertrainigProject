#!/usr/bin/python3
import cgi
import cgitb

cgitb.enable()
print("Content-type:text")
print("")


webdata = cgi.FieldStorage()

mymood = webdata.getvalue('User_Id')

print(mymood)