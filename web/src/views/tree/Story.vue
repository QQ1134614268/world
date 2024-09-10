<template>
  <div>
    <div>
      <router-link :to="{path:'/tree/Catalogue'}" class="p_c_space">
        回到目录
      </router-link>

      <router-link :to="{path:'/tree/AddStory',query: {id: -1,value: '未分类'}}" class="p_c_space">
        添加故事
      </router-link>
    </div>
    <div v-for="(item , index) in story" :key="index" class="block p_c_flexbox_row">
      <div class="col-1">{{ index + 1 }}</div>
      <div class="col-11">{{ item.value }}</div>
    </div>
  </div>
</template>

<script>
import {StoryApi} from "@/api/api";
import {get2} from "@/api/http";

export default {
  name: "StoryComponent",
  data() {
    return {
      story: [],
    }
  },
  methods: {
    async init() {
      let res3 = await get2(StoryApi, 0, {});
      if (res3.data.code === 1) {
        this.story = res3.data.data
      } else {
        this.$message.error('失败');
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