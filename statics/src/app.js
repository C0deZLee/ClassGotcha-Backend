import Vue from 'vue'
import Resource from 'vue-resource'
import Router from 'vue-router'
import Mask from 'v-mask'
import { sync } from 'vuex-router-sync'

import router from './router'
import store from './store'

import App from 'views/components/App'
import * as cookie from './utils/cookie'

Vue.use(Router)
Vue.use(Resource)
Vue.use(Mask)

sync(store, router)

// set csrf token for django
Vue.http.headers.common['X-CSRFToken'] = cookie.getCookie('csrftoken')

export const app = new Vue({
    el: '#app',
    data: {},
    beforeCreate() {
        const formData = { token: cookie.getCookie('token') }
        this.$store.dispatch('tokenVerify', formData)
        /* global Array:true Object:true */
        // add includes function to array
        if (!Array.prototype.includes) {
            Object.defineProperty(Array.prototype, 'includes', {
                value: function(searchElement, fromIndex) {
                    if (this == null)
                        throw new TypeError('"this" is null or not defined')
                    var o = Object(this)
                    var len = o.length >>> 0
                    if (len === 0) return false
                    var n = fromIndex | 0
                    var k = Math.max(n >= 0 ? n : len - Math.abs(n), 0)
                    while (k < len) {
                        if (o[k] === searchElement)
                            return true
                        k++
                    }
                    return false
                }
            })
        }

    },
    router,
    store,
    components: { App }
})
