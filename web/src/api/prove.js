import request from '@/utils/request'
import get2 from '@/main'

/**
 * 应用列表接口
 * @param {*} data
 *
 */
export function adminConfigsetIndexAPI(data) {
    return request({
        url: 'adminConfig/queryModuleSetting',
        method: 'post',
        data: data
    })
}

export async function getProveApi(parent_id) {
    return await get2(this.url, 0, {"parent_id": parent_id});
}

