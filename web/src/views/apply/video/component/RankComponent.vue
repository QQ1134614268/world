<template>
  <div>
    <div v-for="(item,index) in rankData" class="p_c_flexbox_row">
      <div :class="_getRankCls(index)">
        {{ index + 1 }}
      </div>
      <div class="p_c_long_txt_hidden " style="width: 80%">
        <!--        todo-->
        {{ item.describe || item.content }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RankComponent",
  props: {
    rankData: {
      type: Array,
      default: function () {
        return []
      }
    },
  },
  methods: {
    _getRankCls(index) {
      if (index <= 2) {
        return `rank_base rank_${index}`
      } else {
        return 'rank_base'
      }
    },
  }
}
</script>

<style scoped>
.rank_base {
  width: 2.4rem;
  height: 2.4rem;
  background-size: 25px 24px;
  color: #c1abab;
}

/*rank_base rank_0*/
.rank_0 {
  color: #f30303;
}

.rank_1 {
  color: #cb2e59;
}

.rank_2 {
  color: #ac4d60;
}


</style>