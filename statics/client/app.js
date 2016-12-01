import Vue from 'vue'
import {sync} from 'vuex-router-sync'
import App from './components/App'
import router from './router'
import store from './store'

sync(store, router)

const app = new Vue({
        el: '#app',
        data: {
            currentRoute: window.location.pathname
        },
        router,
        store,
        render: h = > h(App)
})

export {app, router, store}
