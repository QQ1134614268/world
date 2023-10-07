import CryptoJS from "crypto-js";
import Axios from "axios";
import {IMG_TYPE, SALT_WORK_FACTOR, TOKEN, UPLOAD_FILE_SIZE_MAX, VIDEO_TYPE} from "@/api/config";
import Vue from "vue";
import jwt_decode from "jwt-decode";

import {get2} from "@/api/http";

export function get_salt_pwd(pwd) {
    // todo 密码明文
    let keyHex = CryptoJS.enc.Utf8.parse(SALT_WORK_FACTOR);
    let encrypted = CryptoJS.DES.encrypt(pwd, keyHex, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();

    // console.log(window.btoa('china is so nb'))
    // // 编码
    // "Y2hpbmEgaXMgc28gbmI="
    // window.atob("Y2hpbmEgaXMgc28gbmI=") // 解码
    // "china is so nb"
}

export function detectOS() {
    let sUserAgent = navigator.userAgent;
    let isWin = (navigator.platform === "Win32") || (navigator.platform === "Windows");
    let isMac = (navigator.platform === "Mac68K") || (navigator.platform === "MacPPC") || (navigator.platform === "Macintosh") || (navigator.platform === "MacIntel");
    if (isMac) return "Mac";
    let isUnix = (navigator.platform === "X11") && !isWin && !isMac;
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
    let char = '-';
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let strDate = date.getDate();

    if (month >= 1 && month <= 9) {
        month = '0' + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = '0' + strDate;
    }
    return year + char + month + char + strDate;
}

export function fmtDateY_M_D_H_M_S(date) {
    let char = '-';
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let strDate = date.getDate();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();

    if (month >= 1 && month <= 9) {
        month = '0' + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = '0' + strDate;
    }
    return year + char + month + char + strDate + " " + hours + ":" + minutes + ":" + seconds;
}

export function getDateY_M_D() {
    let date = new Date();
    return fmtDateY_M_D(date);
}

export async function querySearch(queryString, cb, url) {
    let data = {name: queryString};
    let res = await get2(url, 0, data);
    let suggest = [];
    for (let i = 0; i < res.data.data.length; i++) {
        suggest.push({
            value: res.data.data[i].name
        });
    }
    cb(suggest);
}

export function toTree(arr) {
    let ret = [];
    let tree = {};
    for (let i = 0; i < arr.length; i++) {
        let obj = arr[i];
        if (obj.label === undefined) {
            obj.label = 'other';
        }
        if (tree[obj.label] !== undefined) {
            tree[obj.label].push(obj);
        } else {
            tree[obj.label] = [obj];
            ret.push({
                label: obj.label,
                data: tree[obj.label]
            });
        }
    }

    return ret;
}

export async function exportExcelByHeader(url, headers) {
    let res = await Axios.get(url, {
        responseType: 'arraybuffer', // 或者responseType: 'blob'
        xsrfHeaderName: 'Authorization',
        headers: headers
    });
    try {
        let data = JSON.parse(res.data);
        if (data.code !== 1) {
            Vue.prototype.$message.error(data.data);
        }
    } catch (err) {
        // const {data, headers} = res;
        // const fileName = headers['content-disposition'].replace(/\w+;filename=(.*)/, '$1');
        const link = document.createElement('a');  // 创建元素
        link.style.display = 'none';
        let blob = new Blob([res.data]);
        link.style.display = 'none';
        link.href = URL.createObjectURL(blob);   // 创建下载的链接
        let fileName = "工人列表.xlsx";
        link.setAttribute('download', fileName);  // 给下载后的文件命名 fileName文件名  type文件格式
        document.body.appendChild(link);
        link.click();  // 点击下载
        document.body.removeChild(link);  //  下载完成移除元素
        window.URL.revokeObjectURL(link.href);  // 释放掉blob对象
    }
}

export function getUserInfoByToken() {
    if (localStorage.getItem(TOKEN) !== undefined && localStorage.getItem(TOKEN) !== '') {
        try {
            return jwt_decode(localStorage.getItem(TOKEN));
        } catch (ex) {
            console.log('捕获到异常：', ex);
        }
    }
    return undefined;
}

export function getToken() {
    return localStorage.getItem(TOKEN);
}

export function getUserIdByToken() {
    let user = getUserInfoByToken();
    if (user === undefined) {
        return user;
    }
    return getUserInfoByToken().id;
}

export function beforeImgUpload(file) {
    const isImage = IMG_TYPE.includes(file.type);
    if (!isImage) {
        Vue.prototype.$message.error('上传图片格式不正确!');
        return false;
    }
    const isLtSize = file.size / 1024 / 1024 < 5;
    if (!isLtSize) {
        Vue.prototype.$message.error('上传图片大小不能超过 5MB!');
        return false;
    }
    return true;
}


export function videoBeforeUpload(file) {

    if (VIDEO_TYPE.indexOf(file.type) === -1) {
        Vue.prototype.$message.error("视频格式" + file.type + "不正确！");
        return false;
    }

    const isLt10MB = file.size < UPLOAD_FILE_SIZE_MAX;
    if (!isLt10MB) {
        Vue.prototype.$message.error("上传视频大小不能超过10M！");
        return false;
    }
    //todo

    // const time_limit = new Promise(function (resolve, reject) {
    //     let url = URL.createObjectURL(file);
    //     let videoElement = new Audio(url);
    //     //    当指定的音频/视频的元数据已加载时，会发生 loadedmetadata 事件。 元数据包括：时长、尺寸（仅视频）以及文本轨道。
    //     videoElement.addEventListener("loadedmetadata", function (_event) {
    //         let duration = videoElement.duration; // 视频时长
    //         if (Math.floor(duration) >= 30) {
    //             Vue.prototype.$message.error("上传视频时长不能超过 30S！")
    //             return false
    //         } else {
    //             return true
    //         }
    //     });
    // })
    // return time_limit;
    return true;
}
