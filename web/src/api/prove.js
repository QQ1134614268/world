import {get2} from '@/main'
import {WorkerApi} from "@/api/const";


/*获取工人列表*/
export async function getWorkers(data) {
    let res = await get2(WorkerApi, 0, data);
    return res
}

export async function querySearch(data) {
    let res = await get2(WorkerApi, 0, data);
    return res
}

export async function querySearch(queryString, cb, url) {
    let data = {name: queryString}
    let res = await this.$get2(url, 0, data)
    let suggest = []
    for (let i = 0; i < res.data.data.length; i++) {
        suggest.push({
            value: res.data.data[i].name
        })
    }
    cb(suggest)
}