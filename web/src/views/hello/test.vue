<template>
  <WrdElUpload :fileList="fileList" limit=2>
  </WrdElUpload>
</template>
<script>
import WrdElUpload from "@/components/WrdVideoUpload";

export default {
  components: {WrdElUpload},
  data() {
    return {fileList: []}
  }
}
</script>