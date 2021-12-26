<template>
  <div>
    <div v-if="userId">
      下拉
      select
      dropdown
      <!--    todo 需要刷新 使用vuex 等 ,溢出改变同步全局-->

      <el-button @click="logout"></el-button>

    </div>
  </div>
</template>

<script>

export default {
  name: "UserIconCOMPO",
  data() {
    return {
      userId: '',

    }
  },
  methods: {
    async logout() {

    }
  }
}
</script>

<style scoped>

</style>