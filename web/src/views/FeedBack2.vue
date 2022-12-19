<template>
  <!--  https://www.cnblogs.com/tanshao/p/9487785.html-->
  <!--富文本编辑器-->
  <el-form ref="form" :model="form" label-width="8rem">
    <el-form-item label="内容">
      <quill-editor v-model="value" ref="myQuillEditor" :options="editorOption" @change="onEditorChange($event)">
      </quill-editor>
    </el-form-item>
  </el-form>
</template>
<script>
const toolbarOptions = [
  ['bold', 'italic', 'underline', 'strike'], // toggled buttons
  ['blockquote', 'code-block'],
  [{
    'header': 1
  }, {
    'header': 2
  }], // custom button values
  [{
    'list': 'ordered'
  }, {
    'list': 'bullet'
  }],
  [{
    'script': 'sub'
  }, {
    'script': 'super'
  }], // superscript/subscript
  [{
    'indent': '-1'
  }, {
    'indent': '+1'
  }], // outdent/indent
  [{
    'direction': 'rtl'
  }], // text direction

  [{
    'size': ['small', false, 'large', 'huge']
  }], // custom dropdown
  [{
    'header': [1, 2, 3, 4, 5, 6, false]
  }],

  [{
    'color': []
  }, {
    'background': []
  }], // dropdown with defaults from theme
  [{
    'font': []
  }],
  [{
    'align': []
  }],
  ['link', 'image', 'video'],
  ['clean'] // remove formatting button
]
export default {
  data() {
    return {
      form: {},
      value: '',
      editorOption: {
        placeholder: '请输入院校简介',
        theme: 'snow', // or 'bubble'
        modules: {}
//         modules: {
//           toolbar: {
//             container: toolbarOptions, // 工具栏
//             handlers: {
//               'image': function (value) {
//                 if (value) {
// //										console.log(this.serverUrl)
//                   document.querySelector('.avatar-uploader').click()
// //												                    alert(1)
//                 } else {
//                   this.quill.format('image', false);
//                 }
//               },
//               'video': function (value) {
//                 if (value) {
//                   alert(2)
//                 } else {
//                   this.quill.format('image', false);
//                 }
//               },
//             }
//           }
//         }
      },
    }
  },
  methods: {
    onEditorChange() {
      console.log(this.value)
      let content = this.value
      this.$emit('getText', content)
    }
  }
}
</script>