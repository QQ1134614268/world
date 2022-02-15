<template>
  <!-- 弹框部分 -->
  <div>
    <!--    <div slot="title" :style="{color:colorstatus[dialogStatus]}">-->
    <!--      <i :class="iconMap[dialogStatus]">-->
    <!--        {{ textMap[dialogStatus] }}-->
    <!--      </i>-->
    <!--    </div>-->
    <el-form ref="dataform" label-width="120px" :model="temp" :rules="rules" label-position="right">
      <el-form-item
          v-for="(item,index) in AddDialogForm"
          :key="index"
          :label="item.label"
          :model="temp"
          :prop="item.key"
      >
        <!-- 所属部门 -->
        <el-select
            v-if="item.key==='group_id'"
            v-model="temp[item.key]"
            placeholder="请选择"
            filterable
            style="width:350px"
        >
          <el-option
              v-for="place in groupOptions"
              :key="place.id"
              :label="place.fullname"
              :value="place.id"
              :prop="item.key"
          />
        </el-select>
        <el-input
            v-else-if="item.key==='lng'"
            v-model="temp[item.key]"
            style="width:350px"
            clearable
        />
        <el-input
            v-else-if="item.key==='lat'"
            v-model="temp[item.key]"
            style="width:350px"
            clearable
        />
        <el-input
            v-else
            v-model="temp[item.key]"
            :prop="item.key"
            style="width:350px"
            clearable
        />
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer" style="text-align:center">
      <el-button @click="dialogAdd=false">取 消</el-button>
      <!--            <el-button-->
      <!--                v-if="dialogStatus=='create'"-->
      <!--                type="primary"-->
      <!--                @click="createData"-->
      <!--            >提交-->
      <!--            </el-button>-->
      <!--            <el-button-->
      <!--                v-else-if="dialogStatus=='update'"-->
      <!--                type="primary"-->
      <!--                @click="updateData"-->
      <!--            >提交-->
      <!--            </el-button>-->
    </div>
  </div>
</template>
<script>
// import { isSpace } from '存放函数的路径'
function isSpace(str) {
  const reg = /(^\s+)|(\s+$)|\s+/g
  return reg.test(str)
}

export default {
  name: 'App',
  components: {},
  data() {
    const validateSpace = (rule, value, callback) => {
      if (isSpace(value)) {
        return callback(new Error('请输入非空格字符！'))
      } else if (!value) {
        return callback(new Error('请输入必填项！'))
      } else {
        return callback()
      }
    }
    return {
      temp: {},
      dialogAdd: true,
      groupOptions: [],
      // 弹框部分
      AddDialogForm: [
        {label: '井口编号', key: 'sn'},
        {label: '井口名称', key: 'name'},
        {label: '所属部门', key: 'group_id'},
        {label: '井口经度', key: 'lng'},
        {label: '井口纬度', key: 'lat'},
        {label: '备注', key: 'remark'}
      ],
      // message:存放的是提示信息
      // validator:回调函数，函数里写判断条件
      rules: {
        sn: [{required: true, trigger: 'blur', validator: validateSpace}],
        name: [{required: true, message: '请输入正确的井口名称', trigger: 'blur'}],
        group_id: [{required: true, message: '请选择部门', trigger: 'blur', validator: validateSpace}]
      },
    }
  },
}
</script>