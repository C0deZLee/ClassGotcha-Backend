import Vue from 'vue'
import {
  sync
} from 'vuex-router-sync'
import Resource from 'vue-resource'
import Router from 'vue-router'
import App from './components/App'
import router from './router'
import store from './store'

// Vue.use(Resource)
// Vue.use(Router)

sync(store, router)

const app = new Vue({
  el: '#app',
  /*  data: () => {
    return {
      currentRoute: window.location.pathname,
      authToken: '123'
    }
  },*/
  data: {
    currentRoute: window.location.pathname,
    authToken: ''
  },
  methods: {
    checkAuth: () => {
      const formData = {
        token: this.authToken
      }
      console.log(this.authToken)
      this.$http.post('http://localhost:8000/account/login-verify/', formData).then(response => {
        // success
        // this.$router.push('/')
        console.log(response)
      }, response => {
        console.log(response)
        // failed
        // this.errorMsg = response.data.non_field_errors[0]
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