<template>
  <div>
    <h1>{{this.$route.params.username}}님의 팔로워 리스트</h1>
    <div v-for="(follower, index) in this.$store.state.currentUserFollowers" :key="index">
      <router-link
        :to="{name: 'ProfileView', params: { username: follower }}"
        style="text-decoration: none;"
        >
        <p>{{ follower }}</p>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
    name: 'FollowerView',
    create() {
        console.log(this.followers)
    }
}
</script>

<style>
.boardname{
  color:gold;
  font-family: 'Gugi', cursive;
  font-size: 60px;
}
.follows{
  font-size: 30px;
  font-family: 'IBM Plex Sans KR', sans-serif;
}
</style>