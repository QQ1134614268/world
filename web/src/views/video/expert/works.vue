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
          <!--          todo -->
          <el-upload class="upload-demo" :show-file-list="false" :action="FileApi"
                     :on-change="handleChange"
                     :on-success="uploadFileSuccess"
                     :before-upload="beforeAvatarUpload"
                     :on-progress="uploadVideoProcess"
                     :file-list="fileList">
            <i v-if="!progressFlag" class="el-icon-plus avatar-uploader-icon"></i>
            <el-progress v-if="progressFlag" type="line" :percentage="loadProgress" style="margin-top:10px;">
            </el-progress>
          </el-upload>
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

export default {
  name: "works",
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
    uploadVideoProcess(event, file, fileList) {
      this.progressFlag = true; // 显示进度条
      this.loadProgress = parseInt(event.percent); // 动态获取文件上传进度
      if (this.loadProgress >= 100) {
        this.loadProgress = 100
        setTimeout(() => {
          this.progressFlag = false
        }, 2000) // 一秒后关闭进度条
      }
    },
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
    async onSubmit() {
      if (!this.form.file) {
        this.$message('请上传视频');
        return
      }
      let result;
      if (this.form.id) {
        result = await this.$putJson2(WorksApi, this.form.id, this.form)
      } else
        result = await this.$postJson2(WorksApi, 0, this.form)
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
    uploadFileSuccess(response, file, fileList) {
      this.form.file = response.data
      this.$message.warning("上传成功");
    },
    handleChange(file, fileList) {
      this.fileList = fileList.slice(-1);
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