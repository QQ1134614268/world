
import {get2} from "@/api/http";
import {ConfigApi} from "@/api/api";


/*获取枚举*/
export async function getEnum(data) {
    let res = await get2(ConfigApi, 0, data);
    return res.data.data
}

