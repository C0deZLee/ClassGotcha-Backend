import postApi from '../../api/posts'
// import router from '../../router'
// import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
// shape: [{ id, quantity }]
const state = {
    error_msg: ''
}

// getters
const getters = {}

// actions
const actions = {
    solveMoment({ commit, dispatch }, pk) {
        postApi.solve(pk)
            .then((response) => {
                commit(types.ADD_MOMENT_SOLVE, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    postMomentComment({ rootState, commit, dispatch }, data) {
        postApi.postComment(data.id, data.formData)
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
                commit(types.ADD_MOMENT_LIKE, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },

}

// mutations
const mutations = {
    [types.ADD_MOMENT_SOLVE](state, response) {},
    [types.ADD_MOMENT_LIKE](state, response) {},
    [types.POST_MOMENT_COMMENT](state, response) {},
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
