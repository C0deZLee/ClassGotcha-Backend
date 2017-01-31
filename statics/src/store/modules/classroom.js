import classApi from '../../api/classroom-api'
// import router from '../../router'
// import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

import default_avatar1x from 'img/default-avatar1x.png'
import default_avatar2x from 'img/default-avatar2x.png'
import default_avatar4x from 'img/default-avatar4x.png'

// initial state
const state = {
    search_results: [],
    classroom: {
        class_number: '',
        id: null,
        chatroom: null,
        created: '',
        groups: [],
        description: '',
        class_short: '',
        class_room: '',
        class_credit: '',
        class_name: '',
        class_time: {
            formatted_end_time: '',
            formatted_start_time: '',
            location: null,
            repeat_list: [],
            task_name: '',
            type: 0
        },
        class_code: '',
        class_section: '',
        major: {
            id: null,
            major_college: '',
            major_full: '',
            major_icon: null,
            major_short: '',
        },
        professors: [],
        semester: {
            formatted_end_date: '',
            formatted_start_date: '',
            name: ''
        },
        students: [],
        students_count: 0,
        syllabus: null,
        tasks: [],
        updated: '',
    },
    is_in_class: false,
    moments: [],
    notes: [],
    tasks: [],
    error_msg: ''
}

// getters
const getters = {
    classSearchResults: (state) => {
        return state.search_results
    },
    currentClassroom: (state) => {
        return state.classroom
    },
    userInClassroom: (state) => {
        return state.is_in_class
    },
    classroomMoments: (state) => {
        return state.moments
    },
    classroomTasks: (state) => {
        if (state.classroom)
            return state.classroom.tasks
        else
            return []
    },
    classroomProfessors: (state) => {
        if (state.classroom)
            return state.classroom.professors
        else
            return []

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
    getClassroom({ rootState, commit, dispatch }, pk) {
        classApi.getClassroom(pk)
            .then((response) => {
                commit(types.GET_CLASSROOM, response)
                let not_in_class = true
                // If user in classroom's student list, commit USER_IN_CLASSROOM
                for (let i in response.students) {
                    if (response.students[i].id === rootState.user.user.id) {
                        commit(types.USER_IN_CLASSROOM)
                        not_in_class = false
                    }
                }
                // If user not in classroom's student list, commit USER_NOT_IN_CLASSROOM
                if (not_in_class) {
                    commit(types.USER_NOT_IN_CLASSROOM)
                }
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getClassroomMoments({ commit, dispatch }, pk) {
        classApi.getMoments(pk)
            .then((response) => {
                commit(types.LOAD_CLASSROOM_MOMENTS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getClassroomTasks({ commit, dispatch }, pk) {
        classApi.getTasks(pk)
            .then((response) => {
                commit(types.LOAD_CLASSROOM_TASKS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    postClassroomTask({ commit, dispatch }, data) {
        classApi.postTask(data.pk, data.formData)
            .then((response) => {
                commit(types.POST_CLASSROOM_TASK, response)
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
    [types.GET_CLASSROOM](state, response) {
        state.classroom = response
        for (let i in state.classroom.students) {
            if (!state.classroom.students[i].avatar) {
                state.classroom.students[i].avatar = {
                    avatar1x: default_avatar1x,
                    avatar2x: default_avatar2x,
                    avatar4x: default_avatar4x
                }
            }
        }
    },
    [types.USER_IN_CLASSROOM](state) {
        state.is_in_class = true
    },
    [types.USER_NOT_IN_CLASSROOM](state) {
        state.is_in_class = false
    },
    [types.LOAD_CLASSROOM_MOMENTS](state, response) {
        state.moments = response
        for (let i in state.moments) {
            if (!state.moments[i].creator.avatar) {
                state.moments[i].creator.avatar = {
                    avatar1x: default_avatar1x,
                    avatar2x: default_avatar2x,
                    avatar4x: default_avatar4x
                }
            }
            for (let j in state.moments[i].comments) {
                if (!state.moments[i].comments[j].creator.avatar) {
                    state.moments[i].comments[j].creator.avatar = {
                        avatar1x: default_avatar1x,
                        avatar2x: default_avatar2x,
                        avatar4x: default_avatar4x
                    }
                }
            }
        }
    },
    [types.POST_CLASSROOM_TASK](state, response) {},
    [types.LOG_ERROR](state, error) {
        state.error_msg = error
        console.log(error)
        // TODO, need to handle errors
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}
