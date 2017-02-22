// vue
import Vue from 'vue'
import Vuex from 'vuex'
import PersistedState from 'vuex-persistedstate'
// utils
import * as types from './mutation-types'
import * as cookie from '../utils/cookie'
import router from '../router'
// import modules
import user from './modules/user'
import classroom from './modules/classroom'
import chat from './modules/chat'
import post from './modules/post'
import task from './modules/task'

Vue.use(Vuex)
const mutations = {
    [types.LOGOUT](state) {
        cookie.delCookie('token')
        state.user.classrooms = []
        state.user.chatrooms = []
        state.user.friends = []
        state.user.tasks = []
        state.user.login_status = false
        state.user.token = null
        state.chat.chatrooms = {}
        state.chat.valid = false
        state.chat.current_chatroom_pk = null
        state.chat.error_msg = null
        state.chat.sockets = {}
        state.classroom.search_results = []
        state.classroom.classroom = {}
        state.classroom.is_in_class = false
        state.classroom.notes = []
        state.classroom.students = []
        state.classroom.error_msg = ''
        router.push('/login')
    }
}
const store = new Vuex.Store({
    // if strict mode is true, then all state change must be triigered by mutations, otherwise compiler will throw error
    strict: false,
    plugins: [PersistedState()],
    // state,
    mutations,
    // actions
    modules: {
        user,
        classroom,
        chat,
        post,
        task
    }
})
export default store
