import Vue from 'vue'
import Cookie from 'vue-cookie'
import { COOKIE_DOMAIN, COOKIE_EXPIRE } from '../config.js'

Vue.use(Cookie)

let cookieConfig = {}
if (COOKIE_DOMAIN !== '' && COOKIE_EXPIRE !== '') {
    cookieConfig = { domain: COOKIE_DOMAIN, expires: COOKIE_EXPIRE }
}

export function setCookie(name, value) {
    Vue.cookie.set(name, value, cookieConfig)
}

export function getCookie(name) {
    return Vue.cookie.get(name)
}

export function delCookie(name) {
    Vue.cookie.delete(name)
}
