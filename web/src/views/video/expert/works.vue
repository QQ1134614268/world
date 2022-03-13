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
          <a :href=VideoUrl>
            <div>
              <img :src="o.thumbnail" style="width: 16rem;height: 9rem;object-fit: cover;">
            </div>
          </a>
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
<!--          todo-->
          <WrdVideoUpload @getFileList="getFileList" :file="form.file" :before-avatar-upload="beforeAvatarUpload">
          </WrdVideoUpload>
        </el-form-item>
        <el-form-item label="视频封面" prop="describe" required>
          <el-upload style="width: 10%;height: 10%" :show-file-list="false" :action="FileApi"
                     :on-success="uploadFileSuccess2">
            <img v-if="form.thumbnail" :src="form.thumbnail">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="form.describe"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即创建</el-button>
          <el-button type="primary" @click="onCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import {FileApi, WorksApi, WorksListApi} from "@/api/api";
import {VideoUrl} from "@/views/video";
import {getUserIdByToken, videoBeforeUpload} from "@/api/util";
import WrdVideoUpload from "@/components/WrdVideoUpload";

export default {
  name: "works",
  components: {WrdVideoUpload},
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
    uploadFileSuccess2(res, file, fileList) {
      this.form.thumbnail = res.data
    },
    async init() {
      let result = await this.$get2(WorksListApi, 0, {user_id: this.user_id})
      if (result.data.code == 1) {
        this.tableData = result.data.data
      } else {
        this.$message('失败');
      }
    },
    getFileList(fileList) {
      this.fileList = fileList
    },
    async onSubmit() {
      if (this.fileList.size()==0) {
        this.$message('请上传视频');
        return
      }
      this.form.file = this.fileList[0].response.data
      let result = await this.$ppJson(WorksApi, this.form.id, this.form)
      if (result.data.code == 1) {
        this.dialogVisible = false
      } else {
        this.$message('失败');
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
      let result = await this.$deleteJson2(WorksApi, id)
      if (result.data.code == 1) {
        this.$message('删除成功!');
        this.tableData.splice(index, 1)
      } else {
        this.$message('');
      }
    },
    beforeAvatarUpload(file) {
      return videoBeforeUpload(file)
    }
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