<template>
    <div>
        <div>{{diary.title}}</div>
        <div>{{diary.create_time}}</div>
        <div>{{diary.content}}</div>
    </div>
</template>

<script>
    export default {
        name: "diary_info",
        data() {
            return {
                id: "",
                diary: {}
            }
        },
        methods: {
            async get_diary_info() {
                let url = '/api/message_api/get_speech_by_id';
                let data = {id: this.id}
                let result = await this.$get(url, data);
                this.diary = result.data.data;
            },
        },
        mounted: function () {
            this.id = this.$route.params.id
            this.get_diary_info()
        }
    }
</script>

<style scoped>

</style>
