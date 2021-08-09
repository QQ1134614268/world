<template>
  <div style="border-bottom: 0.2rem #f1ecec solid;">
    <a :href="video_url+'?video_id='+id">
      <div class="rightullidiv ">
        <img :src="file_url2+thumbnail" fit="contain" class="rightulliimg "/>
      </div>
    </a>
    <div style="height: 2.4rem;" class="p_c_long_txt_hidden">
      {{ describe }}
    </div>
  </div>
</template>

<script>
export default {
  name: "ThumbnailComponent",
  data() {
    return {

      video_url: "/video/Video",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }

  },
  props: {
    thumbnail: {
      type: String,
      default: ""
    },
    describe: {
      type: String,
      default: ""
    },
    id: {
      type: Number,
      default: ""
    },
  },
//   methods: {
//     getHeight() {
// // ref='up' :style="conheight"
// //        conheight: {
// //         height: ''
// //       },
//       // alert(this.$refs.up.offsetWidth)
//       //
//       // let divs = document.getElementsByClassName("rightullidiv");
//       // console.log(o)
//       // alert(o)
//       // o.offsetHeight = o.offsetWidth * 0.75
//       // var o = document.getElementsByClassName("rightullidiv");
// // var h = o.offsetHeight; //高度
// // var w = o.offsetWidth; //宽度
//       // this.conheight.height = $(".rightullidiv").innerHeight * 0.75 + 'rem';
//       // this.conheight.height = $(".rightullidiv").innerHeight * 0.75 + 'rem';
//       // alert(o.offsetHeight, o.offsetWidth)
//     },
//   },
//   created() {
//     window.addEventListener('resize', this.getHeight);
//     this.getHeight()
//   }
}
</script>

<style scoped>
.rightullidiv {
  width: 100%;
  /*todo 根据宽度动态设置 height max min eg: min-height: 20rem;*/
  height: 100%;

  background: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.rightulliimg {
  max-width: 100%;
  max-height: 100%;
}
</style>