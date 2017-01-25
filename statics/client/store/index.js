import Vue from 'vue'
import Vuex from 'vuex'
import PersistedState from 'vuex-persistedstate'

import user from './modules/user'
import classroom from './modules/classroom'

Vue.use(Vuex)

const isDebug = process.env.NODE_ENV !== 'production'


const store = new Vuex.Store({
    // if strict mode is true, then all state change must be triigered by mutations, otherwise compiler will throw error
    strict: isDebug,
    plugins: [PersistedState()],
    // state,
    // mutations,
    // actions
    modules: {
        user,
        classroom
    }
})
export default store
