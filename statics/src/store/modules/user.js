import { userApi } from '../../api/user-api'
import router from '../../router'
import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
// shape: [{ id, quantity }]
const state = {
    user: {},
    friends: [],
    pending_friends: [],
    moments: [],
    tasks: [],
    login_status: false,
    token: null,
    loaded_user: {},
    uploaded: null,
}

// getters
const getters = {
    login_status: state => state.login_status,
    me: state => {
        if (state.user && state.login_status)
            return state.user
        else return {}
    },
    userID: state => {
        if (state.user && state.login_status) {
            return state.user.id
        } else return {}
    },
    userFullName: state => {
        if (state.user && state.login_status) {
            return state.user.full_name
        } else {
            return ''
        }
    },
    userAvatar: state => {
        if (state.user && state.login_status) {
            return state.user.avatar
        } else {
            return ''
        }
    },
    userClassrooms: state => {
        if (state.user && state.login_status) {
            return state.user.classrooms
        } else {
            return []
        }
    },
    userChatrooms: state => {
        if (state.user && state.login_status) {
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
            return state.tasks
        } else {
            return []
        }
    },
    userRecommendedTasks: (state, getters) => {
        let tasks = []
        for (let i in getters.userTasks) {
            // Have to do this to avoid fucking stupid js optimize which only create an reference to the object.
            let task = Object.assign({}, getters.userTasks[i])
            /* global moment:true */
            if (task.category === 1) { // Homework
                const today = moment.utc().startOf('day')
                const due_date = moment.utc(task.end)
                const from_now_in_days = Math.round(moment.duration(due_date - today).asDays())
                if (from_now_in_days >= 0 && from_now_in_days <= 7) {
                    task.task_name = 'Do ' + task.task_name + ' of ' + task.classroom.class_short
                    tasks.push(task)
                }
            } else if (task.category === 2) { // Quiz
                const today = moment.utc().startOf('day')
                const due_date = moment.utc(task.end)
                const from_now_in_days = Math.round(moment.duration(due_date - today).asDays())
                if (from_now_in_days >= 0 && from_now_in_days <= 7) {
                    task.task_name = 'Prepare ' + task.task_name + ' of ' + task.classroom.class_short

                    tasks.push(task)
                }
            } else if (task.category === 3) { // Exam
                const today = moment.utc().startOf('day')
                const due_date = moment.utc(task.end)
                const from_now_in_days = Math.round(moment.duration(due_date - today).asDays())
                if (from_now_in_days >= 0 && from_now_in_days <= 10) {
                    task.task_name = 'Prepare ' + task.task_name + ' of ' + task.classroom.class_short
                    tasks.push(task)
                }
            }
        }
        return tasks
    },
    userFriends: state => {
        return state.friends
    },
    userPendingFriends: state => {
        return state.pending_friends
    },
    loadedUser: state => {
        return state.loaded_user
    }

}

// actions
const actions = {
    register({ commit, dispatch }, formData) {
        return userApi.register(formData)
            .then((response) => {
                commit(types.REGSITER_SUCCESS, response)
                dispatch('getSelf')
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
                dispatch('getTasks')
                dispatch('getFriends')
                dispatch('setSockets')
                router.push({ path: 'home' })

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
                if (rootState.route.name === 'login' || rootState.route.name === 'register' || rootState.route.name === 'landing') {
                    router.push({ path: 'home' })
                }
                dispatch('getSelf')
                dispatch('getTasks')

                dispatch('getFriends')
                dispatch('setSockets')
            })
            .catch((error) => {
                if (rootState.route.name !== 'register') {
                    dispatch('tokenRefresh', formData)
                }
                commit(types.LOG_ERROR, error)
            })
    },
    tokenRefresh({ rootState, commit, dispatch }, formData) {
        userApi.tokenRefresh(formData)
            .then((response) => {
                commit(types.REFRESH_SUCCESS, response)
                dispatch('getSelf')
                dispatch('getTasks')

                dispatch('getFriends')
                dispatch('setSockets')
            })
            .catch((error) => {
                if (rootState.route.name !== 'login' && rootState.route.name !== 'register' && rootState.route.name !== 'landing')
                    commit(types.LOGIN_FAILED)
                commit(types.LOG_ERROR, error)
            })
    },
    logout({ commit }) {
        commit(types.LOGOUT)
    },
    getSelf({ commit }) {
        return userApi.getSelf()
            .then((response) => {
                commit(types.LOAD_SELF, response)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject(error)
            })
    },
    updateSelf({ commit }, formData) {
        userApi.updateSelf(formData)
            .then(() => {
                commit(types.UPDATE_SELF)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    // getClassrooms({ commit }) {
    //     userApi.getClassrooms()
    //         .then((response) => {
    //             commit(types.LOAD_CLASSROOMS, response)
    //         })
    //         .catch((error) => {
    //             commit(types.LOG_ERROR, error)
    //         })
    // },
    // getChatrooms({ commit }) {
    //     userApi.getChatrooms()
    //         .then((response) => {
    //             commit(types.LOAD_CHATROOMS, response)
    //         })
    //         .catch((error) => {
    //             commit(types.LOG_ERROR, error)
    //         })
    // },
    getFriends({ commit }) {
        userApi.getFriends()
            .then((response) => {
                commit(types.LOAD_FRIENDS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
        userApi.getPendingFriends()
            .then((response) => {
                commit(types.LOAD_PENDING_FRIENDS, response)
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
                dispatch('getTasks')
                dispatch('setSockets')
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
                dispatch('getTasks')
                dispatch('setSockets')
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
    postMoment({ rootState, state, commit, dispatch }, formdata) {
        if (state.uploaded)
            formdata['file'] = state.uploaded
        return userApi.postMoment(formdata)
            .then((response) => {
                commit(types.POST_MOMENT)
                commit(types.CLEAR_FILE)
                dispatch('getClassroomMoments', rootState.route.params.classroom_id)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject()
            })
    },
    delMoment({ rootState, commit, dispatch }, pk) {
        userApi.delMoment(pk)
            .then((response) => {
                commit(types.REMOVE_MOMENT)
                dispatch('getClassroomMoments', rootState.route.params.classroom_id)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    addFriend({ commit }, pk) {
        userApi.addFriend(pk)
            .then(() => {
                commit(types.ADD_FRIEND)
            })
            .catch((error) => {
                console.log(error)
            })
    },
    remFriend({ commit }, pk) {
        userApi.remFriend(pk)
            .then(() => {
                commit(types.REMOVE_FRIEND)
            })
            .catch((error) => {
                console.log(error)
            })
    },
    acceptFriend({ commit }, pk) {
        return userApi.acceptFriend(pk)
            .then(() => {
                commit(types.ACCEPT_FRIEND)
                return Promise.resolve()
            })
            .catch((error) => {
                // console.log(error)
                return Promise.reject(error)
            })
    },
    uploadFile({ commit }, payload) {
        commit(types.UPLOAD_FILE, payload)
    },
    clearFile({ commit }) {
        commit(types.CLEAR_FILE)
    }
}

// mutations
const mutations = {
    // auth
    [types.LOGIN_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.login_status = true
        router.push({ name: 'home' })
    },
    [types.REGSITER_SUCCESS](state, response) {
        cookie.setCookie('token', response.token)
        state.token = response.token
        state.login_status = true
        router.push({ name: 'home' })
    },
    [types.LOGIN_FAILED](state, error) {
        state.login_status = false
        state.token = null
        state.error_msg = error
        router.push({ name: 'login' })
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
    [types.LOAD_PENDING_FRIENDS](state, response) {
        state.pending_friends = response
    },

    [types.LOAD_TASKS](state, response) {
        state.tasks = response
    },
    [types.LOAD_USER](state, response) {
        state.loaded_user = response
    },

    // post change
    [types.ADD_CLASSROOM](state) {},
    [types.POST_MOMENT](state) {},
    [types.REMOVE_MOMENT](state) {},
    [types.UPDATE_SELF](state) {},

    [types.ACCEPT_FRIEND](state) {},
    [types.ADD_FRIEND](state) {},
    [types.REMOVE_FRIEND](state) {},

    [types.UPLOAD_FILE](state, payload) {
        state.uploaded = payload
    },
    [types.CLEAR_FILE](state, payload) {
        state.uploaded = null
    },
    // [types.ADD_CLASSROOM_FAILED](state) {},

}

export default {
    state,
    getters,
    actions,
    mutations
}
