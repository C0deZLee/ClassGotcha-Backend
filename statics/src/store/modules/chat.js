import chatApi from '../../api/chat-api'
import router from '../../router'
// import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
const state = {
    current_chatroom: null,
    sockets: {
        // pk:  websocket
    },
    messages: {
        // pk: {
        //     message:[]
        // }
    },
    valid: false,
    current_chatroom_pk: null,
    error_msg: null,
}

// getters
const getters = {
    currentChatroom: (state) => {
        if (state.current_chatroom)
            return state.current_chatroom
    },
    currentChatroomUsers: (state) => {
        if (state.current_chatroom)
            return state.current_chatroom.accounts
    },
    currentChatroomMessages: (state) => {
        if (state.messages[state.current_chatroom_pk])
            return state.messages[state.current_chatroom_pk]
    },
    currentChatroomName: (state) => {
        if (state.current_chatroom)
            return state.current_chatroom.name
    }
}

// actions
const actions = {
    getChatroom({ state, commit, dispatch }, pk) {
        return chatApi.getChatroom(pk)
            .then((response) => {
                commit(types.GET_CHATROOM, response)
                return Promise.resolve(response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject()
            })
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
        commit(types.CLEAR_SOCKET)
        for (let i in rootState.user.user.chatrooms) {
            const pk = rootState.user.user.chatrooms[i].id
            let socket = chatApi.connectSocket(pk)
            commit(types.SET_SOCKET, { socket: socket, pk: pk })
        }
    },
    sendMessage({ state, commit, dispatch }, data) {
        commit(types.SEND_MESSAGE, data)
    },
}

// mutations
const mutations = {
    [types.GET_CHATROOM](state, response) {
        console.log('loaded chatroom', response)
        state.current_chatroom = response
        // Vue.set(state.current_chatroom, 'chatroom', response)

        state.current_chatroom_pk = response.id
    },
    [types.CLEAR_SOCKET](state) {
        state.sockets = {}
    },
    [types.SET_SOCKET](state, data) {
        data.socket.onmessage = (message) => {
            console.log('received message', message.data)
            state.messages[data.pk].push(JSON.parse(message.data))
        }
        state.sockets[data.pk] = data.socket
        state.messages[data.pk] = []

    },
    [types.SEND_MESSAGE](state, data) {
        console.log('sent message', data.message)
        state.sockets[data.pk].send(JSON.stringify(data.message))
    },
    [types.USER_IN_CHATROOM](state, pk) {
        state.valid = true
    },
    [types.USER_NOT_IN_CHATROOM](state, pk) {
        state.current_chatroom = {}
        state.valid = false
        state.current_chatroom_pk = null
        router.push({ name: 'home' })
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
