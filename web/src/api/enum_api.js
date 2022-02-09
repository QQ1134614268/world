import {get2} from "@/api/util";
import {EnumApi} from "@/api/api";
import {REVIEW_ENUM} from "@/api/config";


/*获取枚举*/
export async function getEnum(data) {
    let res = await get2(EnumApi, 0, data);
    // let ret=[]
    // for (let i =0; i<res.data.data.length;i++){
    //     ret.append({
    //
    //     })
    // }
    return res.data.data
}

