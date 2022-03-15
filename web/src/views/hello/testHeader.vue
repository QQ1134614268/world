<template>
  <div>
    <div class="p_c_flexbox_row  p_c_box-flex_center" style="height: 6rem">
      <div style="flex: 1" class="p_c_box-flex_row-center">test</div>
      <div class="p_c_flexbox_row" style="width: 20rem">
      </div>
    </div>
    <div id="body">
      <el-input v-model="form.imgUrl"></el-input>
      <el-input v-model="form.imgUrl"></el-input>
      <el-button @click="change">改变</el-button>
      <el-avatar :src="form.imgUrl" :key="form.imgUrl"></el-avatar>
    </div>
  </div>
</template>

<script>
export default {
  name: "test",
  data() {
    return {
      input: "",
      form: {},
      imgUrl: "upload_file/963e329ab7f411eb849580fa5b6c6ed4_movie.jpg",
      imgUrl2: "upload_file/1b337502917011ebb2b580fa5b6c6ed4_小程序.jpg",
    }
  },
  methods: {
    async change() {
      await this.sleep(1000);
      if (this.form.imgUrl == this.imgUrl) {
        return this.form.imgUrl = this.imgUrl2
      }
      if (this.form.imgUrl == this.imgUrl2) {
        return this.form.imgUrl = ""
      }
      this.form.imgUrl = this.imgUrl
    },
    sleep(time) {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve();
        }, time || 1000);
      })
    },
    handleCommand() {
    }
  }
}
</script>

<style scoped>
img, video {
  object-fit: contain;
  max-width: none;
  height: auto;
}

img.a {
  width: 200px;
  height: 400px;
  object-fit: cover;
}
</style>
