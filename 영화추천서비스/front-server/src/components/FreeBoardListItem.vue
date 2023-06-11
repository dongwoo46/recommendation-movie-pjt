<template>
    <div>
      <p class="boardlistitem">{{ freeboard.title }}</p>
      <p class="boardlistitemcontent">{{freeboard.content.slice(0,20)}}</p>
      <router-link class="goboard" :to="{ name: 'FreeDetailView',params: {id: freeboard.id }}"> [게시물가기]   </router-link>
      <hr style="color:white">
    </div>
</template>

<script>

export default {
  name: 'FreeBoardListItem',
  props: {
    freeboard: Object,
  },
  methods: {
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
