<template>
  <div>
    <div class="p_c_flexbox_row  p_c_box-flex_center" style="height: 6rem">
      <div style="flex: 1" class="p_c_box-flex_row-center">真实之树</div>
      <div class="p_c_flexbox_row p_c_test_border" style="width: 20rem" >
        <UserIconCMPO></UserIconCMPO>
      </div>
    </div>
    <div id="body">
      <el-input v-model="FilePathApi+from.imgUrl"></el-input>
      <el-input v-model="from.imgUrl"></el-input>
      <el-button @click="change">改变</el-button>
      <el-avatar :src="FilePathApi+from.imgUrl" :key="from.imgUrl"></el-avatar>
      <!--      <img :src="FileApi+from.imgUrl">-->
    </div>
  </div>
</template>

<script>

import UserIconCMPO from "@/components/UserIconCMPO";
import {FilePathApi} from "@/api/api";

export default {
  name: "test",
  data() {
    return {
      input: "",
      from: {},
      FilePathApi,
      imgUrl: "upload_file/963e329ab7f411eb849580fa5b6c6ed4_movie.jpg",
      imgUrl2: "upload_file/1b337502917011ebb2b580fa5b6c6ed4_小程序.jpg",
    }
  },
  components: {
    UserIconCMPO
  },
  methods: {
    async change() {
      await this.sleep(1000);
      if (this.from.imgUrl == this.imgUrl) {
        return this.from.imgUrl = this.imgUrl2
      }
      if (this.from.imgUrl == this.imgUrl2) {
        return this.from.imgUrl = ""
      }
      this.from.imgUrl = this.imgUrl
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
