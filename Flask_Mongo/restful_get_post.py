from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name' : 'Javascript'}, {'name' : 'Python'}]

#get --> recieve everything 
@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'it works'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages':languages}) #key : value inside a new dictionary

@app.route('/lang/<string:name1>', methods=['GET'])
def returnOne(name1):
	langs = [languages for languages in languages if languages['name'] == name1]
	return jsonify({'languages' : langs[0]})

#while using postman don't forget to change default text to app/json
#post --> add
@app.route('/lang', methods= ['POST'])
def addOne():
	language = {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages})

#put --> to manipulate the name or data
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [languages for languages in languages if languages['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'language': langs[0]})

#delete --> delete a value or data
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	lang = [languages for languages in languages if languages['name'] == name]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__' :
	app.run(debug=True)
