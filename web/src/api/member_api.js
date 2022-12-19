import {get2, postJson2} from "@/api/util";
import {GoodsApi, OrderApi} from "@/api/api";

export async function getWorkerApi(data) {
    let res = await get2(GoodsApi, data.id, data)
    return res
}


export function postOrder(data) {
    return postJson2(OrderApi, data.id, data);
}
