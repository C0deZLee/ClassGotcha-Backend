import Vue from 'vue'
import Resource from 'vue-resource'

import { API_ROOT } from '../config'
import { getCookie } from '../utils/cookie'

Vue.use(Resource)

export default {
    // Authorization
    login(formData) {
        return Vue.http.post(API_ROOT + 'account/login/', formData)
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    register(formData) {
        return Vue.http.post(API_ROOT + 'account/register/', formData)
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    passwordReset(formData) {
        return Vue.http.post(API_ROOT + 'account/reset/', formData)
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    tokenVerify(formData) {
        return Vue.http.post(API_ROOT + 'account/login-verify/', formData)
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    tokenRefresh(formData) {
        return Vue.http.post(API_ROOT + 'account/login-refresh/', formData)
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    // Load User Data
    getSelf() {
        return Vue.http.get(API_ROOT + 'account/me/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getUser(pk) {
        return Vue.http.get(API_ROOT + 'account/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getAvatar() {
        return Vue.http.get(API_ROOT + 'account/avatar/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getClassrooms() {
        return Vue.http.get(API_ROOT + 'account/classrooms/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getChatrooms() {
        return Vue.http.get(API_ROOT + 'account/chatrooms/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getFriends() {
        return Vue.http.get(API_ROOT + 'account/friends/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getPendingFriends() {
        return Vue.http.get(API_ROOT + 'account/pending-friends/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getTasks() {
        return Vue.http.get(API_ROOT + 'account/tasks/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getMoments() {
        return Vue.http.get(API_ROOT + 'account/moments/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },

    // update changes
    updateSelf(formData) {
        return Vue.http.put(API_ROOT + 'account/me/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },

    // change relation
    addClassroom(pk) {
        return Vue.http.post(API_ROOT + 'account/classrooms/' + pk + '/', {}, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    remClassroom(pk) {
        return Vue.http.delete(API_ROOT + 'account/classrooms/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    addChatroom(pk) {
        return Vue.http.post(API_ROOT + 'account/clatrooms/' + pk + '/', {}, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    remChatroom(pk) {
        return Vue.http.delete(API_ROOT + 'account/clatrooms/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    addFriend(pk) {
        return Vue.http.post(API_ROOT + 'account/friends/' + pk + '/', {}, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    acceptFriend(pk) {
        return Vue.http.put(API_ROOT + 'account/friends/' + pk + '/', {}, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    remFriend(pk) {
        return Vue.http.delete(API_ROOT + 'account/friends/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    // post new 
    postMoment(formdata) {
        return Vue.http.post(API_ROOT + 'account/moments/', formdata, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    delMoment(pk) {
        return Vue.http.delete(API_ROOT + 'account/moments/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    postTask(fromData) {
        return Vue.http.post(API_ROOT + 'account/tasks/', fromData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    }
}

//  this.$http.post(state.apiEndPoint + '/account/login/', formData).then(response => {
//     // success
//     // store auth token
//     state.authToken = response.data.token
//     // write token to cookie, expires in 1 day
//     this.$cookie.set('token', response.data.token, 1)
//     this.$http.headers.common.Authorization = 'JWT ' + response.data.token
//     // load user data
//     this.$http.get(state.apiEndPoint + '/account/me/', {
//         headers: {
//             Authorization: 'JWT ' + state.authToken
//         }
//     }).then(response => {
//         state.user = response.data
//     })
//     // load user class
//     this.$http.get(state.apiEndPoint + '/account/classrooms/', {
//         headers: {
//             Authorization: 'JWT ' + state.authToken
//         }
//     }).then(response => {
//         state.classrooms = response.data
//     })
//     // load user chatrooms
//     this.$http.get(state.apiEndPoint + '/account/chatrooms/', {
//         headers: {
//             Authorization: 'JWT ' + state.authToken
//         }
//     }).then(response => {
//         state.chatrooms = response.data
//         console.log(response.data)
//     })
//     // redirect to home page
//     this.$router.push('/')
// }, response => {
//     // failed
//     console.log(response.status)
// })
