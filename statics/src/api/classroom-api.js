import Vue from 'vue'
import Resource from 'vue-resource'

import { API_ROOT } from '../config.js'
import { getCookie } from '../utils/cookie'

Vue.use(Resource)

export default {
    // fatch data
    getClassroom(pk) {
        return Vue.http.get(API_ROOT + 'classroom/' + pk + '/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getNotes(pk) {
        return Vue.http.get(API_ROOT + 'classroom/' + pk + '/notes/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getTasks(pk) {
        return Vue.http.get(API_ROOT + 'classroom/' + pk + '/tasks/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getStudents(pk) {
        return Vue.http.get(API_ROOT + 'classroom/' + pk + '/students/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getMoments(pk) {
        return Vue.http.get(API_ROOT + 'classroom/' + pk + '/moments/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    getMajors() {
        return Vue.http.get(API_ROOT + 'classroom/majors/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    validate(pk) {
        return Vue.http.get(API_ROOT + 'classroom/' + pk + '/validate/', { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    // search
    search(formData) {
        return Vue.http.post(API_ROOT + 'classroom/search/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    // post changes
    postNote(pk, formData) {
        return Vue.http.post(API_ROOT + 'classroom/' + pk + '/notes/', formData, { emulateJSON: true, headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    },
    postTask(pk, formData) {
        return Vue.http.post(API_ROOT + 'classroom/' + pk + '/tasks/', formData, { headers: { Authorization: 'JWT ' + getCookie('token') } })
            .then((response) => Promise.resolve(response.data))
            .catch((error) => Promise.reject(error))
    }
}
