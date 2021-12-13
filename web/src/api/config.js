import Axios from "axios";

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
export const ppJson = (url, data, id) => {
    if (typeof (id) == "undefined" || id == null) {
        return postJson(url, data)
    }
    return putJson(url + "/" + id, data)
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