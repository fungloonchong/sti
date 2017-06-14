#!flask/bin/python

from flask import Flask, jsonify, request, abort

import requests

#from flask_httpauth import HTTPBasicAuth

#auth = HTTPBasicAuth()

#@auth.get_password
#def get_password(username):
#	if username == 'admin':
#		return 'flask'
#	return None

#@auth.error_handler
#def unauthorizaed():
#	return make_response(jsonify({'error': 'Flask unauthorized access'}), 401)

app = Flask(__name__)

@app.route('/rackhd/login', methods=['POST'])
#@auth.login_required
def rackhd_login():
	if not request.json or not 'username' in request.json:
		abort(400)

	username = request.json['username']
	password = request.json['password']
	#role = request.json['role']


	url = "https://localhost:8443/login"

	headers = {
		"Content-Type": "application/json"
	}

	payload = '{"username" : "' + username + '", "password": "' + password + '"}'

	#return payload
        response = requests.post(url, headers=headers, data=payload, verify=False)
        #print(response.text)
	return response.text

@app.route('/rackhd/role/read', methods=['GET'])

def read_role():
	#if not request.headers.get or not 'token' in request.headers.get:
	#	abort(400)

	url = "https://localhost:8443/api/current/roles"

	token = "JWT " + request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.get(url, headers=headers, verify=False)
	return response.text

if __name__ == '__main__':
	app.run(debug=True)
