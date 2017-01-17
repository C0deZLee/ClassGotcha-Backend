import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'

import AuthLayout from '../components/AuthLayout'
import DefaultLayout from '../components/DefaultLayout'

import Home from '../views/Home'
import Classroom from '../views/Classroom'
import Register from '../views/Register'
import Login from '../views/Login'
import Upload from '../views/Upload'
import Chat from '../views/Chat'

Vue.use(Router)
Vue.use(Resource)

export default new Router({
  mode: 'hash',
  routes: [{
    // use auth layout
    path: '/auth',
    component: AuthLayout,
    children: [{
      path: '/login',
      component: Login
    }, {
      path: '/register',
      component: Register
    }]
  }, {
    // use default layout
    path: '/',
    component: DefaultLayout,
    children: [{
      path: '/classroom',
      component: Classroom
    }, {
      path: '',
      component: Home
    }, {
      path: '/upload',
      component: Upload
    }, {
      path: '/chat',
      component: Chat
    }]
  }]
})