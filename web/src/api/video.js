import {VideoUserApi} from "@/api/api";
import {postJson2} from "@/api/util";

export async function videoUserRegister(data) {
    let result = await postJson2(VideoUserApi, 0, data)
    return result
}

