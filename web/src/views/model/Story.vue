<template>
  <div>
    <div>
      <router-link :to="{name:'/model/Catalogue'}" class="p_c_space">
        回到目录
      </router-link>

      <router-link :to="{name:'/model/AddStory',query: {id: -1,value: '未分类'}}" class="p_c_space">
        添加故事
      </router-link>
    </div>
    <div v-for="(item , index) in story" class="block p_c_flexbox_row">
      <div class="col-1">{{ index + 1 }}</div>
      <div class="col-11">{{ item.value }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Story",
  data() {
    return {
      story: [],
      url2: "/api/model_api/StoryApi",
    }
  },
  methods: {
    async init() {
      let res3 = await this.$get2(this.url2, 0, {});
      if (res3.data.code == 1) {
        this.story = res3.data.data
      } else {
        this.$message('失败');
      }
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>