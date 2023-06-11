<!-- views/CreateView.vue -->
<template>
  <div>
    <br>
    <h1 class="createname">자유게시판 작성</h1>
    <br>
    <form @submit.prevent="createFreeBoard">
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
  name: 'FreeCreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createFreeBoard() {
      const title = this.title
      const content = this.content

      
      
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/freeboard/`,
        data: { title, content },
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then(() => {
        this.$router.push({name: 'FreeView'})
      })
      .catch((err) => {
        console.log(err)
        if (!title) {
        alert('제목 입력해주세요')
      } if (!content) {
        alert('내용을 입력해주세요')
      }
      })
    }
  }
}
</script>

<style>
.font1 {
  font-family: 'Gugi', cursive;
}
.font2{
  font-family: 'Black Han Sans', sans-serif;
}

.createname{
  color:gold;
  font-family: 'Gugi', cursive;
  font-size: 70px;
}

</style>
