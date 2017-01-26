import Vue from 'vue'
import chatApi from '../../api/chat'
import router from '../../router'
import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
const state = {
    chatrooms: {
        // pk : {
        //   chatroom: {},
        //   chat_socket: {},
        //   message_list: [],
        //   users: [],
        // }
    },
    valid: false,
    current_chatroom_pk: null,
    error_msg: null,
}

// getters
const getters = {
    currentChatroom: (state) => {
        if (state.chatrooms[state.current_chatroom_pk])
            return state.chatrooms[state.current_chatroom_pk].chatroom
    },
    currentChatroomUsers: (state) => {
        if (state.chatrooms[state.current_chatroom_pk])
            return state.chatrooms[state.current_chatroom_pk].users
    },
    validChatroom: (state) => {
        return state.valid
    },
}

// actions
const actions = {
    getChatroom({ commit, dispatch }, pk) {
        if (!state.chatrooms[pk]) {
            chatApi.getChatroom(pk)
                .then((response) => {
                    console.log(response, pk)
                    commit(types.GET_CHATROOM, { response: response, pk: pk })
                })
                .catch((error) => {
                    console.log(error)
                    commit(types.LOG_ERROR, error)
                })
        }
    },
    getChatroomUsers({ state, commit, dispatch }, pk) {
        console.log(state.chatrooms[pk])
        if (state.chatrooms[pk] && !state.chatrooms[pk].users) {
            chatApi.getChatroomUsers(pk)
                .then((response) => {
                    commit(types.LOAD_CHATROOM_USERS, { response: response, pk: pk })
                })
                .catch((error) => {
                    commit(types.LOG_ERROR, error)
                })
        }
    },
    validateChatroom({ state, commit }, pk) {
        chatApi.validateChatroom(pk)
            .then((response) => {
                commit(types.USER_IN_CHATROOM, pk)
            })
            .catch((error) => {
                commit(types.USER_NOT_IN_CHATROOM, pk)
            })
    },
    connectSocket({ state, commit }, pk) {
        if (state.chatrooms[pk]) {
            const socket = chatApi.connectSocket(pk)
            commit(types.CONNECT_SOCKET, { socket: socket, pk: pk })
            state.chatrooms[pk].chat_socket.onmessage = (message) => {
                console.log("received message ")
                console.log(message.data)
                commit(types.RECIEVE_MESSAGE, { message: message.data, pk: pk })
            }
        }
    },
    sendMessage({ commit }, data) {
        console.log('send message commit with', data)
        commit(types.SEND_MESSAGE, data)
    },
}

// mutations
const mutations = {
    [types.GET_CHATROOM](state, data) {
        Vue.set(state.chatrooms[data.pk], 'chatroom', data.response)
    },
    [types.LOAD_CHATROOM_USERS](state, data) {
        Vue.set(state.chatrooms[data.pk], 'users', data.response)
    },
    [types.CONNECT_SOCKET](state, data) {
        Vue.set(state.chatrooms[data.pk], 'chat_socket', data.socket)
        Vue.set(state.chatrooms[data.pk], 'message_list', [])
    },
    [types.SEND_MESSAGE](state, data) {
        state.chatrooms[data.pk].chat_socket.send(JSON.stringify(data.message));
    },
    [types.RECIEVE_MESSAGE](state, data) {
        state.chatrooms[data.pk].message_list.push(JSON.parse(data.message))
    },
    [types.USER_IN_CHATROOM](state, pk) {
        state.valid = true
        state.current_chatroom_pk = pk
    },
    [types.USER_NOT_IN_CHATROOM](state, pk) {
        if (state.chatrooms[pk])
            delete state.chatrooms[pk]
        state.valid = false
        state.current_chatroom_pk = null
        // state.chatrooms[pk].valid = false

        // router.push('/')
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
