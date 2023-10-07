<template>
  <div>
    <div class="title block" v-if="this.$route.query.value">
      <input v-model="title"> </input>
    </div>
    <div class="block">
      <textarea v-model="content" style="width: 100%;" rows="10">
      </textarea>
    </div>
    <div class="block">
      <button @click="save">保存</button>
    </div>
  </div>
</template>

<script>
import {ProveApi} from "@/api/api";
import {postJson2} from "@/api/http";

export default {
  name: "AddRoot",
  data() {
    return {
      id: this.$route.query.id,
      title: this.$route.query.value,
      content: "",
    }
  },
  methods: {
    async save() {
      let data = {
        parent_id: this.id,
        value: this.content
      }
      let result = await postJson2(ProveApi, 0, data);
      if (result.data.code == 1) {
        this.$message.success('操作成功');
        this.$router.back()
      }
    }
  },
}
</script>

<style scoped>

</style>