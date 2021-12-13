import {get2} from "@/api/config";
import {WorkerApi} from "@/api/api";


/*获取工人列表*/
export async function getWorkers(data) {
    let res = await get2(WorkerApi, 0, data);
    return res
}
