<template>
  <div>
    <div>
      <router-link to="/member/admin/GoodList"> 菜单列表</router-link>
    </div>
    <div style="display: flex">
      <div class="p_c_HolyGrail-body">
        <span>
          菜单分类
        </span>
        <div :key="index" v-for="(obj,index) in goodList ">
          <li><a :href="'#'+obj.type">{{ obj.type }}</a></li>
        </div>
      </div>
      <div class="p_c_HolyGrail-body p_c_test_border">
        商品信息
        <div :key="index" v-for="(obj,index) in goodList " style="height: 50rem" class="p_c_HolyGrail-body" >
          <a :id="obj.type"></a>
          <div :key="index2" v-for="(obj2 , index2) in obj.data">
            <div class="p_c_HolyGrail-body">
              <el-image :src="obj2.img">
              </el-image>
              <div>
                {{ obj2.name }}
                {{ obj2.price }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Store",
  data() {
    return {
      goodList: [
        {
          type: "主食",
          data: [
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
          ]
        },
        {
          type: "饮料",
          data: [
            {
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
          ]
        }
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