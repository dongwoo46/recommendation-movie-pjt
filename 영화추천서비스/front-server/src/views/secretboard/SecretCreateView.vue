<!-- views/CreateView.vue -->
<template>
  <div>
    <br>
    <h1 class="createname">비밀게시판 작성</h1>
    <br>
    <form @submit.prevent="createSecretBoard">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SecretCreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createSecretBoard() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } 
      
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/secretboard/`,
        data: { title, content },
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'SecretView'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>
