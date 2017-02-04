/** 
 *  Format time
 */
export const formatDate = (time, type = 1) => {
    let tmpDate = new Date(time)
    let year = tmpDate.getFullYear()
    let month = tmpDate.getMonth() + 1
    let day = tmpDate.getDate()
    let hours = tmpDate.getHours()
    let minutes = tmpDate.getMinutes()

    if (month === 1) {
        month = 'Jan.'
    } else if (month === 2) {
        month = 'Feb.'
    } else if (month === 3) {
        month = 'Mar.'
    } else if (month === 4) {
        month = 'Apr.'
    } else if (month === 5) {
        month = 'May.'
    } else if (month === 6) {
        month = 'Jun.'
    } else if (month === 7) {
        month = 'Jul.'
    } else if (month === 8) {
        month = 'Aug.'
    } else if (month === 9) {
        month = 'Sep.'
    } else if (month === 10) {
        month = 'Oct.'
    } else if (month === 11) {
        month = 'Nov.'
    } else if (month === 12) {
        month = 'Dec.'
    }
    if (type === 1)
        return year + '.' + month + '.' + day + ' ' + hours + ':' + minutes
    else if (type === 2)
        return month + ' ' + day + ', ' + year
    else if (type === 3)
        return month + ' ' + day
}


export const customTime = item => {
    let nowTime = new Date().getTime()
    let minuteTime = 60 * 1000
    let hourTime = 60 * minuteTime
    let dayTime = 24 * hourTime
    let monthTime = dayTime * 30
    let yearTime = monthTime * 12

    let publishTime = new Date(item).getTime()
    let historyTime = parseInt(nowTime) - parseInt(publishTime)
    let descTime
    if (historyTime >= yearTime) {
        // Count in year
        descTime = formatDate(publishTime, 2)

        // const year = parseInt(historyTime / yearTime)
        // if (year > 1)
        //     descTime = year + ' years ago'
        // else
        //     descTime = year + ' year ago'
    } else if (historyTime < yearTime && historyTime >= monthTime) {
        // Count in month
        descTime = formatDate(publishTime, 2)

        // const mouth = parseInt(historyTime / monthTime)
        // if (mouth > 1)
        //     descTime = mouth + ' mouths ago'
        // else
        //     descTime = mouth + ' mouth ago'
    } else if (historyTime < monthTime && historyTime >= dayTime) {
        // Count in day
        const day = parseInt(historyTime / dayTime)
        if (day > 1)
            // descTime = day + ' days ago'
            descTime = formatDate(publishTime, 2)
        else
            descTime = day + ' day ago'
    } else if (historyTime < dayTime && historyTime >= hourTime) {
        // Count in hour
        const hour = parseInt(historyTime / hourTime)
        if (hour > 1)
            descTime = hour + ' hours ago'
        else
            descTime = hour + ' hour ago'
    } else if (historyTime < hourTime && historyTime >= minuteTime) {
        // Count in minute
        const min = parseInt(historyTime / minuteTime)
        if (min > 1)
            descTime = min + ' minutes ago'
        else
            descTime = min + ' minute ago'
    } else {
        descTime = 'Just now'
    }
    return descTime
}

export const toTimezoneOffsetString = time => {
    const now = new Date()
    const tzo = -now.getTimezoneOffset()
    const dif = tzo >= 0 ? '+' : '-'
    const pad = num => {
        var norm = Math.abs(Math.floor(num))
        return (norm < 10 ? '0' : '') + norm
    }
    return time.getFullYear() +
        '-' + pad(time.getMonth() + 1) +
        '-' + pad(time.getDate()) +
        'T' + pad(time.getHours()) +
        ':' + pad(time.getMinutes()) +
        ':' + pad(time.getSeconds()) +
        dif + pad(tzo / 60) +
        ':' + pad(tzo % 60)
}

export const toUtcString = time => {
    const pad = num => {
        var norm = Math.abs(Math.floor(num))
        return (norm < 10 ? '0' : '') + norm
    }
    return time.getFullYear() +
        '-' + pad(time.getMonth() + 1) +
        '-' + pad(time.getDate()) +
        'T' + pad(time.getHours()) +
        ':' + pad(time.getMinutes()) +
        ':' + pad(time.getSeconds())
}
