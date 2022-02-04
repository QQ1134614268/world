<template>
  <BoxFlex>
    <div class="">
      菜单分类
      <ul>

        <li><a href="#miao">去找喵星人</a></li>

        <li><a href="#wang">去找汪星人</a></li>

        <li><a href="#meng">其他萌物</a></li>

      </ul>
    </div>
    <div class="p_c_HolyGrail-body p_c_test_border">
      商品信息
      <a id="miao"></a><!--设置锚点方法1-->
      <h3 id="miao2">喵星人基地</h3><!--设置锚点方法2-->

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>


      <a name="wang"></a>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <a id="meng"></a>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>
    </div>
  </BoxFlex>
</template>

<script>
export default {
  name: "Store",
  data() {
    return {
      goodList: [
        {
          type: "主食",
          name: "大米",
          img: "",
          price: "",
        },
        {
          type: "主食",
          name: "馒头",
          img: "",
          price: "",
        },
        {
          type: "饮料",
          name: "青岛",
          img: "",
          price: "",
        },
        {
          type: "饮料",
          name: "矿泉水",
          img: "",
          price: "",
        },
      ],
      // goodList2: [
      //   {
      //     type: "主食",
      //     name: "大米",
      //     img: "",
      //     price: "",
      //   },
      //   {
      //     type: "主食",
      //     name: "馒头",
      //     img: "",
      //     price: "",
      //   },
      //   {
      //     type: "饮料",
      //     name: "青岛",
      //     img: "",
      //     price: "",
      //   },
      //   {
      //     type: "饮料",
      //     name: "矿泉水",
      //     img: "",
      //     price: "",
      //   },
      // ]
    }
  },
  methods: {}
}
</script>

<style scoped>
p {
  height: 20rem;
}
</style>