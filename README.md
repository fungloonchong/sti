OBMS
GET /api/current/obms
curl https://localhost:8443/api/current/obms \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X GET

GET /api/current/obms/<nodeId>
curl https://localhost:8443/api/current/obms/<nodeId> \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X GET

PUT /api/current/obms
curl https://localhost:8443/api/current/obms \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X PUT
-d '{ "nodeId": <node id>, "service": "ipmi-obm-service", "config": { "user": "admin", "password": "admin", "host": "<host ip>" } }'

PATCH /api/current/obms/<nodeId>
curl https://localhost:8443/api/current/obms/<nodeId> \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X PATCH
-d '{ "nodeId": <node id>, "service": "ipmi-obm-service", "config": { "user": "admin", "password": "admin", "host": "<host ip>" } }'

DELETE /api/current/obms/<nodeId>
curl https://localhost:8443/api/current/obms/<nodeId> \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X DELETE

Role
GET /api/current/roles
curl https://localhost:8443/api/current/roles \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X GET

GET /api/current/roles/<role>
curl https://localhost:8443/api/current/roles/<role> \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X GET

POST /api/current/roles
curl https://localhost:8443/api/current/roles \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X POST
-d '{"privileges":["<privilege1>","<privilege2>"], "role": "<role>"}'

PATCH /api/current/roles
curl https://localhost:8443/api/current/roles/<role> \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X PATCH
-d '{"privileges":["<privilege1>","<privilege2>"]}'

DELETE /api/current/roles/<role>
curl https://localhost:8443/api/current/roles/<role> \
-k \
-H "Content-Type:application/json" \
-H "Authorization: JWT <token>" \
-X DELETE
