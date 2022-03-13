<template>
  <WrdVideoUpload @get-file-list="getFileList" :fileList="fileList" limit=2>
  </WrdVideoUpload>

  <el
</template>
<script>
import WrdVideoUpload from "@/components/WrdVideoUpload";

export default {
  components: {WrdVideoUpload},
  data() {
    return {fileList: []}
  },
  methods: {
    getFileList(fileList) {
      this.fileList = fileList
    }
  }
}
</script>