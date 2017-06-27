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
