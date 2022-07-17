import time,os
from flask import Flask, render_template,request, redirect,make_response
import pymongo



client = pymongo.MongoClient(os.environ['MONGO_URL'])
votedb = client['vote']
votedata = votedb['votedata']
#test db
#votedata.insert_one({'name':'test','votes':0})

str = 'Mozilla/5.0 (Linux; Android'
iphonestr = 'Mozilla/5.0 (iPhone'
linuxstr ='Mozilla/5.0 (Linux'
linuxstr2 = 'Mozilla/5.0 (X11'
app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
@app.route('/vote', methods=['GET','POST'])
def vote():
	if request.method == 'GET':
		if request.args.get('id') == None:
			return redirect('/')
		else:
			id = request.args.get('id')
			if votedata.find_one({'id':id}) == None:
				return redirect('/')
			return render_template('vote.html')

@app.route('/')
def index():
	resp = make_response(render_template('index.html'))
	resp.headers['Refresh'] = '6; url=https://www.youtube.com/watch?v=dQw4w9WgXcQ'
	return resp

@app.route("/favicon.ico")
def favicon():
  return redirect("https://media.discordapp.net/attachments/858972718611562496/900698598612803584/A.png")

if __name__ == '__main__':
  app.run(debug=True)