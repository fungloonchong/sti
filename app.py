#!flask/bin/python

from flask import Flask, jsonify, request, abort

import requests, json

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


	url = "https://localhost:8443/login"

	headers = {
		"Content-Type": "application/json"
	}

	payload = '{"username" : "' + username + '", "password": "' + password + '"}'

        response = requests.post(url, headers=headers, data=payload, verify=False)
	return response.text

@app.route('/rackhd/role/create', methods=['POST'])

def create_role():
	url = "https://localhost:8443/api/current/roles"

	token = "JWT " + request.headers.get('Authorization')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	privileges = request.json['privileges']

	privileges2 = list()

	for permission in privileges:
		privileges2.append(str(permission))

	privileges2 = str(privileges2)
	privileges2 = privileges2.replace("'",'"')

	role = request.json['role']

	payload = '{"privileges": ' + privileges2 + ', "role": "' + role + '"}'
	response = requests.post(url, headers=headers, data=payload, verify=False)

	return response.text

@app.route('/rackhd/role/read', methods=['GET'])

def read_role():

	url = "https://localhost:8443/api/current/roles"

	token = "JWT " + request.headers.get('Authorization')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.get(url, headers=headers, verify=False)
	return response.text

@app.route('/rackhd/role/update', methods=['PATCH'])

def update_role():

	base_url = "https://localhost:8443/api/current/roles"

	role = request.json['role']

	url = base_url + "/" + role

	token = "JWT " + request.headers.get('Authorization')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	privileges = request.json['privileges']

	privileges2 = list()

	for permission in privileges:
		privileges2.append(str(permission))

	privileges2 = str(privileges2)
	privileges2 = privileges2.replace("'",'"')

	payload = '{"privileges": ' + privileges2 + '}'
	response = requests.patch(url, headers=headers, data=payload, verify=False)

	return response.text

@app.route('/rackhd/role/delete', methods=['DELETE'])

def delete_role():

	base_url = "https://localhost:8443/api/current/roles"

	role = request.json['role']

	url = base_url + "/" + role

	token = "JWT " + request.headers.get('Authorization')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.delete(url, headers=headers, verify=False)

	return response.text

if __name__ == '__main__':
	app.run(debug=True)
