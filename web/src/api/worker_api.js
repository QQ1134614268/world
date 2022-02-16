import {get2} from "@/api/util";
import {WorkerApi} from "@/api/api";

export async function getWorkerApi(data) {
    let res = await get2(WorkerApi, data.id, data)
    return res
}
