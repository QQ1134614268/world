<template>
  <div>
    测试服务
    <div v-for="item in testUrls ">
      <a :href=item.path>{{ item.path }}</a>
    </div>
  </div>
</template>

<script>
import routes from "./index"

export default {
  name: "TestHome",
  data() {
    return {
      testUrls: routes,
    }
  }
}
</script>

<style scoped>

</style>