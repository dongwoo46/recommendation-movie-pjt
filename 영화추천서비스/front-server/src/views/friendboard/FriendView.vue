<template>
  <div>
    <h1 class="boardname">친구게시판</h1>
    <div>새로운 친구를 만들어봐요</div>
    <br>
    <router-link :to="{ name: 'FriendCreateView' }">[CREATE]</router-link>
    <FriendBoardList />
    <hr>

  </div>
</template>

<script>
import FriendBoardList from '@/components/FriendBoardList.vue'

export default {
  name: 'FriendView',
  components: {
    FriendBoardList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getFriendBoards()
  },
  methods: {
    getFriendBoards() {
      
      if (this.isLogin) {
        this.$store.dispatch('getFriendBoards')
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
