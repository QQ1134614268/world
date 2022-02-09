<template>
  <div class="p_c_box-flex">
    <div>
      <div v-for="(item,k) in attentionList">
        <div>
          {{ item.username }}
        </div>
      </div>
    </div>
    <div style="position:relative; width: 50rem;">
      <div>xxx</div>
      <div>
        message1 : 111
      </div>
      <div>
        message2 : 222
      </div>
      <div style="position:absolute;bottom:0;width: 100%;height: 8rem">
        <textarea style="width: 100%;height: 7rem"></textarea>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "message",
  data() {
    return {
      attentionList: [],
      userList: [],
      username: "",
      user: "",
      message: "",
    }
  },
  created() {
  },
}
</script>


<style scoped>

</style>
