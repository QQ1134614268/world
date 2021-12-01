<template>
  <div>
    <div style="height: 5rem">
      <div v-if="music!=null">
        <span>
          <select v-model="type" name="fruit">
            <option value="1" selected>单曲循环</option>
            <option value="2">顺序播放(暂不支持)</option>
            <option value="3">随机播放(暂不支持)</option>
          </select>
        </span>
        <span style="text-align: center">{{ music.name }}</span>
        <audio ref="music" :src=music.url controls="controls" @ended="audioEnd">
          您的浏览器不支持 audio标签。
        </audio>
      </div>
    </div>
    <br/>
    <div v-for="(item,key) in musicList">
      <li @click="play(item)" style="list-style: none;">
        {{ key + 1 }}.{{ item.name }}
      </li>
    </div>
  </div>
</template>

<script>
export default {
  name: "Music",
  data() {
    return {
      type: 1,
      music: null,
      musicList: [],
      baseUrl: process.env.VUE_APP_BASE_URL
    }
  },
  methods: {
    async getMusicList() {
      let url = "/api/hello_api/get_music"
      let response = await this.$get(url);
      if (response.data.code != 1) {
        return
      }
      for (let value of response.data.data) {
        this.musicList.push({
          name: value.split("/").pop(),
          url: process.env.VUE_APP_BASE_URL + '/api/hello_api/get_music?music=' + value
        })
      }
    },
    play(item) {
      this.music = item
      this.$nextTick(() => {
        this.$refs.music.play()
      });
    },
    audioEnd() {
      this.$refs.music.play()
    },
  },
  created() {
    this.getMusicList()
  }
}
</script>

<style scoped>

</style>
