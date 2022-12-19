import {get2} from "@/api/util";
import {EnumApi} from "@/api/api";


/*获取枚举*/
export async function getEnum(data) {
    let res = await get2(EnumApi, 0, data);
    return res.data.data
}

