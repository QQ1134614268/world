<template>
  <div style="display: flex;height: 50rem">
    <div style="width: 20rem">
      <div v-for="(item,k) in attentionList">
        <div>
          {{ item.username }}
        </div>
      </div>
      <div>
        群组1
      </div>
      <div>
        群组2
      </div>
      <div>
        陌生人
      </div>
      <div style="display: flex;">
        <input v-model="username" style="width: 10rem"></input>
        <button @click="findUserByName">查找</button>
        <button @click="addAttention">添加</button>
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
  methods: {
    async getMyAttention() {
      let url = '/api/attention_api/getAttentionList';
      let result = await this.$get(url);
      this.attentionList = result.data.data;
    },
    async addAttention() {
      let data = {
        userId: this.user.id
      }
      let url = '/api/attention_api/addAttention';
      let result = await this.$postJson(url, data);
      this.message = result.data.data;
    },
    async getUserAll() {
      let url = '/api/user_api/getUserAll';
      let result = await this.$get(url);
      this.userList = result.data.data;
    },
    async findUserByName() {
      let url = '/api/user_api/getUserByName';
      let data = {
        username: this.username
      };
      let result = await this.$get(url, data);
      this.user = result.data.data;
    },
  },
  created() {
  },
}
</script>


<style scoped>

</style>
