<template>
  <div>
    <el-form :model="formData" :rules="formRule" ref="formData" label-width="100px">
      <el-form-item prop="name" label="姓名">
        <el-input v-model="formData.name"></el-input>
      </el-form-item>
      <el-form-item prop="user.tel" label="手机号">
        <el-input v-model="formData.user.tel"></el-input>
      </el-form-item>
      <el-form-item prop="phones[0].model" label="手机号">
        <el-input v-model="formData.phones[0].model"></el-input>
      </el-form-item>
      <el-form-item v-for="(phone, index) in formData.phones" :label="phone.brand" :key="phone.brand"
                    :prop="'phones.' + index + '.model'"
                    :rules="{
         required: true, message: 'model不能为空', trigger: 'blur'
         }">
        <el-input v-model="phone.model"></el-input>
        <el-form :model="formData.phones[index]" label-width="100px">
          <el-form-item v-for="(item, index1) in formData.phones[index].arr" :key="index1"
                        :prop="'arr.' + index1 +  '.data1'" label="data1" :rules="{
                 required: true, message: 'data1不能为空', trigger: 'blur'
                 }">
            <el-input v-model="item.data1"></el-input>
          </el-form-item>
        </el-form>
      </el-form-item>
    </el-form>
    <el-button @click="handleSubmit">提交</el-button>
  </div>
</template>


<script>
export default {
  name: 'checkComponent',
  data() {
    return {
      formData: {
        name: '',
        user: {tel: ''},
        phones: [
          {
            brand: "华为",
            model: "",
            arr: [{data1: ""}]
          },
          {
            brand: "小米",
            model: "",
            arr: [{data1: ""}]
          }
        ]
      },
      formRule: {
        name: [
          {required: true, message: '不能为空', trigger: 'blur'},
          {pattern: /^[\u4E00-\u9FA5]+$/, message: '用户名只能为中文', trigger: 'blur'}
        ],
        'user.tel': [{required: true, message: '手机号码不能为空', trigger: 'blur'}],
        'phones[0].model': [{required: true, message: 'model不能为空', trigger: 'blur'}],
      },
    }
  },

  methods: {
    handleSubmit() {
      // const t = this;
      // t.$refs['formData'].validate((valid) => {
      //   if (valid) {
      //     console.log(this.formData);
      //   }
      // })
    }
  }
}
</script>

<style scoped>

</style>
