import Vue from 'vue'
import chatApi from '../../api/chat-api'
import router from '../../router'
// import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
const state = {
    chatrooms: {
        // pk : {
        //   chatroom: {},
        //   message_list: [],
        //   users: [],
        // }
    },
    sockets: {
        // pk:  websocket
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
            return state.chatrooms[state.current_chatroom_pk].chatroom.accounts
    },
    currentChatroomMessages: (state) => {
        if (state.chatrooms[state.current_chatroom_pk])
            return state.chatrooms[state.current_chatroom_pk].message_list
    },
    currentChatroomName: (state) => {
        if (state.chatrooms[state.current_chatroom_pk])
            return state.chatrooms[state.current_chatroom_pk].name
    }
}

// actions
const actions = {
    getChatroom({ state, commit, dispatch }, pk) {
        // console.log(pk, state.chatrooms, state.chatrooms[pk])
        if (!state.chatrooms[pk]) {
            return chatApi.getChatroom(pk)
                .then((response) => {
                    commit(types.GET_CHATROOM, response)
                    return Promise.resolve()
                })
                .catch((error) => {
                    commit(types.LOG_ERROR, error)
                    return Promise.reject()
                })
        }
    },
    validateChatroom({ state, commit, dispatch }, pk) {
        chatApi.validateChatroom(pk)
            .then(() => {
                commit(types.USER_IN_CHATROOM, pk)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.USER_NOT_IN_CHATROOM, pk)
                return Promise.reject(error)
            })
    },

    setSockets({ rootState, state, commit, dispatch }) {
        for (let i in rootState.user.user.chatrooms) {
            const pk = rootState.user.user.chatrooms[i].id
            let socket = chatApi.connectSocket(pk)
            commit(types.SET_SOCKET, { socket: socket, pk: pk })
        }
    },

    connectSocket({ state, commit, dispatch }, pk) {
        if (state.sockets[pk]) {
            commit(types.CONNECT_SOCKET, pk)
        }
    },
    sendMessage({ state, commit, dispatch }, data) {
        commit(types.SEND_MESSAGE, data)
    },
}

// mutations
const mutations = {
    [types.GET_CHATROOM](state, response) {
        state.chatrooms[response.id] = {
            chatroom: {},
            chat_socket: {},
            message_list: [],
            users: [],
        }
        Vue.set(state.chatrooms[response.id], 'chatroom', response)
    },
    [types.SET_SOCKET](state, data) {
        // console.log('CONNECT_SOCKET to', state.chatrooms[data.pk], data.socket)
        // Vue.set(state.chatrooms[data.pk], 'chat_socket', data.socket)
        // state.chatrooms[data.pk]['chat_socket'] = data.socket
        state.sockets[data.pk] = data.socket
        // state.sockets[data.pk].onmessage = (message) => {
        //     console.log('received message', message.data)
        //     state.chatrooms[data.pk].message_list.push(JSON.parse(message.data))
        // }
    },
    [types.CONNECT_SOCKET](state, pk) {
        state.sockets[pk].onmessage = (message) => {
            console.log('received message', message.data)
            state.chatrooms[pk].message_list.push(JSON.parse(message.data))
        }
    },
    [types.SEND_MESSAGE](state, data) {
        console.log(state.sockets[data.pk])
        state.sockets[data.pk].send(JSON.stringify(data.message))
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
        router.push('/')
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
