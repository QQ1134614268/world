<template>
  <div class='avatar-uploader'>
    <myUp v-on:getImgUrl='AddInputUrl'></myUp>
  </div>
</template>

<script>
export default {
  name: "MyUp",
  methods: {
    AddInputUrl(data) {
      let a = data
      let tp = a.length
      let imghz = a.slice(tp - 4, tp)
      let src = 'src="' + a + '"'
      let bq = "<img " + src + " alt='' />"
      this.value += bq
    }
  }
}
</script>

<style scoped>

</style>