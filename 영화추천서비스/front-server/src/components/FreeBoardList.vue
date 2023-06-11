<template>
  <div class="freeboard-list">
    <h3 class="listtitle">게시글 목록</h3>
    <br>
    <hr style="color:white">
    <br>
    <FreeBoardListItem 
    v-for="freeboard in freeboards" :key="freeboard.id" :freeboard="freeboard"
    />
  </div>
</template>

<script>
import FreeBoardListItem from '@/components/FreeBoardListItem'

export default {
  name: 'FreeBoardList',
  components: {
    FreeBoardListItem,
  },
  computed: {
    freeboards() {
        return this.$store.state.freeboards
    }
  }
}
</script>

<style>
/* hr{
  height: 2px;
  color: white;
  background-color: white;
  border: none;
} */
.freeboard-list {
    text-align: start;
}
.font1 {
  font-family: 'Gugi', cursive;
}
.font2{
  font-family: 'Black Han Sans', sans-serif;
}
.listtitle{
  font-family: 'Gugi', cursive;
  color: white;
  font-size: 60px;
}
</style>
