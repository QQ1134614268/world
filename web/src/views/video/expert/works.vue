<template>
  <div>
    <div class="p_c_flexbox" style="justify-content: space-between">
      <span>
          我的作品
      </span>
      <span>
        <el-button @click="dialogVisible=true;form={}">上传作品</el-button>
      </span>
    </div>
    <div class="p_c_flexbox">
      <div v-for="(o, index)  in tableData">
        <div class="block">
          <router-link :to="{path:VideoUrl,query: {video_id: o.id}}" class="p_c_space">
            <div>
              <img :src="o.thumbnail" style="width: 16rem;height: 9rem;object-fit: cover;">
            </div>
          </router-link>
          <div>
            {{ o.describe }}
          </div>
          <div>
            <span>{{ o.create_time }}</span>
          </div>
          <div>
              <span>
                <i class="el-icon-edit" @click="handleEdit(o)" style="margin-right: 1rem;">编辑</i>
                <i class="el-icon-delete" @click="del(index,o.id)" style="margin-right: 1rem;">删除</i>
              </span>
          </div>
        </div>
      </div>
    </div>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" :rules="rules" label-width="8rem" style="padding: 1rem">
        <el-form-item label="视频" prop="describe" required>
          <WrdVideoUploadV2 @getUrl="getUrl" :fileUrl="form.file"></WrdVideoUploadV2>
        </el-form-item>
        <el-form-item label="视频封面" prop="describe" required>
          <WrdImgUpload @getUrl="getUrl2" :fileUrl="form.thumbnail"></WrdImgUpload>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="form.describe"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button type="primary" @click="onCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import {FileApi, WorksApi, WorksListApi} from "@/api/api";
import {VideoUrl} from "@/views/video";
import {getUserIdByToken} from "@/api/util";
import WrdVideoUploadV2 from "@/components/WrdVideoUploadV2";
import WrdImgUpload from "@/components/WrdImgUpload";
import {deleteJson2, get2, ppJson} from "@/api/http";

export default {
  name: "works",
  components: {WrdImgUpload, WrdVideoUploadV2},
  data() {
    return {
      rules: {
        describe: [
          {required: true, message: '不能为空', trigger: 'blur'}
        ],
      },
      dialogVisible: false,
      FileApi,
      VideoUrl,
      progressFlag: false,
      loadProgress: 0,
      user_id: getUserIdByToken(),
      fileList: [],
      form: {},
      tableData: [],
    }
  },
  methods: {
    async init() {
      let result = await get2(WorksListApi, 0, {user_id: this.user_id})
      if (result.data.code === 1) {
        this.tableData = result.data.data
      } else {
        this.$message.error('失败');
      }
    },
    getUrl(fileUrl) {
      this.$set(this.form, 'file', fileUrl)
    },
    getUrl2(fileUrl) {
      this.$set(this.form, 'thumbnail', fileUrl)
    },
    async onSubmit() {
      if (!this.form.file) {
        this.$message.warning('请上传视频');
        return
      }
      let result = await ppJson(WorksApi, this.form.id, this.form)
      if (result.data.code === 1) {
        this.dialogVisible = false
      } else {
        this.$message.error('失败');
      }
    },
    async onCancel() {
      this.form = {}
      this.dialogVisible = false
    },
    handleEdit(row) {
      this.dialogVisible = true
      this.form = row
    },
    async del(index, id) {
      let result = await deleteJson2(WorksApi, id)
      if (result.data.code === 1) {
        this.$message.success('删除成功!');
        this.tableData.splice(index, 1)
      } else {
        this.$message.error('操作失败');
      }
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
@media only screen and (max-width: 768px) {
  /deep/ .el-dialog {
    width: 100%;
  }
}
</style>