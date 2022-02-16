import {get2} from "@/api/util";
import {GoodsApi} from "@/api/api";

export async function getWorkerApi(data) {
    let res = await get2(GoodsApi, data.id, data)
    return res
}
