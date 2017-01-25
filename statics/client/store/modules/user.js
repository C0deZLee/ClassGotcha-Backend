import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'


import { userApi } from '../../api/account'

import router from '../../router'

// initial state
// shape: [{ id, quantity }]
const state = {
    user: {},
    classes: [],
    chatrooms: [],
    friends: [],
    tasks: [],
    loginStatus: false,
    token: null
}

// getters
const getters = {
    loginStatus: state => state.loginStatus

}

// actions
const actions = {
    register({ commit, dispatch }, formData) {
        userApi.login(formData)
            .then((response) => {
                commit(types.LOGIN_SUCCESS, response)
                dispatch('getUser')
                // getClassrooms()
                // getChatrooms()
                // getFriends()
                // getTasks()
            })
            .catch((error) => {
                commit(types.LOGIN_FAILED, error)
            })
    },
    login({ commit, dispatch }, formData) {
        userApi.login(formData)
            .then((response) => {
                commit(types.LOGIN_SUCCESS, response)
                dispatch('getUser')
                dispatch('getClassrooms')
                dispatch('getChatrooms')
                dispatch('getFriends')
                dispatch('getTasks')
                router.push('/')
            })
            .catch((error) => {
                commit(types.LOGIN_FAILED, error)
            })
    },
    tokenVerify({ state, commit, dispatch }, formData) {
        userApi.tokenVerify(formData)
            .then((response) => {
                if (state.route.path === '/login' || state.route.path === '/register') {
                    commit(types.VERIFY_SUCCESS, response)
                    router.push('/')
                }
            })
            .catch((error) => {
                console.log(error)
                if (error.status === 401) {
                    dispatch('tokenRefresh', formData)
                } else {
                    commit(types.VERIFY_FAILED)
                }
            })
    },
    tokenRefresh({ commit, dispatch }, formData) {
        userApi.tokenRefresh(formData)
            .then((response) => {
                commit(types.REFRESH_SUCCESS, response)
            })
            .catch((error) => {
                commit(types.REFRESH_FAILED)
            })
    },
    logout({ commit }) {
        commit(types.LOGOUT)
    },
    getUser({ commit }) {
        userApi.getUser()
            .then((response) => {
                commit(types.LOAD_USER, response)
            })
            .catch((eror) => {
                commit(type.LOAD_FAILED, error)
            })
    },
    getClassrooms({ commit }) {
        userApi.getClassrooms()
            .then((response) => {
                commit(types.LOAD_CLASSROOMS, response)
            })
            .catch((eror) => {
                commit(type.LOAD_FAILED, error)
            })
    },
    getChatrooms({ commit }) {
        userApi.getChatrooms()
            .then((response) => {
                commit(types.LOAD_CHATROOMS, response)
            })
            .catch((eror) => {
                commit(type.LOAD_FAILED, error)
            })
    },
    getFriends({ commit }) {
        userApi.getFriends()
            .then((response) => {
                commit(types.LOAD_FRIENDS, response)
            })
            .catch((eror) => {
                commit(type.LOAD_FAILED, error)
            })
    },
    getTasks({ commit }, products) {
        userApi.getTasks()
            .then((response) => {
                commit(types.LOAD_TASKS, response)
            })
            .catch((eror) => {
                commit(type.LOAD_FAILED, error)
            })
    }
}

// mutations
const mutations = {
    [types.LOGIN_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.loginStatus = true
        router.push('/')
    },

    [types.LOAD_FAILED](state, error) {
        state.errorMsg = error
    },

    [types.VERIFY_SUCCESS](state, response) {
        state.token = response.token
        state.loginStatus = true
    },

    [types.VERIFY_FAILED](state, error) {
        cookie.delCookie('token')
        state.loginStatus = false
        state.token = null
        state.errorMsg = error
        router.push('/login')
    },

    [types.REFRESH_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.loginStatus = true
    },

    [types.REFRESH_FAILED](state, response) {
        cookie.delCookie('token')
        state.loginStatus = false
        state.token = null
        state.errorMsg = error
        router.push('/login')
    },

    [types.LOGIN_FAILED](state, error) {
        state.loginStatus = false
        state.token = null
        state.errorMsg = error
        router.push('/login')
    },

    [types.LOGOUT](state) {
        cookie.delCookie('token')
        state.classes = []
        state.chatrooms = []
        state.friends = []
        state.tasks = []
        state.loginStatus = false
        state.token = null
        router.push('/login')
    },

    [types.LOAD_USER](state, response) {
        state.user = response.data
    },
    [types.LOAD_CLASSROOMS](state, response) {
        state.classrooms = response.data
    },
    [types.LOAD_CHATROOMS](state, response) {
        state.chatrooms = response.data
    },
    [types.LOAD_FRIENDS](state, response) {
        state.friends = response.data
    },
    [types.LOAD_TASKS](state, response) {
        state.tasks = response.data
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
