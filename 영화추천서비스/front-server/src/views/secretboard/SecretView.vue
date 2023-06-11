<template>
  <div>
    <h1 class="boardname">비밀게시판</h1>
    <div>자신만의 비밀을 말해보세요</div>
    <router-link :to="{ name: 'SecretCreateView' }">[CREATE]</router-link>
    <SecretBoardList />
    <hr>

  </div>
</template>

<script>
import SecretBoardList from '@/components/SecretBoardList.vue'

export default {
  name: 'SecretView',
  components: {
    SecretBoardList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getSecretBoards()
  },
  methods: {
    getSecretBoards() {
      
      if (this.isLogin) {
        this.$store.dispatch('getSecretBoards')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'LoginView' })
      }


      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동

    }
  }
}
</script>

<style>
.createname{
  color:gold;
  font-family: 'Gugi', cursive;
  font-size: 70px;
}
</style>
