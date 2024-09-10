<template>
  <div>
    <div class="btn_box">
      <div class="row">
        <span>方向</span>
        <el-radio-group v-model="box_val.flex_direction">
          <el-radio label="row">row</el-radio>
          <el-radio label="column">column</el-radio>
        </el-radio-group>
      </div>
      <div class="row">
        <span>flex_wrap</span>
        <el-radio-group v-model="box_val.flex_wrap">
          <el-radio label="wrap">wrap</el-radio>
          <el-radio label="nowrap">nowrap</el-radio>
        </el-radio-group>
      </div>
      <div class="row">
        <span>justify_content</span>
        <el-radio-group v-model="box_val.justify_content">
          <el-radio :label="item" v-for="(item,index) in justify_content" :key="index">{{ item }}</el-radio>
        </el-radio-group>
      </div>
      <div class="row">
        <span>align-content</span>
        <el-radio-group v-model="box_val.align_content">
          <el-radio :label="item" v-for="(item,index) in align_content" :key="index">{{ item }}</el-radio>
        </el-radio-group>
      </div>
      <div class="row">
        <span>align-items</span>
        <el-radio-group v-model="box_val.align_items">
          <el-radio :label="item" v-for="(item,index) in align_items" :key="index">{{ item }}</el-radio>
        </el-radio-group>
      </div>
      <div class="row">
        <span>border</span>
        <el-radio-group v-model="show_border">
          <el-radio :label=true>是</el-radio>
          <el-radio :label=false>否</el-radio>
        </el-radio-group>
      </div>
    </div>
    <div class="btn_box">
      <div class="row">
        <span>align_self</span>
        <el-radio-group v-model="align_self_attr">
          <el-radio :label="item" v-for="(item,index) in align_self" :key="index">{{ item }}</el-radio>
        </el-radio-group>
        <div class="row">
          <span>flex成长</span>
          <el-radio-group v-model="flex">
            <el-radio label="0 0 auto">0 0 auto</el-radio>
            <el-radio label="1 1 auto">1 1 auto</el-radio>
          </el-radio-group>
        </div>
      </div>
    </div>
    <!--    <div>-->
    <!--      <div v-for="(val ,key, index) of box_val" :key="index">-->
    <!--        {{ key.replace("_", "-") }} : {{ val }}-->
    <!--      </div>-->
    <!--    </div>-->
    <div id="box">
      <div v-for="(item, index) in 20" :class="{p_c_test_border:show_border}" :key="index"
           :style="{width:(index+1)+'rem', height:(index+1)+'rem','align-self':align_self_attr,'flex':flex}">
        {{ (index + 1) }}
        白日依山尽,黄河入海流.
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "test_box",
  data() {
    return {
      show_border: true,
      box_val: {},
      item_val: {},
      justify_content: ["flex-start", "flex-end", "center", "space-between", "baseline", "first baseline", "last baseline", "space-around", "space-evenly"],
      align_items: ["flex-start", "flex-end", "center", "baseline", "stretch"],
      align_content: ["flex-start", "flex-end", "center", "space-between", "space-around", "stretch"],

      align_self: ["auto", "stretch", "center", "flex-start", "flex-end", "baseline", "initial", "inherit"],
      align_self_attr: 'auto',
      flex: '0 0 auto',

    }
  },
  created() {
    this.box_val = {
      'display': 'flex',
      'flex_direction': 'row',
      'flex_wrap': 'nowrap',
      'justify_content': 'flex-start',

      'align_content': 'stretch',
      'align_items': 'stretch',
    }
  },
  watch: {
    box_val: {
      handler: function () {
        let ele = document.getElementById("box")
        for (let attr in this.box_val) {
          ele.style[attr.replace("_", "-")] = this.box_val[attr]
        }

        let obj = {}
        for (let attr in this.box_val) {
          obj[attr.replace("_", "-")] = this.box_val[attr]
        }
        this.box = obj
      },
      deep: true
    },
  }
}
</script>

<style scoped>
.style {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  flex: 0 0 1;
  justify-content: center;
  justify-items: center;

  align-content: center;
  align-items: center;
}

.item_style {
  order: 1;
  flex-grow: 0;
  flex-shrink: 0;
  flex-basis: auto;

  align-self: center;
}

#box {
  height: 60rem;
  /*width: 100rem;*/
  border: blue solid 1px;

}

.btn_box {
  margin-left: 4rem
}
</style>
