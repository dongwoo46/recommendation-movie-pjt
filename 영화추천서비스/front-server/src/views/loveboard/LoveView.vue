<template>
  <div>
    <h1 class="boardname">연애게시판</h1>
    <div>당신의 사랑을 찾으세요</div>
    <br>
    <router-link :to="{ name: 'LoveCreateView' }">[CREATE]</router-link>
    <LoveBoardList />
    <hr>

  </div>
</template>

<script>
import LoveBoardList from '@/components/LoveBoardList.vue'

export default {
  name: 'LoveView',
  components: {
    LoveBoardList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getLoveBoards()
  },
  methods: {
    getLoveBoards() {
      
      if (this.isLogin) {
        this.$store.dispatch('getLoveBoards')
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

</style>
