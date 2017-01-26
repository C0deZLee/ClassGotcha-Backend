import chatApi from '../../api/chat'
import router from '../../router'
import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
// shape: [{ id, quantity }]
const state = {
    chatroom: {},
    chat_socket: {},
    message_list: [],
    users: [],
    error_msg: '',
}

// getters
const getters = {
    currentChatroom: (state) => {
        return state.chatroom
    },
    currentChatroomUsers: (state) => {
        return state.users
    },
    chatSocket: (state) => {
        return state.chat_socket
    }
}

// actions
const actions = {
    getChatroom({ commit, dispatch }, pk) {
        chatApi.getChatroom(pk)
            .then((response) => {
                commit(types.GET_CHATROOM, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getChatroomUsers({ commit, dispatch }, pk) {
        chatApi.getChatroomUsers(pk)
            .then((response) => {
                commit(types.USER_IN_CHATROOM)
            })
            .catch((error) => {
                commit(types.USER_NOT_IN_CHATROOM)
            })
    },
    validateChatroom({ rootState, commit, dispatch }) {
        chatApi.validate(rootState.route.params.chatroom_id)
            .then((response) => {
                commit(types.LOAD_CHATROOM_USERS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    connectSocket({ commit, dispatch }, pk) {
        const socket = chatApi.connectSocket(pk)
        commit(types.CONNECT_SOCKET, socket)
    },
    sendMessage({ state, commit, dispath }, message) {
        commit(types.SEND_MESSAGE, message)
    },
}

// mutations
const mutations = {

    [types.LOAD_CHATROOM_USERS](state, response) {
        state.users = response
    },
    [types.CONNECT_SOCKET](state, socket) {
        state.chat_socket = socket
        state.chat_socket.onmessage = (message) => {
            console.log("received message ")
            console.log(message.data)
            state.message_list.push(JSON.parse(message.data))
        }
    },
    [types.SEND_MESSAGE](state, message) {
        state.chat_socket.send(JSON.stringify(message));
    },
    [types.USER_IN_CHATROOM](state) {},

    [types.USER_NOT_IN_CHATROOM](state) {
        router.push('/')
        // TODO, FIXME, need to redirect to previous page
    },
    [types.LOG_ERROR](state, error) {
        state.error_msg = error
        // TODO, need to handle errors
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}
