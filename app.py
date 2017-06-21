#!flask/bin/python

from flask import Flask, jsonify, request, abort, make_response, url_for
from flask_httpauth import HTTPBasicAuth

import requests, json

auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def get_password(username):
	if username == 'admin':
		return 'flask'
	return None

@auth.error_handler
def unauthorizaed():
	return make_response(jsonify({'error': 'Flask unauthorized access'}), 401)

@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error':'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not found'}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
	return make_response(jsonify({'error':'Method not allowed'}), 405)

@app.route('/rackhd/login', methods=['POST'])
@auth.login_required
def rackhd_login():
	if not request.json or not 'username' in request.json:
		abort(400)

	username = request.json['username']
	password = request.json['password']


	url = "https://localhost:8443/login"

	headers = {
		"Content-Type": "application/json"
	}

	payload = '{"username": "' + username + '", "password": "' + password + '"}'

	response = requests.post(url, headers=headers, data=payload, verify=False)

	return response.text

@app.route('/rackhd/obms/create', methods=['PUT'])
@auth.login_required
def create_obms():
	url = "https://localhost:8443/api/current/obms"

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	nodeId = request.json['nodeId']
	service = request.json['service']
	user = request.json['user']
	password = request.json['password']
	host = request.json['host']

	payload = '{"nodeId": "' + nodeId + '", "service":"' + service + '", "config":{"user":"' + user + '", "password":"' + password + '", "host":"' + host + '"}}'

	response = requests.put(url, headers=headers, data=payload, verify=False)

	return response.text

@app.route('/rackhd/obms/read', methods=['GET'])
@auth.login_required
def read_obms():
	url = "https://localhost:8443/api/current/obms"

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.get(url, headers=headers, verify=False)

	return response.text

@app.route('/rackhd/obms/read/<string:nodeId>', methods=['GET'])
@auth.login_required
def read_obms_by_id(nodeId):
	base_url = "https://localhost:8443/api/current/obms"

	url = base_url + "/" + nodeId

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.get(url, headers=headers, verify=False)

	return response.text

@app.route('/rackhd/obms/update', methods=['PATCH'])
@auth.login_required
def update_obms():
	base_url = "https://localhost:8443/api/current/obms"

	nodeId = request.json['nodeId']

	url = base_url + "/" + nodeId

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	service = request.json['service']
	user = request.json['user']
	password = request.json['password']
	host = request.json['host']

	payload = '{"nodeId":"' + nodeId +'", "service":"' + service + '", "config":{"user":"' + user +'", "password":"' + password + '", "host":"' + host + '"}}'

	response = requests.patch(url, headers=headers, data=payload, verify=False)

	return response.text

@app.route('/rackhd/obms/delete', methods=['DELETE'])
@auth.login_required
def delete_obms():
	base_url = "https://localhost:8443/api/current/obms"

	nodeId = request.json['nodeId']

	url = base_url + "/" + nodeId

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.delete(url, headers=headers, verify=False)

	return response.text

@app.route('/rackhd/role/create', methods=['POST'])
@auth.login_required
def create_role():
	url = "https://localhost:8443/api/current/roles"

	token = "JWT " + request.headers.get('Token')

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
@auth.login_required
def read_role():

	url = "https://localhost:8443/api/current/roles"

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.get(url, headers=headers, verify=False)
	return response.text

@app.route('/rackhd/role/read/<string role>', methods=['GET'])
@auth.login_required
def read_role_by_role():

	base_url = "https://localhost:8443/api/current/roles"

	role = request.json['role']

	url = base_url + "/" + role

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.get(url, headers=headers, verify=False)
	return response.text

@app.route('/rackhd/role/update', methods=['PATCH'])
@auth.login_required
def update_role():

	base_url = "https://localhost:8443/api/current/roles"

	role = request.json['role']

	url = base_url + "/" + role

	token = "JWT " + request.headers.get('Token')

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
@auth.login_required
def delete_role():

	base_url = "https://localhost:8443/api/current/roles"

	role = request.json['role']

	url = base_url + "/" + role

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.delete(url, headers=headers, verify=False)

	return response.text

@app.route('/rackhd/account/create', methods=['POST'])
@auth.login_required
def create_account():

	base_url = "https://localhost:8443/api/current/users?auth_token="

	token = request.headers.get['Token']

	url = base_url + token

	username = request.json['username']
	password = request.json['password']
	role = request.json['role']

	payload = '{"username":"' + username + '", "password":"' + password +'", "role":"' + role + '"}'

	headers = {
		"Content-Type": "application/json"
	}

	response = requests.post(url, headers=headers, data=payload, verify=False)
	return response.text

if __name__ == '__main__':
	app.run(debug=True)
