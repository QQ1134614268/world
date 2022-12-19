<template>
  <div>
    <h1>{{ message }}</h1>
    <button v-on:click="getData">get 测试连通性</button>
    <button v-on:click="getData2">get 测试连通性2</button>
    <button v-on:click="postJson">postJson 测试</button>
    <div>
      <input type="file" ref="file1">
      <input type="file" ref="file2">
      <button v-on:click="postFormData">FormData 提交文件</button>
    </div>
    <div>
      <button v-on:click="script">script</button>
    </div>
       <el-tabs v-model="msg2" >
        <el-tab-pane label="用户管理" name="first">用户管理</el-tab-pane>
        <el-tab-pane label="配置管理" name="second">配置管理</el-tab-pane>
        <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane>
        <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import jwt_decode from 'jwt-decode';
import Axios from "axios";
import {TOKEN} from "@/api/config";

export default {

  name: 'hello',
  data() {
    return {
      message: 'default',
      msg2:'first'
    }
  },
  methods: {
    async getData() {
      let url = '/api/hello_api/hello';
      let result = await Axios({
        method: 'get',
        url: url,
        params: {name: 'cat'}
      })
      this.message = result.data.data;
    },
    script() {
      const decoded = jwt_decode(localStorage.getItem(TOKEN));
      console.log(decoded);
    },
    async postJson() {
      let url = '/api/hello_api/post_json';
      let data = {"name": 'tom', "age": 1}
      let result = await Axios({
        method: 'POST',
        url,
        data: data
      });
      this.message = result.data.data;
    },
    async postFormData() {
      let url = '/api/hello_api/post_formData';
      const file1 = this.$refs.file1.files[0];
      const file2 = this.$refs.file2.files[0];
      const data = new FormData();
      data.append('file1', file1);
      data.append('file2', file2);
      data.append('name', 'cat');
      let result = await Axios({
        method: 'POST',
        url,
        data: data,
        headers: {
          'Content-Type': 'multipart/form-data;'
        }
      })
      this.message = result.data.data;
    },
    getData2: function () {
      let that = this;
      let url = '/api/hello_api/hello';
      // url='http://127.0.0.1/api/hello_api/post_json?name=1'
      // let requestData = {};
      Axios.get(url)
          .then(function (res) {
            that.message = res.data.data;
          })
          .catch(function (err) {
            alert(err);
          })
    },
    postJson2: function () {
      let that = this;
      let url = '/api/hello_api/post_json';
      let requestData = {name: 'tom', age: 11};
      requestData = JSON.stringify(requestData);
      Axios.post(url, requestData)
          .then(function (res) {
            that.message = res.data.data;
          })
          .catch(function (err) {
            alert(err);
          })
    },
  }
}
</script>

