import {WorkerApi} from "@/api/api";
import {get2} from "@/api/util";


/*获取工人列表*/
export async function getWorkers(data) {
    let res = await get2(WorkerApi, 0, data);
    return res
}
