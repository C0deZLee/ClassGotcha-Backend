import Vue from 'vue'
import {
  sync
} from 'vuex-router-sync'
import Resource from 'vue-resource'
import Cookie from 'vue-cookie'
import Router from 'vue-router'
import App from './components/App'
import router from './router'
import store from './store'

Vue.use(Router)
Vue.use(Resource)
Vue.use(Cookie)

sync(store, router)

const app = new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname,
    apiEndPoint: 'http://localhost:8000',
    socketApiEndPoint: 'ws://localhost:8000',
    authToken: '',
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
      }, response => {
        // failed
        this.logout()
      })
    },
    logout: function() {
      this.authToken = ''
      this.$cookie.delete('token')
      this.$router.push('/login')
    }
  },
  mounted: function() {
    this.checkAuth()
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