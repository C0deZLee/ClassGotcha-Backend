export const API_ROOT = (process.env.NODE_ENV === 'production') ?
    'http://api.classgotcha.com/' :
    'http://localhost:8000/'

export const WS_ROOT = (process.env.NODE_ENV === 'production') ?
    'ws://api.classgotcha.com/' :
    'ws://localhost:8000/'

export const COOKIE_DOMAIN = (process.env.NODE_ENV === 'production') ?
    'classgotcha.com' :
    'localhost'

// cookie expired in 1 day
// Options: '1Y' '1M' '1D' '1h' '1m' '1s'
export const COOKIE_EXPIRE = 1
