import {get2} from "@/api/config";
import {PermissionApi} from "@/api/api";

export const Permission = {
    INVITATION_CODE: "INVITATION_CODE"
}


export async function hasPermission(permission) {
    let data = {permission: permission}
    let res = await get2(PermissionApi, 0, data);
    if (res.data.code == 1) {
        return res.data.data
    }
    return false
}


