<template>
  <div>
    <div class="title">
      title--希洛之书
      <div>
        <button @click="edit">编辑</button>
      </div>
    </div>
    <div class="p_c_box-flex" v-for="(item,k)  in argList">
      {{ item }}
    </div>
    <div v-for="(item,k)  in storyList">
      <div>
        <span>{{ k }}</span>
        .
        <span>
        {{ item }}
         </span>
      </div>

    </div>
    <div>
      2. xxx
    </div>
    <div>
      3. xxx
    </div>
  </div>

</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      storyList: [],
      argList: [],
      url: "",
    }
  },
  methods: {
    async edit() {
      await this.$router.push({path: '/model/Edit'})
    },
    async save() {
      let result = await this.$putJson2(this.url, this.form.id, this.form)
      if (result.data.code == 1) {
        this.$message('修改成功!');
      } else {
        this.$message('');
      }
    }
  }
}
</script>

<style scoped>

</style>