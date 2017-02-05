import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'

import AuthLayout from 'components/AuthLayout'
import DefaultLayout from 'components/DefaultLayout'

import Home from 'views/Home'
import AddClassroom from 'views/AddClassroom'
import Classroom from 'views/Classroom'
import ClassroomStudents from 'views/ClassroomStudents'
import Register from 'views/Register'
import Login from 'views/Login'
import Profile from 'views/Profile'
import Chat from 'views/Chat'
import Notes from 'views/Notes'
import Page404 from 'views/404'
import Page403 from 'views/403'
import Professor from 'views/Professor'

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
            component: Login,
            name: 'login'
        }, {
            path: '/register',
            component: Register,
            name: 'register'
        }]
    }, {
        // use default layout
        path: '/',
        component: DefaultLayout,
        children: [{
            path: '/classroom/add',
            component: AddClassroom,
            name: 'classroom_add'
        }, {
            path: '/classroom/id/:classroom_id',
            //  access anywhere in the vm with this.$route.params.classroom_id
            component: Classroom,
            name: 'classroom'
        }, {
            path: '/classroom/id/:classroom_id/files',
            //  access anywhere in the vm with this.$route.params.classroom_id
            component: Notes,
            name: 'classroom_files'
        }, {
            path: '/classroom/id/:classroom_id/students',
            //  access anywhere in the vm with this.$route.params.classroom_id
            component: ClassroomStudents,
            name: 'classroom_students'
        }, {
            path: '/',
            component: Home,
            name: 'home'
        }, {
            path: '/chatroom/id/:chatroom_id',
            component: Chat,
            name: 'chat'
        }, {
            path: '/404',
            component: Page404,
            name: '404'
        }, {
            path: '/403',
            component: Page403,
            name: '403'
        }, {
            path: '/profile/id/:user_id',
            component: Profile,
            name: 'user'
        }, {
            path: '/professor/id/:professor_id',
            component: Professor,
            name: 'professor'
        }]
    }]
})
