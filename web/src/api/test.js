const SALT_WORK_FACTOR = "AAAA_BBBB_CCCC_DDDD"

function testMapReduce() {
    let data = [{time: 1, time2: 1}, {time: 1}, {time: 1}, {time: 1},]

    let total = data.map((x) => {
        return x.time
    }).reduce(
        (a, b) => {
            return a + b
        }
    )
    return total
}

// console.log(testMapReduce())

let CryptoJS = require("crypto-js")

function get_salt_pwd(pwd) {
    let keyHex = CryptoJS.enc.Utf8.parse(SALT_WORK_FACTOR);
    let encrypted = CryptoJS.DES.encrypt(pwd, keyHex, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}


console.log(get_salt_pwd("1234536"))