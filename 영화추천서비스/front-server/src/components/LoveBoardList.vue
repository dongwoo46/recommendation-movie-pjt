<template>
  <div class="loveboard-list">
    <h3 class="listtitle">게시글 목록</h3>
    <br>
    <hr style="color:white">
    <br>
    <LoveBoardListItem 
    v-for="loveboard in loveboards" :key="loveboard.id" :loveboard="loveboard"
    />
  </div>
</template>

<script>
import LoveBoardListItem from '@/components/LoveBoardListItem'

export default {
  name: 'LoveBoardList',
  components: {
    LoveBoardListItem,
  },
  computed: {
    loveboards() {
       return this.$store.state.loveboards
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
.loveboard-list {
    text-align: start;
}
.listtitle{
  font-family: 'Gugi', cursive;
  color: white;
  font-size: 60px;
}
</style>
