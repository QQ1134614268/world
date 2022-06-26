<template>
  <div>
    <!--    todo 删除-->
    <el-upload
        :action="action"
        list-type="picture-card"
        :on-success="handleSuccess"
        :file-list="fileList"
        :on-exceed="handleExceed"
        :on-progress="handleProgress"
        :accept="accept"
        :before-upload="beforeAvatarUpload"
        :headers="{token:token}"
        :disabled="fileList.length >= limit || uploadBtn">
      <i slot="default" class="el-icon-plus"></i>
      <div slot="file" slot-scope="{file}">
        <video class="el-upload-list__item-thumbnail" :src="file.url" alt=""></video>
        <span class="el-upload-list__item-actions">
                    <span class="el-upload-list__item-preview" @click="handleShowVideo(file)">
                        <i class="el-icon-video-play"></i>
                    </span>
          <!--                    <span class="el-upload-list__item-edit" @click="handleEditVideo(file)">-->
          <!--                        <i class="el-icon-edit"></i>-->
          <!--                    </span>-->
                    <span class="el-upload-list__item-delete" @click="handleRemove(file)">
                        <i class="el-icon-delete"></i>
                    </span>
                </span>
        <el-progress type="circle" class="progressModule" :color="colors" :percentage="Number(uploadPercentage)"
                     v-if="showProgress && file.url === uploadUrl"></el-progress>
      </div>
    </el-upload>
    <el-dialog :visible.sync="dialogVisible" append-to-body width="40%" style="text-align:center">
      <video :src="dialogImageUrl" alt="" autoplay class="video" controls="controls"></video>
    </el-dialog>
    <!--    <el-dialog :visible.sync="editView" width="40%" append-to-body>-->
    <!--      <el-input type="textarea" :rows="4" v-model="editForm.url" @input="editVideo"></el-input>-->
    <!--    </el-dialog>-->
  </div>
</template>

<script>
import {FileApi} from "@/api/api";
import {VIDEO_TYPE_STR} from "@/api/config";
import {getToken} from "@/api/util";

export default {
  name: "WrdVideoUpload",
  props: {
    limit: {
      type: Number | String,
      default: 1,
    },
    action: {
      type: String,
      default: FileApi
    },
    file: {
      type: String,
      default: FileApi
    },
    accept: {
      type: String,
      default: VIDEO_TYPE_STR
    },
    beforeAvatarUpload: {
      type: Function,
      default: () => {
      }
    },
  },
  data() {
    return {
      fileList: [],
      dialogImageUrl: '',
      dialogVisible: false,
      // fileLists:this.fileList,
      // editForm: {
      //   url: '',
      //   uid: null
      // },
      // editView: false,
      token: getToken(),
      uploadPercentage: 0,
      showProgress: false,
      uploadUrl: '',
      colors: [
        {color: '#ADD8E6', percentage: 20},
        {color: '#87CEEB', percentage: 40},
        {color: '#87CEFA', percentage: 60},
        {color: '#00BFFF', percentage: 80},
        {color: '#1296DB', percentage: 100}
      ],
      uploadBtn: false,
    }
  },
  methods: {
    // 移除视频
    handleRemove(file) {
      for (let i in this.fileList) {
        if (this.fileList[i].uid === file.uid) {
          this.fileList.splice(i, 1)
        }
      }
      // this.submitFile()
    },
    handleShowVideo(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    // 上传完成
    handleSuccess(response, file, fileList) {
      this.showProgress = false
      this.uploadBtn = false
      if (response.code !== 1) {
        for (let i = 0; i < fileList.length; i++) {
          if (i + 1 === fileList.length) {
            fileList.splice(i, 1)
          }
        }
        this.$message.error(response.data)
        return
      }
      this.$message.success("上传成功")
      this.$emit("getFileList", fileList)
      // let obj = {
      //   uid: file.uid,
      //   url: response.data,
      // }
      // this.fileLists.push(obj)
      // this.submitFile()
    },
    // 播放视频
    // handleEditVideo(file) {
    //   this.editForm.url = file.url
    //   this.editForm.uid = file.uid
    //   this.editView = true
    // },
    // 编辑视频
    // editVideo() {
    //   for (let i in this.fileLists) {
    //     if (this.fileLists[i].uid === this.editForm.uid) {
    //       this.fileLists[i].url = this.editForm.url
    //     }
    //   }
    //   this.submitFile()
    // },
    // 将图片文件传回给父组件
    // submitFile() {
    //   this.$emit('submitImg', this.fileLists)
    // },
    // 上传进度
    handleProgress(response, file, fileList) {
      this.uploadBtn = true
      this.uploadUrl = file.url
      this.showProgress = true
      this.uploadPercentage = file.percentage.toFixed(0)
    },
    handleExceed() {
      console.log("handleExceed")
    }
  }
}
</script>

<style scoped>
.el-icon-plus {
  font-size: 30px !important;
}

.el-icon-video-play {
  font-size: 18px !important;

}

.el-icon-delete {
  font-size: 18px !important;
  color: rgb(243, 143, 130);
}

.video {
  min-height: 200px;
  max-height: 600px;
  min-width: 200px;
  max-width: 100%;
}

</style>
