<template>
    <div>
        <div>
            <div>标题<input v-model="title"></input></div>
            <textarea v-model="content" style="width: 100%;height: 50rem"></textarea>
        </div>
        <button @click="add_speech">保存</button>
    </div>
</template>

<script>
    export default {
        name: "add_diary",
        data() {
            return {
                title: "",
                content: "",
            }
        },
        methods: {
            async add_speech() {
                let data = {'title': this.title, "content": this.content}
                let url = '/api/message_api/add_speech';
                let result = await this.$postJson(url, data);
                if (result.data.code) {
                    await this.$router.push({path: '/diary/diary_list'})
                } else {
                    alert(result.data.data)
                }
            },
        },
        created() {
        }
    }
</script>

<style scoped>

</style>
