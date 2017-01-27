import Vue from 'vue'
import Resource from 'vue-resource'
import ReconnectingWebSocket from 'reconnecting-websocket'

import { API_ROOT, WS_ROOT } from '../config.js'
import { getCookie } from '../utils/cookie'

Vue.use(Resource)

export default {
    // fatch data
    getChatroom(pk) {
        return Vue.http.get(API_ROOT + 'chatroom/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },

    getChatroomUsers(pk) {
        return Vue.http.get(API_ROOT + 'chatroom/' + pk + '/users/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },

    validateChatroom(pk) {
        return Vue.http.get(API_ROOT + 'chatroom/' + pk + '/validate/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },

    // post changes
    createChatroom(formData) {
        return Vue.http.post(API_ROOT + 'chatroom/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },

    // Web socket
    connectSocket(pk) {
        return new ReconnectingWebSocket(WS_ROOT + 'chat/' + pk)
    }
}
