<template>
  <div>
    <div class="block">
      <el-button @click="del">删除</el-button>
      <el-button @click="save">保存</el-button>
    </div>
    <div class="title">
      <el-input v-model="obj.value"></el-input>
    </div>
    <div class="block">
      <div v-for="(item , index) in prove">
        <textarea v-model="item.value " class="p_c_para">
        </textarea>
      </div>
    </div>
    <div class="block">
      <div v-for="(item , index) in story" class="p_c_flexbox_row">
        <textarea v-model="item.value " class="p_c_para">
        </textarea>
      </div>
    </div>
  </div>
</template>

<script>
import {ADD_PROVE, ADD_STORY} from "@/views/tree/index";
import {ProveApi, StoryApi} from "@/api/api";
import {deleteJson2, get2, putJson2} from "@/api/http";

export default {
  name: "EditBook",
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
    async del() {
      let res1 = await deleteJson2(ProveApi, this.id, {});
      this.$router.back()
      this.$router.back()
    },
    async save() {
      let res1 = await putJson2(ProveApi, this.obj.id, this.obj);
      let res2 = await putJson2(ProveApi, 0, this.prove);
      let res3 = await putJson2(StoryApi, 0, this.story);
      this.$router.back()
    },
  },
  created() {
    this.get_data();
  }
}
</script>

<style scoped>

</style>