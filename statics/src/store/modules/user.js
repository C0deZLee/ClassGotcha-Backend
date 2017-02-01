import { userApi } from '../../api/user-api'
import router from '../../router'
import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

import default_avatar1x from 'img/default-avatar1x.png'
import default_avatar2x from 'img/default-avatar2x.png'
import default_avatar4x from 'img/default-avatar4x.png'

// initial state
// shape: [{ id, quantity }]
const state = {
    user: {},
    friends: [],
    moments: [],
    login_status: false,
    token: null,
    loaded_user: {}
}

// getters
const getters = {
    login_status: state => state.login_status,
    me: state => {
        if (state.login_status)
            return state.user
    },
    userID: state => {
        if (state.login_status) {
            return state.user.id
        }
    },
    userFullName: state => {
        if (state.login_status) {
            return state.user.full_name
        } else {
            return 'None'
        }
    },
    userAvatar: state => {
        if (state.login_status) {
            return state.user.avatar
        } else {
            return 'None'
        }
    },
    userClassrooms: state => {
        if (state.login_status) {
            return state.user.classrooms
        } else {
            return []
        }
    },
    userChatrooms: state => {
        if (state.login_status) {
            return state.user.chatrooms
        } else {
            return []
        }
    },
    userMoments: state => {
        if (state.login_status) {
            return state.moments
        } else {
            return []
        }
    },
    userTasks: state => {
        if (state.login_status) {
            return state.user.tasks
        } else {
            return []
        }
    },
    loadedUser: state => {
        return state.loaded_user
    }

}

// actions
const actions = {
    register({ commit, dispatch }, formData) {
        console.log('register', formData)
        return userApi.register(formData)
            .then((response) => {
                commit(types.REGSITER_SUCCESS, response)
                dispatch('getSelf')
                // getClassrooms()
                // getChatrooms()
                // getFriends()
                // getTasks()
            })
            .catch((error) => {
                commit(types.REGSITER_FAILED, error)
                return Promise.reject(error)
            })
    },
    login({ commit, dispatch }, formData) {
        return userApi.login(formData)
            .then((response) => {
                console.log(response)
                commit(types.LOGIN_SUCCESS, response)
                dispatch('getSelf')
                dispatch('getFriends')
                dispatch('setSockets')
                router.push('/')
            })
            .catch((error) => {
                commit(types.LOGIN_FAILED, error)
                return Promise.reject(error)
            })
    },
    tokenVerify({ rootState, commit, dispatch }, formData) {
        userApi.tokenVerify(formData)
            .then((response) => {
                commit(types.VERIFY_SUCCESS, response)
                if (rootState.route.path === '/login' || rootState.route.path === '/register') {
                    router.push('/')
                }
                dispatch('getSelf')
                dispatch('getFriends')
                dispatch('setSockets')
            })
            .catch((error) => {
                if (rootState.route.path !== '/register') {
                    dispatch('tokenRefresh', formData)
                }
                commit(types.LOG_ERROR, error)
            })
    },
    tokenRefresh({ commit, dispatch }, formData) {
        userApi.tokenRefresh(formData)
            .then((response) => {
                commit(types.REFRESH_SUCCESS, response)
                dispatch('getSelf')
                dispatch('getFriends')
                dispatch('setSockets')
            })
            .catch((error) => {
                commit(types.LOGIN_FAILED)
                commit(types.LOG_ERROR, error)

            })
    },
    logout({ commit }) {
        commit(types.LOGOUT)
    },
    getSelf({ commit }) {
        userApi.getSelf()
            .then((response) => {
                commit(types.LOAD_SELF, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getClassrooms({ commit }) {
        userApi.getClassrooms()
            .then((response) => {
                commit(types.LOAD_CLASSROOMS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getChatrooms({ commit }) {
        userApi.getChatrooms()
            .then((response) => {
                commit(types.LOAD_CHATROOMS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getFriends({ commit }) {
        userApi.getFriends()
            .then((response) => {
                commit(types.LOAD_FRIENDS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getTasks({ commit }) {
        userApi.getTasks()
            .then((response) => {
                commit(types.LOAD_TASKS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getUser({ commit }, pk) {
        userApi.getUser(pk)
            .then((response) => {
                commit(types.LOAD_USER, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    addClassroom({ commit, dispatch }, pk) {
        userApi.addClassroom(pk)
            .then((response) => {
                commit(types.ADD_CLASSROOM)
                dispatch('getSelf')
                // dispatch('getClassrooms')
                // dispatch('getChatrooms')
                // dispatch('getTasks')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    remClassroom({ commit, dispatch }, pk) {
        userApi.remClassroom(pk)
            .then((response) => {
                commit(types.REMOVE_CLASSROOM)
                dispatch('getSelf')
                // dispatch('getClassrooms')
                // dispatch('getChatrooms')
                // dispatch('getTasks')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    addChatroom({ commit, dispatch }, pk) {
        userApi.addChatroom(pk)
            .then((response) => {
                commit(types.ADD_CHATROOM)
                dispatch('getChatrooms')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    remChatroom({ commit, dispatch }, pk) {
        userApi.remChatroom(pk)
            .then((response) => {
                commit(types.REMOVE_CHATROOM)
                dispatch('getChatrooms')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    postMoment({ rootState, commit, dispatch }, formdata) {
        userApi.postMoment(formdata)
            .then((response) => {
                commit(types.POST_MOMENT)
                dispatch('getClassroomMoments', rootState.route.params.classroom_id)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    delMoment({ commit, dispatch }, pk) {
        userApi.delMoment(pk)
            .then((response) => {
                commit(types.REMOVE_MOMENT)
                // dispatch('getChatrooms')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
}

// mutations
const mutations = {
    // auth
    [types.LOGIN_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.login_status = true
        router.push('/')
    },
    [types.REGSITER_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.login_status = true
        router.push('/')
    },
    [types.LOGIN_FAILED](state, error) {
        state.login_status = false
        state.token = null
        state.error_msg = error
        router.push('/login')
    },
    [types.REGSITER_FAILED](state, error) {
        state.login_status = false
        state.token = null
        state.error_msg = error
    },
    [types.LOG_ERROR](state, error) {
        state.error_msg = error
        // TODO, need to handle errors
    },

    [types.VERIFY_SUCCESS](state, response) {
        state.token = response.token
        // state.login_status = true
    },

    [types.REFRESH_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        // state.login_status = true
    },

    // load data
    [types.LOAD_SELF](state, response) {
        state.user = response
        if (!state.user.avatar) {
            state.user.avatar = {
                avatar1x: default_avatar1x,
                avatar2x: default_avatar2x,
                avatar4x: default_avatar4x
            }
        }
    },
    [types.LOAD_CLASSROOMS](state, response) {
        state.classrooms = response
    },
    [types.LOAD_CHATROOMS](state, response) {
        state.chatrooms = response
    },
    [types.LOAD_FRIENDS](state, response) {
        state.friends = response
    },
    [types.LOAD_TASKS](state, response) {
        state.tasks = response
    },
    [types.LOAD_USER](state, response) {
        state.loaded_user = response
        if (!state.user.avatar) {
            state.user.avatar = {
                avatar1x: default_avatar1x,
                avatar2x: default_avatar2x,
                avatar4x: default_avatar4x
            }
        }
    },

    // post change
    [types.ADD_CLASSROOM](state) {},
    [types.POST_MOMENT](state) {
        // TODO, update only 1 moment
    },
    // [types.ADD_CLASSROOM_FAILED](state) {},

}

export default {
    state,
    getters,
    actions,
    mutations
}
