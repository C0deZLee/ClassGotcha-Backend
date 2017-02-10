import Vue from 'vue'
import Resource from 'vue-resource'

import { API_ROOT } from '../config.js'
import { getCookie } from '../utils/cookie'

Vue.use(Resource)

export default {
    // post changes
    solveMoment(pk) {
        return Vue.http.post(API_ROOT + 'post/moment/' + pk + '/solve/', {}, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    postMomentComment(pk, formData) {
        return Vue.http.post(API_ROOT + 'post/moment/' + pk + '/comment/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    addLike(pk) {
        return Vue.http.post(API_ROOT + 'post/moment/' + pk + '/like/', {}, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    addReport(pk) {
        return Vue.http.put(API_ROOT + 'post/moment/' + pk + '/report/', {}, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getPosts() {
        return Vue.http.get(API_ROOT + 'post/post/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getPost(pk) {
        return Vue.http.get(API_ROOT + 'post/post/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    postPost(formData) {
        return Vue.http.post(API_ROOT + 'post/post/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    postPostComment(pk, formData) {
        return Vue.http.post(API_ROOT + 'post/post/' + pk + '/comment/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    addPostVote(pk, formData) {
        return Vue.http.put(API_ROOT + 'post/post/' + pk + '/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    }

}
