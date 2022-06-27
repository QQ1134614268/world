import Axios from "axios";
import {CREATE_API, DELETE_API, DELETE_BATCH_API, PAGE_API, UPDATE_API} from "@/api/config";

export const getJson2 = (url, params) => {
    return Axios({
        method: 'get', url: url, params: params
    });
};
export const postJson2 = (url, data) => {
    return Axios({
        method: 'POST', url: url, data: data
    });
};
export const postForm2 = (url, data = {}) => {
    return Axios({
        method: 'POST', url: url, data: data, headers: {
            'Content-Type': 'multipart/form-data;'
        }
    });
};

export const getPageJson2 = (url, data = {}) => {
    return getJson2(url + PAGE_API, data);
};
export const crateJson2 = (url, data = {}) => {
    return postJson2(url + CREATE_API, data);
};
export const updateJson2 = (url, data = {}) => {
    return postJson2(url + UPDATE_API, data);
};
export const deleteJson2 = (url, data = {}) => {
    return postJson2(url + DELETE_API, data);
};
export const deleteBatchJson2 = (url, data = {}) => {
    return postJson2(url + DELETE_BATCH_API, data);
};

export const ppJson = (url, data, id) => {
    if (id === undefined || id == null || id === 0) {
        return crateJson2(url, data, id);
    }
    return updateJson2(url, data);
};
