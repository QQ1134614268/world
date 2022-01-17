const CryptoJS = require('crypto-js');

export const DATE_FMT = "YYYY-MM-DD"
export const SALT_WORK_FACTOR = "AAAA_BBBB_CCCC_DDDD"

export function get_salt_pwd(pwd) {
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