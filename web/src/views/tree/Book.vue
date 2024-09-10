<template>
  <div>
    <div>
      <router-link :to="{path:'/tree/Catalogue'}" class="p_c_space">
        回到目录
      </router-link>
      <router-link :to="{path:'/tree/EditBook',query: {id:id }}" class="p_c_space">
        编辑
      </router-link>
      <router-link :to="{path:'/tree/AddProve',query: {id:id,value: obj.value}}" class="p_c_space">
        添加论点
      </router-link>
      <router-link :to="{path:'/tree/AddStory',query: {id: id,value: obj.value}}" class="p_c_space">
        添加故事
      </router-link>
    </div>
    <div class="title">
      {{ obj.value }}
    </div>
    <div class="block">
      <div v-for="(item , index) in prove" :key="index">
        <span>{{ index + 1 }}</span>
        <a :href="'/tree/Book?id='+item.id">
          {{ item.value }}
        </a>
      </div>
    </div>
    <div class="block">
      <div v-for="(item , index) in story" :key="index">
        <span>{{ index + 1 }}</span>
        <span>{{ item.value }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import {ADD_PROVE, ADD_STORY} from './index.js'
import {ProveApi, StoryApi} from "@/api/api";
import {get2} from "@/api/http";

export default {
  name: "BookComponent",
  data() {
    return {
      ADD_STORY: ADD_STORY,
      ADD_PROVE: ADD_PROVE,
      obj: {
        value: "希洛之书",
      },
      prove: [],
      story: [],
      id: this.$route.query.id,
    }
  },
  methods: {
    async get_data() {
      let res1 = await get2(ProveApi, this.id, {});
      let res2 = await get2(ProveApi, 0, {"parent_id": this.id});
      let res3 = await get2(StoryApi, 0, {"parent_id": this.id});

      if (res1.data.code === 1) {
        this.obj = res1.data.data
      } else {
        this.$message.error('失败');
      }
      if (res3.data.code === 1) {
        this.prove = res2.data.data
      } else {
        this.$message.error('失败');
      }
      if (res3.data.code === 1) {
        this.story = res3.data.data
      } else {
        this.$message.error('失败');
      }
    },
  },
  created() {
    this.get_data();
  }
}
</script>

<style scoped>

</style>