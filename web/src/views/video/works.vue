<template>
  <div>
    <HeaderComponent :user_id="user_id" v-if="user_id"></HeaderComponent>
    <el-tabs v-model="activeName">
      <el-tab-pane label="我的作品" name="first" class="p_c_box-flex_row-center">
        <div class="p_c_flexbox">
          <div v-for="(o, index) in tableData" class="col-3">
            <div class="p_c_box_margin p_c_box-shadow">
              <ThumbnailComponent :describe="o.describe" :thumbnail="o.thumbnail" :id="o.id">
              </ThumbnailComponent>
              <div style="display: flex;justify-content: space-between">
                <time>{{ o.create_time }}</time>
                <span>
                  <i class="el-icon-edit" @click="handleEdit(o)" style="margin-right: 1.6rem;">编辑</i>
                <i class="el-icon-delete" @click="del(index,o.id)" style="margin-right: 1.6rem;">删除</i>
                </span>
              </div>
            </div>
          </div>
        </div>
      </el-tab-pane>
      <el-tab-pane label="上传作品" name="second">
        <el-form ref="form" :model="form" :rules="rules" label-width="8rem" style="padding: 1rem">
          <el-form-item label="视频" prop="describe" required>
            <el-upload
                class="upload-demo"
                :show-file-list="false"
                :action="file_url"
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
                       :action="file_url"
                       :on-success="uploadLicense">
              <img v-if="form.thumbnail" :src="file_url+'?path='+form.thumbnail">
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
      </el-tab-pane>
    </el-tabs>
    <el-dialog title="编辑" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" :rules="rules" label-width="8rem" style="padding: 1rem">
        <el-form-item label="描述">
          <el-input v-model="form.describe"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit2">立即创建</el-button>
          <el-button type="primary" @click="onCancel2">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import HeaderComponent from "./component/avatar/HeaderComponent"
import jwt_decode from 'jwt-decode';
import AvatarComponent from "./component/avatar/AvatarComponent"
import ThumbnailComponent from "./component/ThumbnailComponent"

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
      TAB_FIRST: "first",
      TAB_SECOND: "second",
      dialogVisible: false,
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      file_url: process.env.VUE_APP_BASE_URL + '/api/file/FileApi2',
      video_url: "/video/Video",
      user_id: jwt_decode(localStorage.getItem("token"))["id"],
      activeName: "first",
      currentDate: new Date(),
      fileList: [],
      file_path: null,
      form: {},
      tableData: [],
      url: '/api/video_api/WorksApi',
      works_list_url: '/api/video_api/WorksListApi',
      tabPosition: "left",
      user: "",
    }
  },
  components: {
    HeaderComponent,
    AvatarComponent,
    ThumbnailComponent
  },
  methods: {
    uploadLicense(res, file, fileList) {
      this.form.thumbnail = res.data
    },
    async init() {
      let result = await this.$get2(this.works_list_url, 0, {user_id: this.user_id})
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
      let result = await this.$postJson2(this.url, 0, this.form)
      if (result.data.code == 1) {
        this.form = {}
        // await this.$router.push({path: 'video/works'})
      } else {
        this.$message('失败');
      }
    },
    async onCancel() {
      this.activeName = this.TAB_FIRST
      this.form = {}
    },
    handleEdit(row) {
      this.dialogVisible = true
      this.form = row
    },
    async onSubmit2() {
      let result = await this.$putJson2(this.url, this.form2.id, this.form2)
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
      let result = await this.$deleteJson2(this.url, id)
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