import {WorkerApi} from "@/api/api";

import {get2} from "@/api/http";

export async function getWorkerApi(data) {
    let res = await get2(WorkerApi, data.id, data)
    return res
}
