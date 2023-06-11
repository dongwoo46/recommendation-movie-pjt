<template>
  <div class="friendboard-list">
    <h3 class="listtitle">게시글 목록</h3>
    <br>
    <hr style="color:white;">
    <br>
    <FriendBoardListItem 
    v-for="friendboard in friendboards" :key="friendboard.id" :friendboard="friendboard"
    />
  </div>
</template>

<script>
import FriendBoardListItem from '@/components/FriendBoardListItem'

export default {
  name: 'FriendBoardList',
  components: {
    FriendBoardListItem,
  },
  computed: {
    friendboards() {
       return this.$store.state.friendboards
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
.friendboard-list {
    text-align: start;
}
.listtitle{
  font-family: 'Gugi', cursive;
  color: white;
  font-size: 60px;
}
</style>
