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
      <div v-for="o in tableData">
        <div class="block">
          <a :href=VideoUrl>
            <div>
              <img :src="FilePathApi+o.thumbnail" style="width: 25rem;height: 14rem;object-fit: cover;">
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
                <i class="el-icon-edit" @click="handleEdit(o)" style="margin-right: 1.6rem;">编辑</i>
                <i class="el-icon-delete" @click="del(index,o.id)" style="margin-right: 1.6rem;">删除</i>
              </span>
          </div>
        </div>
      </div>
    </div>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" :rules="rules" label-width="8rem" style="padding: 1rem">
        <el-form-item label="视频" prop="describe" required>
          <el-upload
              class="upload-demo"
              :show-file-list="false"
              :action="FileApi"
              :on-change="handleChange"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload"
              :file-list="fileList">
            <el-button size="small" type="primary">点击上传</el-button>
          </el-upload>
        </el-form-item>
        <el-form-item label="视频封面" prop="describe" required>
          <el-upload style="width: 10%;height: 10%"
                     :show-file-list="false"
                     :action="FileApi"
                     :on-success="uploadLicense">
            <img v-if="form.thumbnail" :src="FilePathApi +form.thumbnail">
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
import jwt_decode from 'jwt-decode';
import {VideoUrl} from "@/api/routerUrl";
import {FileApi, FilePathApi, WorksApi, WorksListApi} from "@/api/api";

export default {
  name: "works",
  data() {
    return {
      rules: {
        // file_path: [
        //   {required: true, message: '不能为空', trigger: 'blur'}
        // ],
        describe: [
          {required: true, message: '不能为空', trigger: 'blur'}
        ],
      },
      dialogVisible: false,
      FilePathApi,
      FileApi,
      VideoUrl,
      user_id: jwt_decode(localStorage.getItem("token"))["id"],
      fileList: [],
      file_path: null,
      form: {},
      tableData: [],
    }
  },
  methods: {
    uploadLicense(res, file, fileList) {
      this.form.thumbnail = res.data
    },
    async init() {
      let result = await this.$get2(WorksListApi, 0, {user_id: this.user_id})
      if (result.data.code == 1) {
        this.tableData = result.data.data
        // await this.$router.push({path: 'video/works'})
      } else {
        this.$message('失败');
      }
    },
    async onSubmit() {
      if (this.file_path) {
        this.form.file = this.file_path
      } else {
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
    async onSubmit2() {
      let result = await this.$putJson2(WorksApi, this.form2.id, this.form2)
      if (result.data.code == 1) {
        this.dialogVisible = false
        this.form = {}
      } else {
        this.$message('失败');
      }
    },
    onCancel2() {
      this.dialogVisible = false
      this.form = {}
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
    handleAvatarSuccess(response, file, fileList) {
      this.file_path = response.data
      this.$message.warning("上传成功");
    },
    handleChange(file, fileList) {
      this.fileList = fileList.slice(-1);
    },
    beforeAvatarUpload(file) {
      return 1
      // const isJPG = file.type === 'image/jpeg';
      // const isLt2M = file.size / 1024 / 1024 < 2;
      //
      // if (!isJPG) {
      //   this.$message.error('上传头像图片只能是 JPG 格式!');
      // }
      // if (!isLt2M) {
      //   this.$message.error('上传头像图片大小不能超过 2MB!');
      // }
      // return isJPG && isLt2M;
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