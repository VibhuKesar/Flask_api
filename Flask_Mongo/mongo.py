from flask import Flask, request, jsonify
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'framework'
app.config['MONGO_URI'] = 'mongodb://<dbuser>:<dbpassword>@ds113795.mlab.com:13795/framework'

mongo = PyMongo(app) #initialize db


#find and get data from the db
@app.route('/framework_main', methods=['GET'])
def get_all():
	framework_main = mongo.db.framework_main

	output = []

	for q in framework_main.find():	#find all docs from the db
		output.append({'name' : q['name'],'language' : q['language']})

	return jsonify({'result': output})


#get a specific one and find whether u typed existed one or not
@app.route('/framework_main/<name>', methods=['GET'])
def get_one():
	framework_main = mongo.db.framework_main
	q = framework_main.find_one({'name' : name}) 	

	if q:
		output = {'name' : q['name'], 'language' : q['language']}
	else
		output = 'No result'

	return jsonify({'result' : output})


#Post--> insert the data not manipulate
@app.route('/framework_main', methods=['POST'])
def add():
	framework_main = mongo.db.framework_main

	name = request.json['name']
	language = request.json['language']

	f_id = framework_main.insert({'name': name, 'langauge':language})
	new_f = framework_main.find_one({'_id' : f_id})

	output = {'name' : new_f['name'], 'language' : new_f['language']}

	return jsonify({'result' : output})

#delete not created cz mongo web. support it 
if __name__ == '__main__':
	app.run(debug=True)