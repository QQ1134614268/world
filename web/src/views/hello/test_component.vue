<template>
  <div>
    <h3> 测试导入对话框</h3>
    <div>
      <err msg="this is err test dialog message!"></err>
    </div>
  </div>
</template>

<script>
import err from "@/components/err.vue"

export default {
  components: {
    err
  },
  name: "test_component"
}
</script>

<style scoped>

</style>
