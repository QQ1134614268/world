import CryptoJS from "crypto-js";
import Axios from "axios";
import {SALT_WORK_FACTOR, TOKEN} from "@/api/config";
import Vue from "vue";
import jwt_decode from "jwt-decode";

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
    let isWin = (navigator.platform === "Win32") || (navigator.platform == "Windows");
    let isMac = (navigator.platform === "Mac68K") || (navigator.platform == "MacPPC") || (navigator.platform == "Macintosh") || (navigator.platform == "MacIntel");
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
        if (obj.label == undefined) {
            obj.label = 'other'
        }
        if (tree[obj.label] != undefined) {
            tree[obj.label].push(obj)
        } else {
            tree[obj.label] = [obj]
            ret.push({
                label: obj.label,
                data: tree[obj.label]
            })
        }
    }

    return ret
}

export async function exportExcelByHeader(url, headers) {
    let res = await Axios.get(url, {
        responseType: 'arraybuffer', // 或者responseType: 'blob'
        xsrfHeaderName: 'Authorization',
        headers: headers
    })
    try {
        let data = JSON.parse(res.data)
        if (data.code != 1) {
            Vue.prototype.$message.error(data.data)
        }
    } catch (err) {
        // const {data, headers} = res;
        // const fileName = headers['content-disposition'].replace(/\w+;filename=(.*)/, '$1');
        const link = document.createElement('a');  // 创建元素
        link.style.display = 'none';
        let blob = new Blob([res.data]);
        link.style.display = 'none';
        link.href = URL.createObjectURL(blob);   // 创建下载的链接
        let fileName = "工人列表.xlsx"
        link.setAttribute('download', fileName);  // 给下载后的文件命名 fileName文件名  type文件格式
        document.body.appendChild(link);
        link.click();  // 点击下载
        document.body.removeChild(link);  //  下载完成移除元素
        window.URL.revokeObjectURL(link.href);  // 释放掉blob对象
    }
}

export function getUserInfoByToken() {
    if (localStorage.getItem(TOKEN) != undefined && localStorage.getItem(TOKEN) != '') {
        return jwt_decode(localStorage.getItem(TOKEN))
    }
    return undefined
}

export function getUserIdByToken() {
    let user = getUserInfoByToken()
    if (user != undefined)
        return getUserInfoByToken().id
}

export function beforeImgUpload(file) {
    let types = ['image/jpeg', 'image/jpg', 'image/png'];
    const isImage = types.includes(file.type);
    if (!isImage) {
        Vue.prototype.$message.error('上传图片只能是 JPG、JPEG、PNG 格式!');
    }
    const isLtSize = file.size / 1024 / 1024 < 5;
    if (!isLtSize) {
        this.$message.error('上传图片大小不能超过 5MB!');
    }
}

export function beforeVideoUpload(file) {
    // 获取视频时长
    var url = URL.createObjectURL(file);
    var audioElement = new Audio(url);
    var duration;
    this.durationNumber = audioElement.addEventListener(
        "loadedmetadata",
        function (_event) {
            duration = audioElement.duration; //时长为秒，小数
            return duration;
        }
    );
    setTimeout(() => {
        //视频大小（MB）
        let fileSize = file.size / 1024 / 1024;
        this.bandwidth = fileSize / duration;
    }, 50);
    if (
        [
            "video/mp4",
            "video/ogg",
            "video/flv",
            "video/avi",
            "video/wmv",
            "video/rmvb",
            "video/mov"
        ].indexOf(file.type) == -1
    ) {
        // layer.msg("请上传正确的视频格式");
        this.$message({
            type: "info",
            message: "请上传正确的视频格式"
        });
        return false;
    }
    if (this.bandwidth > 2) {
        // 视频带宽不能超过2MB/s
        this.$message.error('视频带宽过大，上传失败！');
        return false;
    }
    this.isShowUploadVideo = false;
}

export function videoBeforeUpload(file) {
    const self = this
    const isLt30MB = file.size / 1024 / 1024 < 30;
    const isSize = new Promise(function (resolve, reject) {
        let _URL = window.URL || window.webkitURL;
        let videoElement = document.createElement('video')
        // 当指定的音频/视频的元数据已加载时，会发生 loadedmetadata 事件。 元数据包括：时长、尺寸（仅视频）以及文本轨道。
        videoElement.addEventListener("loadedmetadata", function (_event) {
            let width = videoElement.videoWidth
            let height = videoElement.videoHeight
            let duration = videoElement.duration; // 视频时长
            if (!isLt30MB) return operatTip('error', '上传视频大小不能超过30MB！')
            if (Math.floor(duration) >= 30) return operatTip('error', '上传视频时长不能超过 30S！')
            let valid = `${width}*${height}` === '1280*720'
            valid ? resolve() : reject();
        })
        videoElement.src = _URL.createObjectURL(file)
    }).then(() => {
        return file;
    }, () => {
        operatTip('error', '上传视频尺寸为 1280*720！')
        return Promise.reject();
    });
    return isSize;
}