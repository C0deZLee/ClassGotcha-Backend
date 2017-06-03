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
| 201 | {'token': <auth_token>} |

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
| 404 | "detail": "Not found." |

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
| 404 | "detail": "Not found." |

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
| 404 | "detail": "Not found." |

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
| 404 | "detail": "Not found." |

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
| GET | account/pending-friends/ |

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

| Status | Response |
| --- | --- |
| 200 | [{'pk',<br>'id', <br>'avatar', <br>'username', <br>'email', <br>'full_name', <br>'about_me', <br>'level', <br>'tag':{<br>'name'}}, ...] |

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
| 400 | none |
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
| 200 | 'message': 'The reset password email has been sent. ' |
| 400 | none |
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
| 200 | none |
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
| 200 | none |
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
| 200 | [] | [{'id',<br>'title', <br>'comments', <br>'creator', <br>'created', <br>'vote', <br>'tags'}, ...] |
| 404 | "detail": "Not found." |

#### Request 

| Method | URL |
| --- | --- |
| POST | account/professor/(pk)/comment/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | content |  | True |

#### Response 

| Status | Response |
| --- | --- |
| 201 | none |
| 400 | none |

---

## Chat
### Validate
#### Request 

| Method | URL |
| --- | --- |
|  | chat/pk/validate/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |


### last-message
#### Request 

| Method | URL |
| --- | --- |
|  | chat/pk/last-message/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |

### users
#### Request 

| Method | URL |
| --- | --- |
|  | chat/pk/users/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |

### pk
#### Request 

| Method | URL |
| --- | --- |
|  | chat/pk/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |

###
#### Request 

| Method | URL |
| --- | --- |
|  | chat/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |

---

## classroom
### notes

user notes

#### Request 

| Method | URL |
| --- | --- |
| GET | classroom/pk/notes/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | [{'pk',<br>'id', <br>'avatar', <br>'username', <br>'email', <br>'full_name', <br>'about_me', <br>'level', <br>'tag':{<br>'name'}}, ...] |
| 404 | none |

#### Request 

| Method | URL |
| --- | --- |
| POST | classroom/pk/notes/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | uploaded_file | file | true |
| body | title | string | true |
| body | tags | string | true |
| body | description | sting | true |

#### Response 

| Status | Response |
| --- | --- |
| 201 | none |
| 400 | none |

---

### tasks

user task

#### Request 

| Method | URL |
| --- | --- |
| GET | classroom/pk/tasks/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | [] | [{'formatted_start_time',<br>'formatted_end_time',<br>'formatted_start_date',<br>'formatted_end_date',<br>'repeat_start_date',<br>'repeat_end_date',<br>'repeat_list',<br>'repeat',<br>'task_name',<br>'type',<br>'description',<br>'category',<br>'location',<br>'start',<br>'end',<br>'id',<br>'classroom',<br>'expired'} ... ] |

#### Request 

| Method | URL |
| --- | --- |
| POST | classroom/pk/tasks/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | start | DATE | true |
| body | end | DATE | true |
| body | task_name | string | true |

#### Response 

| Status | Response |
| --- | --- |
| 201 | none |
| 400 | none |

---

### students

view students in classroom id

#### Request 

| Method | URL |
| --- | --- |
| GET | classroom/pk/students/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | [{'pk',<br>'id', <br>'avatar', <br>'username', <br>'email', <br>'full_name', <br>'about_me', <br>'level'}, ... ] |
| 404 | none |

---

### moments

user moments

#### Request 

| Method | URL |
| --- | --- |
| GET | classroom/pk/moments/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | [] | [{"id", <br> "comments",<br> "creator" <br>{<br> "pk", <br> "id", <br> "avatar", <br>"username", <br>"email", <br>"full_name", <br>"about_me", <br>"level" <br>}, <br>"likes", <br>"content", <br>"images", <br>"deleted", <br>"solved", <br>"permission", <br>"created", <br>"updated", <br>"classroom", <br>"flagged_users", <br>"liked_users"}, ... ] |
| 404 | none |

---

### validate

validate status of user in classroom

#### Request 

| Method | URL |
| --- | --- |
| GET | classroom/pk/validate/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 403 | 'error': 'You are not in this classroom' |

---

### 
#### Request 

| Method | URL |
| --- | --- |
| GET | classroom/pk/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | "id" | int |
|  | "class_time" | {<br>"formatted_start_time",<br>"formatted_end_time",<br>"repeat_list": [],<br>"task_name",<br>"location",<br>"repeat"} |
|  | "students" | [] |
|  | "students_count" | string |
|  | "class_short" | string |
|  | "folders" | [] |
|  | "semester" |{<br>"name",<br>"formatted_start_date",<br>"formatted_end_date"} |
|  | "major" | {"id",<br>"major_short",<br>"major_full",<br>"major_college",<br>"department",<br>"major_icon"},
|  | "professors" | [{<br>"id", <br>"full_name",<br>"classrooms":<br>[{<br>  "id",<br>"class_code",<br>"class_short",<br>"students_count",<br>"class_section",<br>"description",<br>"class_time":<br> {<br>"formatted_start_time",<br>"formatted_end_time",<br>"repeat_list",<br>"task_name",<br>"location",<br>"repeat"<br>},<br>"semester":<br> {"name",<br>"formatted_start_date",<br>"formatted_end_date"<br>},<br>"professors":<br>[{<br>"id",<br>"first_name",<br>"last_name",<br>"mid_name",<br>"email",<br>"office",<br>"created",<br>"major",<br>"tags"<br>}],<br>"folders"<br>},<br> ...],<br>"office_hours",<br>"avg_rate",<br>"first_name",<br>  "last_name",<br>"mid_name",<br>"email",<br>"office",<br>"created",<br>"major",<br>"tags"<br>}] |
|  | "class_name" | string |
|  |"class_number"| int |
|  |"class_code"| int |
|  |"class_section"| int |
|  |"class_credit" | int |
|  |"class_location": | string |
|  |"syllabus" | file |
|  |"description"| string |
|  |"created" | DATE |
|  |"updated" | DATE |

---

### search

search things

#### Request 

| Method | URL |
| --- | --- |
| POST | classroom/search/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 | students | {'pk',<br>'id', <br>'avatar', <br>'username', <br>'email', <br>'full_name', <br>'about_me', <br>'level'}
|  | 'name' | string |
|  | folders | {'name', <br>'formatted_start_date', <br>'formatted_end_date'} |
|  | major | {full_name , <br>classrooms, <br>office_hours, <br>avg_rate} |
| 400 | none |  |

---

### majors

view majors

#### Request 

| Method | URL |
| --- | --- |
| GET | classroom/majors/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value |
| --- | --- | --- |
| 200 |"id" | 63 |
|  | "major_short" | string |
|  | "major_full" | string |
|  | "major_college" | string |
|  | "department" | string |
|  | "major_icon" |  |

---

### upload

upload file

#### Request 

| Method | URL |
| --- | --- |
| POST | classroom/upload/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | file | file | true |

#### Response 

| Status | Response |
| --- | --- |
| 201 | none |
| 400 | none |
| 403 | none |

---

## email
does not work

## posts
### moment/comment
#### Request 

| Method | URL |
| --- | --- |
| POST | /post/moment/pk/comment/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 400 | none |
| 404 | none |

---

### moment/like
#### Request 

| Method | URL |
| --- | --- |
| POST | /post/moment/pk/like/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | none |

---

### moment/solve
#### Request 

| Method | URL |
| --- | --- |
| POST | /post/moment/pk/solve/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | none |

---

### moment/report
#### Request 

| Method | URL |
| --- | --- |
| PUT | /post/moment/pk/report/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | none |

---

### moment/pk
#### Request 

| Method | URL |
| --- | --- |
| GET | /post/moment/pk/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | value |
| --- | --- | --- |
| 200 | id | int |
|  | comments | [{<br>"id",<br>"creator": <br>{<br>"pk",<br>"id",<br>"avatar",<br>"username",<br>"email",<br>"full_name",<br>"about_me",<br>"level"<br>},<br>"content",<br>"created",<br>"updated",<br>"post",<br>"moment",<br>"note",<br>"professor",<br>"rate"<br>}] |
|  | creator | {"pk",<br>"id",<br>"avatar",<br>"username",<br>"email",<br>"full_name",<br>"about_me",<br>"level"} |
|  | likes | int |
|  | content | string |
|  | images" | null |
|  | deleted" | boolean |
|  | solved | null |
|  | permission | int |
|  | created | DATE |
|  | updated | DATE |
|  | classroom | int |
|  | flagged_users | [] |
|  | liked_users | [] |
| 404 | none |  |

---

### post
#### Request 

| Method | URL |
| --- | --- |
| GET | /post/post/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | value |
| --- | --- | --- |
| 200 | [] |["id",<br><br>"title",<br>"comments",<br>"creator": <br>{<br>"pk",<br>"id",<br>"avatar",<br>"username",<br>"email",<br>"full_name",<br>"about_me",<br>"level"<br>},<br>"created",<br>"vote",<br>"tags"}, ... ] |
| 404 | none |  |

#### Request 

| Method | URL |
| --- | --- |
| POST | /post/post/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | title | string | true |
| body | content | string | true |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 400 | none |

---

### post/pk
#### Request 

| Method | URL |
| --- | --- |
| GET | /post/pk/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | "id" | int |
|  | "comments" | [],
|  | "creator" | {"pk",<br>"id",<br>"avatar",<br>"username",<br>"email",<br>"full_name",<br>"about_me",<br>"level"} |
|  | "vote" | int |
|  | "tags" | [] |
|  | "title" | string |
|  | "content" | string |
|  | "flagged_num" | int |
|  | "permission" | int |
|  | "created" | DATE |
|  | "updated" | DATE |
|  | "up_voted_user" | [] |
|  | "down_voted_user" | [] |
| 404 | none |  |

#### Request 

| Method | URL |
| --- | --- |
| PUT | /post/pk/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | vote | int | true |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 400 | none |
| 404 | none |

### post/pk/comment

## tags
does not have url file

## tasks
### pk

put update
delete delete
#### Request 

| Method | URL |
| --- | --- |
| PUT | /pk/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| body | task_name | string | true |
| body | description | string | true |
| body | start | DATE | true |
| body | end | DATE | true |
| body | location | int | true |
| body | category | int | true |
| body | repeat | [int] |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | none |

#### Request 

| Method | URL |
| --- | --- |
| DELETE | /pk/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response |
| --- | --- |
| 200 | none |
| 404 | none |
