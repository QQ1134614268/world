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
  methods: {
    getHeight() {
// ref='up' :style="conheight"
//        conheight: {
//         height: ''
//       },
      // alert(this.$refs.up.offsetWidth)
      //
      // let divs = document.getElementsByClassName("rightullidiv");
      // console.log(o)
      // alert(o)
      // o.offsetHeight = o.offsetWidth * 0.75
      // var o = document.getElementsByClassName("rightullidiv");
// var h = o.offsetHeight; //高度
// var w = o.offsetWidth; //宽度
      // this.conheight.height = $(".rightullidiv").innerHeight * 0.75 + 'rem';
      // this.conheight.height = $(".rightullidiv").innerHeight * 0.75 + 'rem';
      // alert(o.offsetHeight, o.offsetWidth)
    },
  },
  mounted() {
    //todo
    // https://www.cnblogs.com/lhl66/p/7908133.html
    // let h = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight; //浏览器高度
    // let topH = this.$refs.topInfo.offsetHeight;
    // console.log()
    // let tabH = this.$refs.tab.offsetHeight;
    // console.log()
    // let subH = this.$refs.subBtn.offsetHeight;
    // console.log()
    // let scrollHight = this.$refs.scroller.offsetHeight
    // this.height = (h - topH - tabH - subH) + "px"
    // //localStorage.setItem("access_token", '52ecda6ecb4a11e7bd2a00163e0891fd') //测试token
    // let w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;//浏览器宽度　
    //
    // //获取元素样式值,为元素ref="ele"(在样式里面写死了的高度)
// var heightCss = window.getComputedStyle(this.$refs.ele).height; // ？px


//获取元素内联样式值
//     var heightStyle = this.$refs.ele.style.height; // ？px　

    // https://blog.csdn.net/weixin_40008920/article/details/114474018?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_ecpm_v1~rank_v31_ecpm-1-114474018.pc_agg_new_rank&utm_term=vue+%E5%8A%A8%E6%80%81style+%E8%AE%BE%E7%BD%AE%E9%AB%98%E5%BA%A6&spm=1000.2123.3001.4430
  },
  created() {
    window.addEventListener('resize', this.getHeight);
    this.getHeight()
  }
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