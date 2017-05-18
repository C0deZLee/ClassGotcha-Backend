# ClassGotcha API Documentation 
### Version 1.0

## Account

### Login

Authenticate the user with the system and obtain the auth_token

### Request


| Method | URL |
| --- | --- |
| POST | account/login/ |

| Type | Params | Values | Required|
| --- | --- | --- | --- |
| Body | username | string | True|
| Body | password | string | True|

### Response 

| Status | Response |
| --- | --- |
| 200 | {'token': <auth_token>}|
| 400 | {"error":"Username is required."} |
| 400 | {"error":"Password is required"} |
| 401 | {"error":"Incorrect username or password."} |

---

### Register
