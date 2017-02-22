import classApi from '../../api/classroom-api'
// import router from '../../router'
// import * as cookie from '../../utils/cookie'
import * as types from '../mutation-types'

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
        updated: '',
    },
    is_in_class: false,
    moments: [],
    notes: [],
    tasks: [],
    majors: [],
    error_msg: ''
}

// getters
const getters = {
    classSearchResults: (state) => {
        return state.search_results
    },
    majors: (state) => {
        return state.majors
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
        let tasks = []
        for (let i in state.tasks) {
            if (state.tasks[i].repeat_list.length) {
                const repeat_list = state.tasks[i].repeat_list
                for (let j in repeat_list) {
                    // http://momentjs.com/docs/#/get-set/day/
                    /* global moment:true */
                    const date = moment().day(repeat_list[j] + 7).format('YYYY-MM-DDT')
                    if (state.tasks[i].start)
                        state.tasks[i].start = date + moment.utc(state.tasks[i].start).format('HH:mm:ss')
                    state.tasks[i].end = date + moment.utc(state.tasks[i].end).format('HH:mm:ss')
                    tasks.push(state.tasks[i])
                }
            } else if (!state.tasks[i].expired) {
                tasks.push(state.tasks[i])
            }
        }
        // js sort method
        tasks.sort((a, b) => {
            return new Date(a.end) - new Date(b.end)
        })
        return tasks
    },
    currentClassroomNotes: (state) => {
        return state.notes
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
        return classApi.search(formData)
            .then((response) => {
                commit(types.SEARCH_CLASSROOMS, response)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject()
            })
    },
    getMajors({ commit, dispatch }) {
        return classApi.getMajors()
            .then((response) => {
                commit(types.LOAD_CLASSROOM_MAJORS, response)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject()
            })
    },
    getClassroom({ rootState, commit, dispatch }, pk) {
        classApi.getClassroom(pk)
            .then((response) => {
                commit(types.GET_CLASSROOM, response)
                dispatch('getClassroomMoments', pk)
                dispatch('getClassroomTasks', pk)

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
    getClassroomMoments({ state, commit, dispatch }, pk) {
        classApi.getMoments(state.classroom.id)
            .then((response) => {
                commit(types.LOAD_CLASSROOM_MOMENTS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getClassroomTasks({ state, commit, dispatch }, pk) {
        classApi.getTasks(state.classroom.id)
            .then((response) => {
                commit(types.LOAD_CLASSROOM_TASKS, response)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    getClassroomNotes({ commit, dispatch }, pk) {
        return classApi.getNotes(pk)
            .then((response) => {
                commit(types.LOAD_CLASSROOM_NOTES, response)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject(error)
            })
    },
    postClassroomTask({ commit, dispatch }, data) {
        classApi.postTask(data.pk, data.formData)
            .then((response) => {
                commit(types.POST_CLASSROOM_TASK, response)
                dispatch('getClassroomTasks', data.pk)
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
            })
    },
    postClassroomNote({ commit, dispatch }, data) {
        console.log('store.module.classroom.postClassroomNote', data)
        return classApi.postNote(data.pk, data.formData)
            .then((response) => {
                commit(types.POST_CLASSROOM_TASK, response)
                dispatch('getClassroomNotes', data.pk)
                return Promise.resolve()
            })
            .catch((error) => {
                commit(types.LOG_ERROR, error)
                return Promise.reject(error)
            })
    }
}

// mutations
const mutations = {
    [types.SEARCH_CLASSROOMS](state, response) {
        state.search_results = response
    },
    [types.LOAD_CLASSROOM_MAJORS](state, response) {
        state.majors = response
    },
    [types.GET_CLASSROOM](state, response) {
        state.classroom = response
    },
    [types.USER_IN_CLASSROOM](state) {
        state.is_in_class = true
    },
    [types.USER_NOT_IN_CLASSROOM](state) {
        state.is_in_class = false
    },
    [types.LOAD_CLASSROOM_MOMENTS](state, response) {
        state.moments = response
    },
    [types.LOAD_CLASSROOM_TASKS](state, response) {
        state.tasks = response
    },
    [types.POST_CLASSROOM_TASK](state, response) {},
    [types.LOAD_CLASSROOM_NOTES](state, response) {
        state.notes = response
    },
    [types.POST_CLASSROOM_NOTE](state, response) {},

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
