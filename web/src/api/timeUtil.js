export function getDateY_M_D() {
    let date = new Date()
    return fmtDateY_M_D(date)
}

export function fmtDateY_M_D(date) {
    let char = '-'
    let year = date.getFullYear()
    let month = date.getMonth() + 1
    let strDate = date.getDate()

    if (month >= 1 && month <= 9) {
        month = '0' + month
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = '0' + strDate
    }
    return year + char + month + char + strDate
}

// console.log(getDateYMD())