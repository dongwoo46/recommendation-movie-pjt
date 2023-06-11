<template>
  <div>
    <h1>{{this.$route.params.username}}님의 팔로잉 리스트</h1>
    <div v-for="(following, index) in this.$store.state.currentUserFollowings" :key="index">
      <router-link
        :to="{name: 'ProfileView', params: { username: following }}"
        style="text-decoration: none;"
        >
        <p>{{ following }}</p>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
    name: 'FollowingView',
    create() {
        console.log(this.followings)
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