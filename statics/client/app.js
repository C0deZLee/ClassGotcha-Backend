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
    authToken: '',
    user: {}
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
      }
      console.log(this.authToken)
      this.$http.post('http://localhost:8000/account/login-verify/', formData).then(response => {
        // success
      }, response => {
        // console.log(response)
        // failed
        this.$router.push('/login')
      })
    },
    logout: function() {
      this.authToken = ''
      this.$cookie.delete('token')
    }
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