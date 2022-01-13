import {get2} from "@/api/config";
import {PermissionApi} from "@/api/api";

export class Permission {
    static  INVITATION_CODE = "邀请码权限"
}

export async function hasPermission(permission) {
    let data = {permission: permission}
    let res = await get2(PermissionApi, 0, data);
    return res
}