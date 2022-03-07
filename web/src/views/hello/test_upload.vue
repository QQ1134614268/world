<template>
  <WrdVideoUpload :fileList="fileList" limit=2>
  </WrdVideoUpload>
</template>
<script>
import WrdVideoUpload from "@/components/WrdVideoUpload";

export default {
  components: {WrdVideoUpload},
  data() {
    return {fileList: []}
  }
}
</script>