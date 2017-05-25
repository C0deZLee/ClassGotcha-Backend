# ClassGotcha API Documentation 
### Version 1.0

## Account
### Register

user registration

#### Request

| Method | URL |
| --- | --- |
| POST | account/register/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Body | first_name | string | True |
| Body | last_name | string | True |
| Body | username | string | True |
| Body | password | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | {'token': <auth_token>} |

---

### Friends

user friend related functions

### Request

| Method | URL |
| --- | --- |
| GET | account/friends/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

### Response

| Status | Response | Value
| --- | --- | --- |
| 200 | [] | id
//need checking

### Request

| Method | URL |
| --- | --- |
| POST | account/friends/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | id | integer | True |

### Response

| Status | Response |
| --- | --- |
| 403 | 'detail': 'cant add yourself as your friend' | 
| 403 | 'detail': 'Already friended' | 
| 403 | 'detail': 'Already sent the request' | 
| 200 | none | 

### Request

| Method | URL |
| --- | --- |
| PUT | account/friends/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | id | integer | True |

### Response

| Status | Response |
| --- | --- |
| 200 | none |
| 403 | 'detail': 'cant add yourself as your friend' |
| 403 | 'detail': 'No friend request found' |

### Request

| Method | URL |
| --- | --- |
| DELETE | account/friends/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | id | integer | True |

### Response

| Status | Response |
| --- | --- |
| 200 | none |

---

### Moments

show user moment

### Request

| Method | URL |
| --- | --- |
| GET | account/moments/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value
| --- | --- | --- |
| 200 | [] | [{"id", <br> "comments",<br> "creator" <br>{<br> "pk", <br> "id", <br> "avatar", <br>"username", <br>"email", <br>"full_name", <br>"about_me", <br>"level" <br>}, <br>"likes", <br>"content", <br>"images", <br>"deleted", <br>"solved", <br>"permission", <br>"created", <br>"updated", <br>"classroom", <br>"flagged_users", <br>"liked_users"}, ... ] |

### Request

| Method | URL |
| --- | --- |
| POST | account/moments/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | cotent | string | true |
| Body | question | string | true |
| Body | classroom_id | int | false |
| Body | file | file | true |
//check file

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 400 | none |
| 400 | 'invalid image!' |

### Request

| Method | URL |
| --- | --- |
| PUT | account/moments/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | pk | integer | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |

### Request

| Method | URL |
| --- | --- |
| DELETE | account/moments/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | pk | integer | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |

---

### Classrooms

manage classrooms

### Request

| Method | URL |
| --- | --- |
| GET | account/classrooms/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | [] | [ {'id', <br> 'class_code', <br> 'class_short', <br> 'students_count', <br> 'class_section', <br> 'description', <br> 'class_time', <br> 'semester', <br> 'professors', <br> 'folders'} , ...] |

### Request

| Method | URL |
| --- | --- |
| POST | account/classrooms/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | pk | integer | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |

### Request

| Method | URL |
| --- | --- |
| DELETE | account/classrooms/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | pk | integer | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |

---

### Chatrooms

to manage chatroom

//included in the URL but not found in view

---

### pk (integer)

to view the user page

### Request

| Method | URL |
| --- | --- |
| GET | account/(integer)/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

### Response

| Status | Response | Value
| --- | --- | --- |
| 200 | "id" | int |
|     | "classrooms" | [] |
|     | "is_professor": | boolean |
|     | "full_name": | string |
|     | "chatrooms": | [] |
|     | "tasks": | [] |
|     | "last_login": | null |
|     | "email": | string |
|     | "username": | string |
|     | "created": | Date |
|     | "updated": | Date |
|     | "first_name": | string |
|     | "mid_name": | string |
|     | "last_name": | string |
|     | "gender": | string |
|     | "birthday": | Date |
|     | "school_year": | int |
|     | "about_me": | "Yo!" |
|     | "level": | int |
|     | "phone": | int |
|     | "professor": | null |
|     | "avatar": | null |
|     | "major": | int |
|     | "friends": | [] |
|     | "pending_friends": | [] |
|     | "notifications": | []|
| 404 | "detail": "Not found." |

---

### Avatar

the avatar for user

### Request

| Method | URL |
| --- | --- |
| POST | account/avatar/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | file | file | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | {'data': 'success'} |
| 400 | none |

### Request

| Method | URL |
| --- | --- |
| GET | account/avatar/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | {} | "avatar" |

---

### Pending-friends

show pending friend request

### Request

| Method | URL |
| --- | --- |
| GET | account/avatar/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | [] | [{'pk', <br>'id', <br>'avatar', <br>'username', <br>'email', <br>'full_name', <br>'about_me', <br>'level'}, ... ] |

### Login

Authenticate the user with the system and obtain the auth_token

#### Request

| Method | URL |
| --- | --- |
| POST | account/login/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Body | username | string | True |
| Body | password | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | {'token': <auth_token>} |
| 400 | {"error":"Username is required."} |
| 400 | {"error":"Password is required"} |
| 401 | {"error":"Incorrect username or password."} |

---

### Login-Refresh

refresh the token

#### Request

| Method | URL |
| --- | --- |
| POST | account/login-refresh/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Body | token | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | {'token': <auth_token>} |
| 400 | "This field may not be blank." |
| 400 | "This field is required"} |
| 400 | "non_field_errors": ["Error decoding signature."] |
//need checking, not found in view

---

### Login-Verify

verify the token

#### Request

| Method | URL |
| --- | --- |
| POST | account/login-verify/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Body | token | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | {'token': <auth_token>} |
| 400 | "This field may not be blank." |
| 400 | "This field is required"} |
| 400 | "non_field_errors": ["Error decoding signature."] |
//need checking, not found in view

---
### Verify

verify the email

#### Request

| Method | URL |
| --- | --- |
| GET | account/verify/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Body | email | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 201 | 'message': 'The verification email has been resent. ' |
| 400 | 'message': 'This email has been verified' |

#### Request

| Method | URL |
| --- | --- |
| POST | account/verify/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Body | token | string | True |
//need checking

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 400 | none |
| 400 | 'message': 'Token is expired' |

---

### Change Password

User change password

#### Request 

| Method | URL |
| --- | --- |
| POST | account/reset/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | password | string | True |
| Body | old-password | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | None |
| 400 |{'ERROR': 'Password not match'} |
| 400 | None |

---

### notes

user notes

#### Request 

| Method | URL |
| --- | --- |
| GET | account/notes/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | [] |  |

---

### tasks

user tasks

#### Request 

| Method | URL |
| --- | --- |
| GET | account/tasks/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | [] | [{'formatted_start_time',<br>'formatted_end_time',<br>'formatted_start_date',<br>'formatted_end_date',<br>'repeat_start_date',<br>'repeat_end_date',<br>'repeat_list',<br>'repeat',<br>'task_name',<br>'type',<br>'description',<br>'category',<br>'location',<br>'start',<br>'end',<br>'id',<br>'classroom',<br>'expired'} ... ] |

#### Request 

| Method | URL |
| --- | --- |
| POST | account/tasks/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | pk | int | true |
| body | task_name | string | false |
| body | type |  | false |
| body | description | string | false |
| body | category | string | false |
| body | location | string | false |
| body | start |DATE | false |
| body | end | DATE | false |
| body | id | int | false |
| body | classroom | int | false |

#### Response 

| Status | Response | 
| --- | --- |
| 201 | none |
| 404 | "detail": "Not found." |

### Request 

| Method | URL |
| --- | --- |
| DELETE | account/tasks/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | pk | int | true |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | "detail": "Not found." |

---

### Freetime

show user freetime table

#### Request 

| Method | URL |
| --- | --- |
| GET | account/freetime/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | 'freetime': |

---

### Forget 

if user forget their password. both /account/forget/ and /account/forget/pk/ are here

#### Request 

| Method | URL |
| --- | --- |
| POST | account/forget/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| body | email | string | true |

#### Response 

| Status | Response |
| --- | --- |
| 200 | 'message': 'The reset password email has been sent. ' |
| 404 | "detail": "Not found." |

#### Request 

| Method | URL |
| --- | --- |
| GET | account/forget/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| body | token | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | "detail": "Not found." |

#### Request 

| Method | URL |
| --- | --- |
| PUT | account/forget/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| body | token | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | "detail": "Not found." |

#### Request 

| Method | URL |
| --- | --- |
| POST | account/forget/(pk)/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| body | email | string | true |

#### Response 

| Status | Response |
| --- | --- |
| 200 | 'freetime': |
| 404 | "detail": "Not found." |

#### Request 

| Method | URL |
| --- | --- |
| GET | account/forget/(pk)/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| body | token | string | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | 'freetime': |
| 404 | "detail": "Not found." |

#### Request 

| Method | URL |
| --- | --- |
| PUT | account/forget/(pk)/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| body | token | string | True |
| 404 | "detail": "Not found." |

#### Response 

| Status | Response |
| --- | --- |
| 200 | 'freetime': |
| 404 | "detail": "Not found." |

---

### me

accessing personal information

#### Request 

| Method | URL |
| --- | --- |
| GET | account/me/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value
| --- | --- | --- |
| 200 | "id" | int |
|     | "classrooms" | [] |
|     | "is_professor": | boolean |
|     | "full_name": | string |
|     | "chatrooms": | [] |
|     | "tasks": | [] |
|     | "last_login": | null |
|     | "email": | string |
|     | "username": | string |
|     | "created": | Date |
|     | "updated": | Date |
|     | "first_name": | string |
|     | "mid_name": | string |
|     | "last_name": | string |
|     | "gender": | string |
|     | "birthday": | Date |
|     | "school_year": | int |
|     | "about_me": | "Yo!" |
|     | "level": | int |
|     | "phone": | int |
|     | "professor": | null |
|     | "avatar": | null |
|     | "major": | int |
|     | "friends": | [] |
|     | "pending_friends": | [] |
|     | "notifications": | [] |

#### Request 

| Method | URL |
| --- | --- |
| PUT | account/me/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |


#### Response 

| Status | Response | 
| --- | --- | 
| 200 | none |

---

### Professor

about the information of the professors

#### Request 

| Method | URL |
| --- | --- |
| GET | account/professor/(pk) |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | "id" | int |
|  | "full_name" | string |
|  | "classrooms" | [{"id", <br>"class_code",<br>"class_short",<br>"students_count",<br>"class_section",<br>"description",<br>"class_time":<br> {<br>"formatted_start_time",<br>"formatted_end_time",<br>"repeat_list": []<br>,"task_name",<br>"location",<br>"repeat" },<br>"semester":<br> {<br>"name",<br>"formatted_start_date",<br>"formatted_end_date"<br>},<br>"professors": <br>[{<br>"id",<br>"first_name",<br>"last_name",<br>"mid_name",<br>"email",<br>"office",<br>"created",<br>"major",<br>"tags": []<br>}, ...]|
|  | "folders" | [] |

#### Request 

| Method | URL |
| --- | --- |
| PUT | account/professor/(pk) |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | 'first_name' | string | True |
| body | 'last_name' | string | True |
| body | 'email' | string | True |
| body | 'office' | string | True |
| body | 'major' | int | True |

#### Response 

| Status | Response |
| --- | --- | 
| 200 | none |
| 404 | "detail": "Not found." |

### Professor comment

about the professors' comment
//cannot find the comment serializer

#### Request 

| Method | URL |
| --- | --- |
| GET | account/professor/(pk)/comment/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 |   |  |
| 404 | "detail": "Not found." |

#### Request 

| Method | URL |
| --- | --- |
| POST | account/professor/(pk)/comment/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 201 |   |  |
| 400 | none |
