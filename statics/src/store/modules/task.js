import taskApi from '../../api/task-api'
import * as types from '../mutation-types'

const actions = {
    updateTask({ commit, dispatch }, data) {
        taskApi.updateTask(data.pk, data.formData)
            .then((response) => {
                commit(types.UPDATE_TASK, response)
                dispatch('getClassroomMoments')
                dispatch('getClassroomTasks')
            })
            .catch((error) => {
                console.log(error)
            })
    },
    deleteTask({ commit, dispatch }, pk) {
        taskApi.deleteTask(pk)
            .then((response) => {
                commit(types.DELETE_TASK, response)
                dispatch('getClassroomTasks')
            })
            .catch((error) => {
                console.log(error)
            })
    },
}

const mutations = {
    [types.UPDATE_TASK](state, response) {},
    [types.DELETE_TASK](state, response) {},
}

export default {
    actions,
    mutations
}
