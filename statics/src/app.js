import Vue from 'vue'
import Resource from 'vue-resource'
import Cookie from 'vue-cookie'
import Router from 'vue-router'

import router from './router'
import store from './store'
import { sync } from 'vuex-router-sync'

import App from 'views/components/App'
import * as cookie from './utils/cookie'

Vue.use(Router)
Vue.use(Resource)
Vue.use(Cookie)

sync(store, router)

// set csrf token for django
Vue.http.headers.common['X-CSRFToken'] = cookie.getCookie('csrftoken')

export const app = new Vue({
    el: '#app',
    data: {
        currentRoute: window.location.pathname,
    },
    mounted: function() {
        const formData = { token: cookie.getCookie('token') }
        console.log('tokenVerify', formData)
        this.$store.dispatch('tokenVerify', formData)
    },
    router,
    store,
    render: h => h(App)
})

// export {
//     app,
//     router,
//     store
// }
