export const debugger = (value) => {
    if (process.env.NODE_ENV == 'development') {
        console.log(value)
    }
}
