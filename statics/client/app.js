import Vue from 'vue'
import {
  sync
} from 'vuex-router-sync'
import Resource from 'vue-resource'
import Router from 'vue-router'
import App from './components/App'
import router from './router'
import store from './store'

Vue.use(Router)
Vue.use(Resource)

sync(store, router)

const app = new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname,
    authToken: ''
  },
  methods: {
    checkAuth: function() {
      const formData = {
        token: this.authToken
      }
      console.log(this.authToken)
      this.$http.post('http://localhost:8000/account/login-verify/', formData).then(response => {
        // success
      }, response => {
        // console.log(response)
        // failed
        this.$router.push('/login')

      })
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