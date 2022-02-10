import CryptoJS from "crypto-js";
import Axios from "axios";
import {SALT_WORK_FACTOR} from "@/api/config";

export function get_salt_pwd(pwd) {
    // todo 密码明文
    let keyHex = CryptoJS.enc.Utf8.parse(SALT_WORK_FACTOR);
    let encrypted = CryptoJS.DES.encrypt(pwd, keyHex, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}

export function detectOS() {
    let sUserAgent = navigator.userAgent;
    let isWin = (navigator.platform == "Win32") || (navigator.platform == "Windows");
    let isMac = (navigator.platform === "Mac68K") || (navigator.platform == "MacPPC") || (navigator.platform == "Macintosh") || (navigator.platform == "MacIntel");
    if (isMac) return "Mac";
    let isUnix = (navigator.platform == "X11") && !isWin && !isMac;
    if (isUnix) return "Unix";
    let isLinux = (String(navigator.platform).indexOf("Linux") > -1);
    if (isLinux) return "Linux";
    if (isWin) {
        let isWin2K = sUserAgent.indexOf("Windows NT 5.0") > -1 || sUserAgent.indexOf("Windows 2000") > -1;
        if (isWin2K) return "Win2000";
        let isWinXP = sUserAgent.indexOf("Windows NT 5.1") > -1 || sUserAgent.indexOf("Windows XP") > -1;
        if (isWinXP) return "WinXP";
        let isWin2003 = sUserAgent.indexOf("Windows NT 5.2") > -1 || sUserAgent.indexOf("Windows 2003") > -1;
        if (isWin2003) return "Win2003";
        let isWinVista = sUserAgent.indexOf("Windows NT 6.0") > -1 || sUserAgent.indexOf("Windows Vista") > -1;
        if (isWinVista) return "WinVista";
        let isWin7 = sUserAgent.indexOf("Windows NT 6.1") > -1 || sUserAgent.indexOf("Windows 7") > -1;
        if (isWin7) return "Win7";
    }
    return "other";
}

export function isApp() {
    if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
        //alert(navigator.userAgent);
        alert('这是IOS');
    } else if (/(Android)/i.test(navigator.userAgent)) {
        //alert(navigator.userAgent);
        alert('这是Android');
    } else {
        alert('这是PC');
    }
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

export function getDateY_M_D() {
    let date = new Date()
    return fmtDateY_M_D(date)
}

export const get = (url, params) => {
    return Axios({
        method: 'get',
        url: url,
        params: params
    })
};
export const get2 = (url, id, params) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'get',
        url: url + "/" + id,
        params: params
    })
};
export const postJson = (url, data = {}) => {
    return Axios({
        method: 'POST',
        url,
        data: data
    })
};
export const postJson2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'POST',
        url: url + "/" + id,
        data: data
    })
};
export const putJson = (url, data = {}) => {
    return Axios({
        method: 'PUT',
        url,
        data: data
    })
};
export const putJson2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'PUT',
        url: url + "/" + id,
        data: data
    })
};
export const deleteJson = (url, data = {}) => {
    return Axios({
        method: 'DELETE',
        url,
        data: data
    })
};
export const deleteJson2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'DELETE',
        url: url + "/" + id,
        data: data
    })
};
export const postForm = (url, data = {}) => {
    return Axios({
        method: 'POST',
        url,
        data: data,
        headers: {
            'Content-Type': 'multipart/form-data;'
        }
    })
};
export const postForm2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'POST',
        url: url + "/" + id,
        data: data,
        headers: {
            'Content-Type': 'multipart/form-data;'
        }
    })
};
export const ppJson = (url, id, data) => {
    if (typeof (id) == "undefined" || id == null) {
        return postJson2(url, 0, data)
    }
    return putJson2(url, id, data)
};

export async function querySearch(queryString, cb, url) {
    let data = {name: queryString}
    let res = await get2(url, 0, data)
    let suggest = []
    for (let i = 0; i < res.data.data.length; i++) {
        suggest.push({
            value: res.data.data[i].name
        })
    }
    cb(suggest)
}

export function toTree(arr) {
    let ret = []
    let tree = {}
    for (let i = 0; i < arr.length; i++) {
        let obj = arr[i]
        if (tree[obj.type] != undefined) {
            tree[obj.type].push(obj)
        } else {
            tree[obj.type] = [obj]
            ret.push({
                type: obj.type,
                data: tree[obj.type]
            })
        }
    }
    return ret
}
