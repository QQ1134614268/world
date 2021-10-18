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
    }
  },
  methods: {
    async save() {

    }
  }
}
</script>

<style scoped>

</style>