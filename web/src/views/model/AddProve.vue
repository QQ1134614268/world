<template>
  <div>
    <div class="title block">
      <input v-model="title"> </input>
    </div>
    <div class="block">
      <textarea v-model="content" style="width: 100%;" rows="10">
      </textarea>
    </div>
    <div class="block">
      <button onclick="save">保存</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Edit",
  data() {
    return {
      title: "希洛之书",
      content: "存在",
      url: "/api/model_api/ProveApi",
      url2: "/api/model_api/StoryApi",
      _id: 0,
    }
  },
  methods: {

    async getData() {
      let vo1 = this.$get2(this.url, this._id, {});
      this.obj = vo1
    },
    async save() {
      let a_data = {
        parent_id: this._id,
        content:this.content
      }
      let result = await this.$putJson2(this.url2, this._id, a_data);
    }
  }
}
</script>

<style scoped>

</style>