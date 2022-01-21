import random,sys,time
from replit import db
from flask import Flask, Response, send_from_directory,render_template,request, redirect,make_response
from werkzeug.useragents import UserAgent
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

'''
,n1 = db['1'],n2 = db['2'],n3 = db['3'],n4 = db['4'],n5 = db['5'],n6= db['6'],n7 = db['7'],n8 = db['8'],n9 = db['9'],n10 = db['10'],n11 = db['11'],n12 = db['12'],n13 = db['13'],n14 = 
                         db['14'],n15 = db['15'],n16 = db['16'],n17 = db['17'],n18 = db['18'],n19 = db['19'],n20 = db['20'],n21 = db['21']
x = 43
y = 1
for times in range(43):
  db[y] = 0
  y += 1
'''
@app.route('/t')
def t():
  return render_template('tt.html')
@app.route('/voteg',methods=['POST','GET'])
def vote():
  global all
  if request.method =='POST':
    if 'votedgirls' in request.cookies:
     return redirect('/voted')
    else:
     str = request.headers.get('user-agent')
     a= request.values['number']
     db[a]+=1
     w = open('file1.txt','a')
     w.write(str)
     w.write('\n')
     w.write(a)
     w.write('\n')   
     return redirect('/set')
  if 'votedgirls' in request.cookies:
     return redirect('/voted')
  else:
     return render_template('17.html')
  return render_template('17.html')
  
  
@app.route("/set")
def setcookie():
    resp =  redirect('/voted')
    resp.set_cookie(key='votedgirls', value='just vote', expires=time.time()+17280900)
    return resp
@app.route('/voted')
def denied ():
  return render_template('vg.html' ,n22 = db['22'],n23 = db['23'],n24 = db['24'],n25 = db['25'],n26 = db['26'],n27= db['27'],n28 = db['28'],n29 = db['29'],n30 = db['30'],n31 = db['31'],n32 = db['32'],n33 = db['33'],n34 = db['34'],n35 = 
                         db['35'],n36 = db['36'],n37 = db['37'],n38 = db['38'],n39 = db['39'],n40 = db['40'],n41 = db['41'],n42 = db['42'])
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
@app.errorhandler(500)
def Server_Error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500

  

  
@app.route('/stat')
def stat():
  global all
  win10num = win10
  agent = request.headers.get('User-Agent')
  return  render_template("stat.html",win10num=win10num,android = android,agent = agent,linuxnum = linuxnum,iphonenum = iphonenum)
  
@app.route('/',methods=['POST','GET'])
def mttest():
  global all
  if request.method =='POST':
    
    a= request.values['user']
    return render_template('1.html',a =a)
  return render_template('1.html')
  

@app.route("/favicon.ico")
def favicon():
  return redirect("https://media.discordapp.net/attachments/858972718611562496/900698598612803584/A.png")


app.run(host='0.0.0.0', port=8080,debug = True)