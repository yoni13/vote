import time,os
from flask import Flask, render_template,request, redirect
import pymongo


win10 = 0
mt = False
android = 0
phnum = 0
linuxnum = 0
iphonenum = 0
testpass = 123
w =0
str = 'Mozilla/5.0 (Linux; Android'
iphonestr = 'Mozilla/5.0 (iPhone'
linuxstr ='Mozilla/5.0 (Linux'
linuxstr2 = 'Mozilla/5.0 (X11'
app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
) 


@app.route("/favicon.ico")
def favicon():
  return redirect("https://media.discordapp.net/attachments/858972718611562496/900698598612803584/A.png")


app.run(host='0.0.0.0', port=8080,debug = True)