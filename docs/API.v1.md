# ClassGotcha API Documentation 
### Version 1.0

## Account

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

###Request

| Method | URL |
| --- | --- |
| GET | account/moments/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |

#### Response 

| Status | Response | Value
| --- | --- | --- |
| 200 | [] |  "id", 
              "comments",
              "creator" {
                          "pk",
                          "id",
                          "avatar",
                          "username",
                          "email",
                          "full_name",
                          "about_me",
                          "level"
                        },
              "likes",
              "content",
              "images",
              "deleted",
              "solved",
              "permission",
              "created",
              "updated",
              "classroom",
              "flagged_users",
              "liked_users" |

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
| Body | file | file
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

| Status | Response | Value
| --- | --- |
| 200 | [] | {'id',
              'class_code',
              'class_short',
              'students_count',
              'class_section',
              'description',
              'class_time',
              'semester',
              'professors',
              'folders'} |

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

| Status | Response | Value
| --- | --- |
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

| Status | Response | Value
| --- | --- |
| 200 | [] | 'pk', 'id', 'avatar', 'username', 'email', 'full_name', 'about_me', 'level' |

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
      | "classrooms" | [] |
      | "is_professor": | boolean |
      | "full_name": | string |
      | "chatrooms": | [] |
      | "tasks": | [] |
      | "last_login": | null |
      | "email": | string |
      | "username": | string |
      | "created": | Date |
      | "updated": | Date |
      | "first_name": | string |
      | "mid_name": | string |
      | "last_name": | string |
      | "gender": | string |
      | "birthday": | Date |
      | "school_year": | int |
      | "about_me": | "Yo!" |
      | "level": | int |
      | "phone": | int |
      | "professor": | null |
      | "avatar": | null |
      | "major": | int |
      | "friends": | [] |
      | "pending_friends": | [] |
      | "notifications": | [] |

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

### change_password

for user to change password

#### Request 

| Method | URL |
| --- | --- |
| POST | account/change_password/ |

| Type | Params | Values | Required |
| --- | --- | --- | --- |
| Header | Authorization | auth_token | True |
| Body | 'old-password' | string | True |
| Body | 'password' | string | True |

#### Response 

| Status | Response |
| --- | --- | --- |
| 400 | none |
| 400 | 'ERROR': 'Password not match' |

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
      | "classrooms" | [] |
      | "is_professor": | boolean |
      | "full_name": | string |
      | "chatrooms": | [] |
      | "tasks": | [] |
      | "last_login": | null |
      | "email": | string |
      | "username": | string |
      | "created": | Date |
      | "updated": | Date |
      | "first_name": | string |
      | "mid_name": | string |
      | "last_name": | string |
      | "gender": | string |
      | "birthday": | Date |
      | "school_year": | int |
      | "about_me": | "Yo!" |
      | "level": | int |
      | "phone": | int |
      | "professor": | null |
      | "avatar": | null |
      | "major": | int |
      | "friends": | [] |
      | "pending_friends": | [] |
      | "notifications": | []|
| 404 | "detail": "Not found." |

---
