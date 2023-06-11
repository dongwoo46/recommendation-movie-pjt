<template>
  <div>
    <h1 class="boardname">자유게시판</h1>
    <div>자유롭게 작성하세요</div>
    <br>
    <router-link class="font2" :to="{ name: 'FreeCreateView' }">[CREATE]</router-link>
    <FreeBoardList />
    <hr>

  </div>
</template>

<script>
import FreeBoardList from '@/components/FreeBoardList.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FreeView',
  components: {
    FreeBoardList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getFreeBoards()
  },
  methods: {
    getFreeBoards() {
      if (this.isLogin) {
        // this.$store.dispatch('getFreeBoards')
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/articles/freeboard/`,
          headers: {
            Authorization: `Token ${ this.$store.state.token }`
            }
            })
          .then((res) => {
            this.$store.state.freeboards = res.data
            console.log(res.data)
            })
          .catch((err) => {
            console.log(err)
          })

      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'LoginView' })
      }
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

.boardname{
  color:gold;
  font-family: 'Gugi', cursive;
  font-size: 70px;
}
</style>
