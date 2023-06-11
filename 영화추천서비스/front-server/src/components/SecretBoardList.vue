<template>
  <div class="secretboard-list">
    <h3 class="listtitle">게시글 목록</h3>
    <br>
    <hr style="color:white">
    <br>
    <SecretBoardListItem 
    v-for="secretboard in secretboards" :key="secretboard.id" :secretboard="secretboard"
    />
  </div>
</template>

<script>
import SecretBoardListItem from '@/components/SecretBoardListItem'

export default {
  name: 'SecretBoardList',
  components: {
    SecretBoardListItem,
  },
  computed: {
    secretboards() {
       return this.$store.state.secretboards
    }
  }
}
</script>

<style>
hr{
  height: 2px;
  color: white;
  background-color: white;
  border: none;
}
.secretboard-list {
    text-align: start;
}
.listtitle{
  font-family: 'Gugi', cursive;
  color: white;
  font-size: 60px;
}
hr{
  color:white;
}
</style>
