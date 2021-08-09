<template>
  <div>
    <div>
      <el-upload
          class="upload-demo"
          :action="url"
          :on-change="handleChange"
          :on-success="handleAvatarSuccess"
          :file-list="fileList">
        <el-button size="small" type="primary">点击上传</el-button>
      </el-upload>
    </div>
    <div>
      <el-input placeholder="输入关键字进行过滤" style="width: 20rem" v-model="filterText"></el-input>
      <el-tree :data='data'
               :props="treeProps"
               :draggable=true
               :expand-on-click-node=false
               @node-drop="handleDrop"
               :lazy=true
               :load="loadNode"
               :highlight-current=true>
        <div class='custom-tree-node' slot-scope='{ node, data }' style="display: flex">
          <div class="text" style="text-overflow:ellipsis;">{{ data.name }}</div>
          <div>
            <el-input placeholder="定义,描述,影响因子" style="width: 10rem" size="mini"
                      v-model="data.describe"></el-input>
          </div>
          <div>
            <el-input placeholder="数据" style="width: 10rem" size="mini" v-model="data.data"></el-input>
          </div>
          <div style="float: right">
            <el-button type="primary" icon="el-icon-plus" size="mini"
                       @click="show(node, data,addDialogVisible)"></el-button>
            <el-button type="primary" icon="el-icon-edit" size="mini"
                       @click="show(node, data,addDialogVisible)"></el-button>
            <el-button type="primary" icon="el-icon-delete" size="mini"></el-button>
          </div>
        </div>
      </el-tree>
      <el-dialog :visible.sync='addDialogVisible' title='提示' width='30%'>
        <span>新增</span>
        <input placeholder='名' type='text' v-model='node.name'>
        <input placeholder='定义,描述,影响因子' type='text' v-model='node.describe'>
        <input placeholder='数据' type='text' v-model='node.data'>
        <span class='dialog-footer' slot='footer'>
        <el-button @click='addDialogVisible = false'>取 消</el-button>
        <el-button @click='save' type='primary'>确 定</el-button>
      </span>
      </el-dialog>
      <el-dialog :visible.sync='updateDialogVisible' title='提示' width='30%'>
        <span>修改</span>
        <input placeholder='名' type='text' v-model='node.name'>
        <input placeholder='定义,描述,影响因子' type='text' v-model='node.describe'>
        <input placeholder='数据' type='text' v-model='node.data'>
        <span class='dialog-footer' slot='footer'>
        <el-button @click='updateDialogVisible = false'>取 消</el-button>
        <el-button @click='save' type='primary'>确 定</el-button>
      </span>
      </el-dialog>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      url: process.env.VUE_APP_BASE_URL + '/api/class_api/ScriptApi',
      fileList: [],
      data: [],
      filterText: "",
      treeProps: {
        children: 'children',
        label: 'name'
      },
      addDialogVisible: false,
      updateDialogVisible: false,
      node: "",
    };
  },
  methods: {
    handleChange(file, fileList) {
      this.fileList = fileList.slice(-3);
    },
    handleAvatarSuccess(res, file, fileList) {
      console.log(res)
      console.log(file)
      console.log(fileList)
    },
    async getAllNodes() {
      let url = '/api/class_api/ClassApi';
      let result = await this.$get(url);
      // this.data = result.data.data;
    },
    show(node, data, addDialogVisible) {
      this.node = data
      this.addDialogVisible = !addDialogVisible
    },
    async loadNode(node, resolve) {
      let url = '/api/class_api/ClassApi';
      let data = {parent_id: node.data ? node.data.id : 0}
      let result = await this.$get(url, data);
      // this.data = result.data.data;
      // node.children = result.data.data
      resolve(result.data.data);
    },
    async addNode() {
      let url = '/api/class_api/ClassApi';
      let result = await this.$get(url);
      this.data = result.data.data;
    },
    async save() {
      let url = '/api/class_api/ClassApi';
      let result = null
      if (this.node.id) {
        result = await this.$putJson(url, this.node);
      } else {
        result = await this.$postJson(url, this.node);
      }
      this.addDialogVisible = !this.addDialogVisible
      if (result.data.code == 1) {
        this.$message('保存成功');
      } else {
        this.$message('保存失败');
      }
    },
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },
    handleDrop(draggingNode, dropNode, dropType, ev) {
      console.log(draggingNode, dropNode, dropType, ev);

    },
  },
  created() {
    this.getAllNodes()
  },
  watch: {
    filterText(val) {
      this.$refs.tree.filter(val);
    }
  }
};
</script>
<style>
div.text {
  /*white-space: nowrap;*/
  width: 12em;
  overflow: hidden;
}

div.text:hover {
  text-overflow: inherit;
  overflow: visible;
}
</style>