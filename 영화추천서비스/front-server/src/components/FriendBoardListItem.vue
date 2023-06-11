<template>
    <div>
      <p class="boardlistitem">{{ friendboard.title }}</p>
      <p class="boardlistitemcontent">{{friendboard.content.slice(0,20)}}</p>
      <router-link class="goboard" :to="{ name: 'FriendDetailView',params: {id: friendboard.id }}"> [게시물가기]   </router-link>
      <hr style="color:white">
    </div>
</template>

<script>
export default {
  name: 'FriendBoardListItem',
  props: {
    friendboard: Object,
  }
}
</script>

<style>
.boardlistitem{
  color: white;
  font-family: 'Black Han Sans', sans-serif;
  font-size: 35px;
}
.goboard{
  font-family: 'Black Han Sans', sans-serif;
  color:rgb(154, 138, 243);
  font-size: 20px;
}
.boardlistitemcontent{
  font-family: 'IBM Plex Sans KR', sans-serif;
  color: white;
  font-size: 2  0px;
}
</style>
