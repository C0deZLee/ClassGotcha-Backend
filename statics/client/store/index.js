import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'
import classroom from './modules/classroom'

import * as types from './mutation-types'

Vue.use(Vuex)


const state = {
    errorMsg: {},
    loginStatus: false,
    token: ''

}

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
        // TODO: FIXME!!!!!!!!
        userApi.tokenVerify(formData)
            .then((response) => {
                if (state.route.path === '/login' || state.route.path === '/register') {
                    //  NOT WORK
                    router.push('/')
                }
            })
            .catch((error) => {
                console.log(error)
                if (error.status === 401) {
                    dispatch('tokenRefresh', formData)
                } else {
                    commit(types.LOGIN_FAILED)
                }
            })
    },
    tokenRefresh({ commit, dispatch }, formData) {
        userApi.tokenRefresh(formData)
            .then((response) => {
                commit(types.LOGIN_SUCCESS, response)
            })
            .catch((error) => {
                commit(types.LOGIN_FAILED)
            })
    },
    logout({ commit }) {
        commit(types.LOGOUT)
    },
}

const mutations = {
    [types.LOGIN_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.loginStatus = true
    },

    [types.LOAD_FAILED](state, error) {
        state.errorMsg = error
    },

    [types.LOGIN_FAILED](state, error) {
        // cookie.delCookie('token')
        state.errorMsg = error
        state.loginStatus = false
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
    }
}

const isDebug = process.env.NODE_ENV !== 'production'
const store = new Vuex.Store({
    // if strict mode is true, then all state change must be triigered by mutations, otherwise compiler will throw error
    strict: isDebug,
    state,
    mutations,
    actions,
    modules: {
        user,
        classroom
    }
})
export default store
