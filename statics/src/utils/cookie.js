import Cookie from 'js-cookie'
import { COOKIE_EXPIRE } from '../config.js'


let cookieConfig = {}
if (COOKIE_EXPIRE !== '') {
    cookieConfig = { expires: COOKIE_EXPIRE }
}

export const setCookie = (name, value) => {
    Cookie.set(name, value, cookieConfig)
}

export const getCookie = (name) => {
    if (Cookie.get(name))
        return Cookie.get(name)
    else return 'None'
}

export const delCookie = (name) => {
    Cookie.remove(name)
}
