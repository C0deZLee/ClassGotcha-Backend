import { userApi } from '../../api/account'
import router from '../../router'
import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
// shape: [{ id, quantity }]
const state = {
    user: {},
    avatar: {},
    classrooms: [],
    chatrooms: [],
    friends: [],
    tasks: [],
    login_status: false,
    token: null
}

// getters
const getters = {
    login_status: state => state.login_status,
    userID: state => {
        if (state.login_status) {
            return state.user.id
        }
    },
    userFullName: state => {
        if (state.login_status) {
            return state.user.first_name + ' ' + state.user.last_name
        } else {
            return 'None'
        }
    },
    userAvatar1x: state => {
        if (state.login_status) {
            return state.avatar.avatar1x
        } else {
            return 'None'
        }
    },
    userClassrooms: state => {
        if (state.login_status) {
            return state.classrooms
        } else {
            return []
        }
    },
    userChatrooms: state => {
        if (state.login_status) {
            return state.chatrooms
        } else {
            return []
        }
    }

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
                dispatch('getAvatar')
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
    tokenVerify({ rootState, commit, dispatch }, formData) {
        userApi.tokenVerify(formData)
            .then((response) => {
                commit(types.VERIFY_SUCCESS, response)
                if (rootState.route.path === '/login' || rootState.route.path === '/register') {
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
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getAvatar({ commit }) {
        userApi.getAvatar()
            .then((response) => {
                commit(types.LOAD_AVATAR, response)
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
    getTasks({ commit }, products) {
        userApi.getTasks()
            .then((response) => {
                commit(types.LOAD_TASKS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    addClassroom({ commit, dispatch }, pk) {
        userApi.addClassroom(pk)
            .then((response) => {
                commit(types.ADD_CLASSROOM)
                dispatch('getClassrooms')
                dispatch('getChatrooms')
                dispatch('getTasks')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    delClassroom({ commit, dispatch }, pk) {
        userApi.delClassroom(pk)
            .then((response) => {
                commit(types.REMOVE_CLASSROOM)
                dispatch('getClassrooms')
                dispatch('getChatrooms')
                dispatch('getTasks')
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
    delChatroom({ commit, dispatch }, pk) {
        userApi.delChatroom(pk)
            .then((response) => {
                commit(types.REMOVE_CHATROOM)
                dispatch('getChatrooms')
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
    [types.LOGIN_FAILED](state, error) {
        state.login_status = false
        state.token = null
        state.error_msg = error
        router.push('/login')
    },
    [types.LOGOUT](state) {
        cookie.delCookie('token')
        state.classrooms = []
        state.chatrooms = []
        state.friends = []
        state.tasks = []
        state.login_status = false
        state.token = null
        router.push('/login')
    },
    [types.LOG_ERROR](state, error) {
        state.error_msg = error
        // TODO, need to handle errors
    },

    [types.VERIFY_SUCCESS](state, response) {
        state.token = response.token
        state.login_status = true
    },

    [types.VERIFY_FAILED](state, error) {
        cookie.delCookie('token')
        state.login_status = false
        state.token = null
        state.error_msg = error
        router.push('/login')
    },

    [types.REFRESH_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.login_status = true
    },

    [types.REFRESH_FAILED](state, response) {
        cookie.delCookie('token')
        state.login_status = false
        state.token = null
        state.error_msg = error
        router.push('/login')
    },
    // load data
    [types.LOAD_USER](state, response) {
        state.user = response
    },
    [types.LOAD_AVATAR](state, response) {
        state.avatar = response
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
    //post change
    [types.ADD_CLASSROOM](state) {},
    // [types.ADD_CLASSROOM_FAILED](state) {},

}

export default {
    state,
    getters,
    actions,
    mutations
}
