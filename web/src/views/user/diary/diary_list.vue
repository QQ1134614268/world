<template>
  <div>
    <!--    todo    只观看朋友的,分页查询-->

    <div>
      <span style="color: #00D000"> 列表</span>
      <button @click="addDiary" style="float: right;">写个日记</button>
    </div>
    <div v-for="(item,k) in recordList" style="display: flex">
      <div style="width: 20rem">{{ item.title }}</div>
      <button @click="getDiaryInfo(item.id)">查看详情</button>
    </div>
    <!--    todo el-tabs 页签-->
    <el-tabs tab-position="left" style="height: 200px;">
      <el-tab-pane label="列表">列表</el-tab-pane>
      <el-tab-pane label="写个日记">配置管理</el-tab-pane>
      <el-tab-pane label="查看详情">角色管理</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: "diary_list",
  data() {
    return {
      recordList: "",
    }
  },
  methods: {
    async get_record_all() {
      let url = '/api/message_api/get_speech_all';
      let result = await this.$get(url);
      this.recordList = result.data.data;
    },
    async getDiaryInfo(id) {
      await this.$router.push({
        name: '/diary/diary_info',
        params: {
          id: id,
        }
        /*query: {
            key: 'key',
            msgKey: this.msg
        }*/
      })
    },
    addDiary() {
      this.$router.push({path: '/diary/add_diary'})
    }
  },
  created() {
    this.get_record_all()
  }
}
</script>

<style scoped>

</style>
