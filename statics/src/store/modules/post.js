import postApi from '../../api/post-api'

import * as types from '../mutation-types'

// initial state
const state = {
    posts: [],
    current_post: {},
    error_msg: ''
}

// getters
const getters = {
    posts(state) {
        return state.posts
    },
    currentPost(state) {
        return state.current_post
    }
}

// actions
const actions = {
    solveMoment({ rootState, commit, dispatch }, pk) {
        postApi.solveMoment(pk)
            .then((response) => {
                commit(types.ADD_MOMENT_SOLVE, response)
                dispatch('getClassroomMoments', rootState.route.params.classroom_id)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    reportMoment({ commit, dispatch }, pk) {
        postApi.addReport(pk)
            .then((response) => {
                commit(types.ADD_MOMENT_REPORT, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    postMomentComment({ rootState, state, commit, dispatch }, data) {
        postApi.postMomentComment(data.id, data.formData)
            .then((response) => {
                commit(types.POST_MOMENT_COMMENT, response)
                // TODO: need optimize, only update 1 moment, not whole classroom's moment
                dispatch('getClassroomMoments', rootState.route.params.classroom_id)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    addMomentLike({ commit, dispatch }, pk) {
        postApi.addLike(pk)
            .then((response) => {
                commit(types.POST_CLASSROOM_TASK, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },

    getPosts({ rootState, commit, dispatch }) {
        return postApi.getPosts()
            .then((response) => {
                commit(types.LOAD_POSTS, response)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject()
            })
    },
    getPost({ rootState, commit, dispatch }, pk) {
        return postApi.getPost(pk)
            .then((response) => {
                commit(types.LOAD_POST, response)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject()
            })
    },

    postPost({ commit, dispatch }, formData) {
        postApi.postPost(formData)
            .then((response) => {
                commit(types.POST_POST, response)
                dispatch('getPosts')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    postPostComment({ rootState, state, commit, dispatch }, data) {
        postApi.postPostComment(data.id, data.formData)
            .then((response) => {
                commit(types.POST_MOMENT_COMMENT, response)
                dispatch('getPost', data.id)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    addPostVote({ commit, dispatch }, data) {
        postApi.addPostVote(data.id, data.formData)
            .then((response) => {
                commit(types.ADD_POST_VOTE, response)
                dispatch('getPosts')
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    }

}

// mutations
const mutations = {
    [types.POST_POST](state, response) {},
    [types.LOAD_POSTS](state, response) {
        state.posts = response
    },
    [types.LOAD_POST](state, response) {
        state.current_post = response
    },
    [types.POST_POST_COMMENT](state, response) {},
    [types.ADD_POST_VOTE](state, response) {},


    [types.ADD_MOMENT_SOLVE](state, response) {},
    [types.ADD_MOMENT_LIKE](state, response) {},
    [types.ADD_MOMENT_REPORT](state, response) {},

    [types.POST_MOMENT_COMMENT](state, response) {},
    [types.POST_CLASSROOM_TASK](state, response) {},

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
