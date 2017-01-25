import classApi from '../../api/classroom'
import router from '../../router'
import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

// initial state
// shape: [{ id, quantity }]
const state = {
    search_results: [],
    classroom: {},
    is_in_class: false,
    notes: [],
    students: [],
    error_msg: ''
}

// getters
const getters = {
    classSearchResults: (state) => {
        return state.search_results
    }
}

// actions
const actions = {
    classroomSearch({ commit, dispatch }, formData) {
        classApi.search(formData)
            .then((response) => {
                commit(types.SEARCH_CLASSROOMS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },


}

// mutations
const mutations = {
    [types.SEARCH_CLASSROOMS](state, response) {
        state.search_results = response
    },

    [types.LOG_ERROR](state, error) {
        state.error_msg = error
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}
