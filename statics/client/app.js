import Vue from 'vue'
import Resource from 'vue-resource'
import Cookie from 'vue-cookie'
import Router from 'vue-router'

import router from './router'
import store from './store'
import { sync } from 'vuex-router-sync'

import App from './views/components/App'
import * as cookie from './utils/cookie'

Vue.use(Router)
Vue.use(Resource)
Vue.use(Cookie)

sync(store, router)

// set csrf token for django  
const csrftoken = Cookies.get('csrftoken')
Vue.http.headers.common['X-CSRFToken'] = csrftoken

const app = new Vue({
    el: '#app',
    data: {
        currentRoute: window.location.pathname,
        apiEndPoint: 'http://localhost:8000',
        socketApiEndPoint: 'ws://localhost:8000',
        authToken: '',
        avatar: {},
        user: {},
        classrooms: {},
        chatrooms: {}
    },
    methods: {
        checkAuth: function() {
            let formData = {}
            if (this.authToken) {
                formData = {
                    token: this.authToken
                }
            } else {
                formData = {
                    token: this.$cookie.get('token')
                }
                this.authToken = this.$cookie.get('token')
            }
            this.$http.post(this.$root.apiEndPoint + '/account/login-verify/', formData).then(response => {
                // success
                // load user data
                this.$http.get(this.$root.apiEndPoint + '/account/me/', {
                    headers: {
                        Authorization: 'JWT ' + this.$root.authToken
                    }
                }).then(response => {
                    this.$root.user = response.data
                })
                // load user class
                this.$http.get(this.$root.apiEndPoint + '/account/classrooms/', {
                    headers: {
                        Authorization: 'JWT ' + this.$root.authToken
                    }
                }).then(response => {
                    this.$root.classrooms = response.data
                })
                // load user chatrooms
                this.$http.get(this.$root.apiEndPoint + '/account/chatrooms/', {
                    headers: {
                        Authorization: 'JWT ' + this.$root.authToken
                    }
                }).then(response => {
                    this.$root.chatrooms = response.data
                    console.log(response.data)
                })
                // load user avatar
                this.$http.get(this.$root.apiEndPoint + '/account/avatar/', {
                    headers: {
                        Authorization: 'JWT ' + this.$root.authToken
                    }
                }).then(response => {
                    console.log(response)
                    this.$root.avatar = {
                        avatar4x: response.data.avatar4x,
                        avatar2x: response.data.avatar2x,
                        avatar1x: response.data.avatar1x
                    }
                })
            }, response => {
                // failed
                this.logout()
            })
        },
        logout: function() {
            this.$store.dispatch('logout')
        }
    },
    mounted: function() {
        const formData = { token: cookie.getCookie('token') }
        this.$store.dispatch('tokenVerify', formData)
    },
    router,
    store,
    render: h => h(App)
})

export {
    app,
    router,
    store
}
