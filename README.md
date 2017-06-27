# STI Redfish
RESTful Redfish/RackHD API rewrite with Flask.
Written in Python & Flask.

### Prerequisites
Required tools: curl

## Getting authentication token

Location: http://locahost:5000/rackhd/login

Method: POST

Flask credentials (username, password): admin, flask

Body (username, password): admin, admin123

Example command:
```
curl -X POST -H "Content-Type: application/json"  http://localhost:5000/rackhd/login -u admin:flask -d '{"username":"admin","password":"admin123"}'
```

## OBMS Management

### Create

Location: http://locahost:5000/rackhd/obms/create

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: PUT

Flask credentials (username, password): admin, flask

Body (nodeId, service, username, password, host): node1, ipmi-obm-service, user1, password123, 192.171.5.1

Example command:
```
curl -X PUT -H "Content-Type: application/json"  http://localhost:5000/rackhd/obms/create -u admin:flask -d '{'{"nodeId":"node1", "service":"ipmi-obm-service", "username":"user1", "password":"password123", "host":"192.171.5.1"}'}' -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```

### Read

Location: http://locahost:5000/rackhd/obms/read

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: GET

Flask credentials (username, password): admin, flask

Example command:
```
curl -X GET -H "Content-Type: application/json"  http://localhost:5000/rackhd/obms/read -u admin:flask -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```

### Update

Location: http://locahost:5000/rackhd/obms/update

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: PATCH

Flask credentials (username, password): admin, flask

Body (nodeId, service, username, password, host): 59415a8bb77ff267c0a9c68d7, ipmi-obm-service, user2, password1234, 192.171.5.2

Example command:
```
curl -X PATCH -H "Content-Type: application/json"  http://localhost:5000/rackhd/obms/update -u admin:flask -d '{"nodeId":"59415a8bb77ff267c0a9c68d7", "service":"ipmi-obm-service", "username":"user2", "password":"password1234", "host":"192.171.5.2"}' -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```

### Delete

Location: http://locahost:5000/rackhd/obms/create

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: DELETE

Flask credentials (username, password): admin, flask

Body (nodeId): 59415a8bb77ff267c0a9c68d7

Example command:
```
curl -X DELETE -H "Content-Type: application/json"  http://localhost:5000/rackhd/obms/delete -u admin:flask -d '{"nodeId":"59415a8bb77ff267c0a9c68d7"}' -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```

## Role Management

### Create

Location: http://locahost:5000/rackhd/role/create

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: POST

Flask credentials (username, password): admin, flask

Body (privileges, role): [Read, Write], ReadWrite

Example command:
```
curl -X POST -H "Content-Type: application/json"  http://localhost:5000/rackhd/role/delete -u admin:flask -d '{"privileges":["Read", "Write"], "role":"ReadWrite"}' -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```

### Read

Location: http://locahost:5000/rackhd/role/read

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: GET

Flask credentials (username, password): admin, flask

Example command:
```
curl -X GET -H "Content-Type: application/json"  http://localhost:5000/rackhd/role/read -u admin:flask -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```

### Update

Location: http://locahost:5000/rackhd/role/update

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: UPDATE

Flask credentials (username, password): admin, flask

Example command:
```
curl -X UPDATE -H "Content-Type: application/json"  http://localhost:5000/rackhd/role/update -u admin:flask -d '{"privileges":["Read"], "role":"ReadWrite"}' -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```

### Delete

Location: http://locahost:5000/rackhd/role/delete

Authorization Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE

Method: DELETE

Flask credentials (username, password): admin, flask

Example command:
```
curl -X DELETE -H "Content-Type: application/json"  http://localhost:5000/rackhd/role/delete -u admin:flask -d '{"role":"ReadWrite"}' -H "Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0NTU2MTI5MzMsImV4cCI6MTQ1NTY5OTMzM30.glW-IvWYDBCfDZ6cS_6APoty22PE_Ir5L1mO-YqO3eE"
```
