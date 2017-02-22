// -------COMMON ---------
export const LOG_ERROR = 'LOG_ERROR'
export const UPLOAD_FILE = 'UPLOAD_FILE'
export const CLEAR_FILE = 'CLEAR_FILE'

// ------- USER --------
export const LOGIN_SUCCESS = 'LOGIN_SUCCESS'
export const LOGIN_FAILED = 'LOGIN_FAILED'

export const REGSITER_SUCCESS = 'REGSITER_SUCCESS'
export const REGSITER_FAILED = 'REGSITER_FAILED'

export const VERIFY_SUCCESS = 'VERIFY_SUCCESS'
export const VERIFY_FAILED = 'VERIFY_FAILED'

export const REFRESH_SUCCESS = 'REFRESH_SUCCESS'
export const REFRESH_FAILED = 'REFRESH_FAILED'

export const LOGOUT = 'LOGOUT'

export const UPDATE_AVATAR = 'UPDATE_AVATAR'

export const LOAD_SELF = 'LOAD_SELF'
export const UPDATE_SELF = 'UPDATE_SELF'
export const UPDATE_SELF_FAILED = 'UPDATE_SELF_FAILED'

export const LOAD_USER = 'LOAD_USER'

export const LOAD_CLASSROOMS = 'LOAD_CLASSROOMS'
export const ADD_CLASSROOM = 'ADD_CLASSROOM'
export const REMOVE_CLASSROOM = 'REMOVE_CLASSROOM'

export const LOAD_FRIENDS = 'LOAD_FRIENDS'
export const LOAD_PENDING_FRIENDS = 'LOAD_PENDING_FRIENDS'
export const ADD_FRIEND = 'ADD_FRIEND'
export const ACCEPT_FRIEND = 'ACCEPT_FRIEND'
export const REMOVE_FRIEND = 'REMOVE_FRIEND'

export const LOAD_TASKS = 'LOAD_TASKS'
export const POST_TASK = 'ADD_TASK'
export const REMOVE_TASK = 'REMOVE_TASK'

export const LOAD_CHATROOMS = 'LOAD_CHATROOMS'
export const ADD_CHATROOM = 'ADD_CHATROOM'
export const REMOVE_CHATROOM = 'REMOVE_CHATROOM'

export const LOAD_MOMENTS = 'LOAD_MOMENTS'
// here use POST not ADD because post a moment will create new record in database,
// not just add a relationship, and this operation does not need pk,
// you should follow this naming pattern
export const POST_MOMENT = 'POST_MOMENT'
export const REMOVE_MOMENT = 'REMOVE_MOMENT'

// ------ Classroom -------
export const SEARCH_CLASSROOMS = 'SEARCH_CLASSROOMS'

export const GET_CLASSROOM = 'GET_CLASSROOM'

export const LOAD_CLASSROOM_MAJORS = 'LOAD_CLASSROOM_MAJORS'

export const LOAD_CLASSROOM_MOMENTS = 'LOAD_CLASSROOM_MOMENTS'
export const LOAD_CLASSROOM_USERS = 'LOAD_CLASSROOM_USERS'

export const LOAD_CLASSROOM_TASKS = 'LOAD_CLASSROOM_TASKS'
export const POST_CLASSROOM_TASK = 'POST_CLASSROOM_TASK'

export const LOAD_CLASSROOM_NOTES = 'LOAD_CLASSROOM_NOTES'
export const POST_CLASSROOM_NOTE = 'POST_CLASSROOM_NOTE'

export const USER_IN_CLASSROOM = 'USER_IN_CLASSROOM'
export const USER_NOT_IN_CLASSROOM = 'USER_NOT_IN_CLASSROOM'

export const JOIN_CLASSROOM = 'JOIN_CLASSROOM'
export const JOIN_CLASSROOM_FAILED = 'JOIN_CLASSROOM_FAILED'
export const QUIT_CLASSROOM = 'QUIT_CLASSROOM'

// ----- Chatroom --------
export const GET_CHATROOM = 'GET_CHATROOM'

export const LOAD_CHATROOM_USERS = 'LOAD_CHATROOM_USERS'
export const CLEAR_SOCKET = 'CLEAR_SOCKET'
export const SET_SOCKET = 'SET_SOCKET'
export const CONNECT_SOCKET = 'CONNECT_SOCKET'
export const SEND_MESSAGE = 'SEND_MESSAGE'

export const USER_IN_CHATROOM = 'USER_IN_CHATROOM'
export const USER_NOT_IN_CHATROOM = 'USER_NOT_IN_CHATROOM'

// ----- posts -------
export const ADD_MOMENT_SOLVE = 'ADD_MOMENT_SOLVE'
export const ADD_MOMENT_LIKE = 'ADD_MOMENT_LIKE'
export const ADD_MOMENT_REPORT = 'ADD_MOMENT_REPORT'
export const POST_MOMENT_COMMENT = 'POST_MOMENT_COMMENT'

export const POST_POST = 'POST_POST'
export const LOAD_POSTS = 'LOAD_POSTS'
export const LOAD_POST = 'LOAD_POST'
export const POST_POST_COMMENT = 'POST_POST_COMMENT'
export const ADD_POST_VOTE = 'ADD_POST_VOTE'

// ----- tasks -----
export const UPDATE_TASK = 'UPDATE_TASK'
export const DELETE_TASK = 'DELETE_TASK'
