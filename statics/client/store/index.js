import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'

Vue.use(Vuex)

const isDebug = process.env.NODE_ENV !== 'production'


const store = new Vuex.Store({
    // if strict mode is true, then all state change must be triigered by mutations, otherwise compiler will throw error
    strict: isDebug,
    // state,
    // mutations,
    // actions
    modules: {
        user
    }
})
export default store
