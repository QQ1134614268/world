<template>
  <!--todo dialog or 页面, 根据配置-->
  <el-form :model="form">
    <el-form-item> </el-form-item>
  </el-form>
</template>

<script>
import {FileApi} from "@/api/api";

export default {
  name: "Select",
  props: {
    form: {
      type: String,
      default: FileApi
    },
  }
}
</script>

<style scoped>

</style>