import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'

import AuthLayout from 'components/AuthLayout'
import DefaultLayout from 'components/DefaultLayout'

import Home from 'views/Home'
import AddClassroom from 'views/AddClassroom'
import Classroom from 'views/Classroom'
import Register from 'views/Register'
import Login from 'views/Login'
import Upload from 'views/Upload'
import Chat from 'views/Chat'
import Notes from 'views/Notes'
import ClassroomList from 'views/ClassroomList'
import Page404 from 'views/404'
import Page403 from 'views/403'

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
            component: ClassroomList
        }, {
            path: '/classroom/add',
            component: AddClassroom
        }, {
            path: '/classroom/id/:classroom_id',
            //  access anywhere in the vm with this.$route.params.classroom_id
            component: Classroom
        }, {
            path: '/classroom/id/:classroom_id/notes',
            //  access anywhere in the vm with this.$route.params.classroom_id
            component: Notes
        }, {
            path: '/',
            component: Home
        }, {
            path: '/upload',
            component: Upload
        }, {
            path: '/chatroom/id/:chatroom_id',
            component: Chat
        }, {
            path: '/404',
            component: Page404
        }, {
            path: '/403',
            component: Page403
        }]
    }]
})
