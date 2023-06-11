<template>
  <div>
    <!-- <div id="app" class="bg-black" :style="myStyle">
      <div id="nav" class="navbar bg-dark navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <router-link to="/" style="text-decoration: none;">
          <img src="./assets/logo.png" alt="Logo" style="max-height: 100%; width: auto;" class="AppLogo">
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link :to="{ name: 'CommunityView' }" style="text-decoration: none;">Community</router-link>
            </li>
            <span v-if="isLogin">
              <li class="nav-item">
                <router-link :to="{ name: 'ProfileView' }" class="d-flex align-items-end flex-column" id="username" style="color:white; text-decoration: none;">{{ $store.state.userName }} 님 환영합니다.</router-link>
              </li>
              <li class="nav-item">
                <router-link to="#" @click.native="logout" class="d-flex align-items-end flex-column" style="color:white; text-decoration: none;">Logout</router-link>
              </li>
            </span>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
        </div>
      </div>
      </div>
      </div> -->
    <div id="app" class="bg-black" :style="myStyle">
      <div id="nav" class="navbar bg-dark px-3 mb-3 d-flex">
        <router-link to="/" style="text-decoration: none;">
          <img src="./assets/logo.png" alt="Logo" style="max-height: 100%; width: auto;" class="AppLogo">
        </router-link>
        <div style="justify-content-center" class="gugi">
          <router-link :to="{ name: 'FreeView' }" style="text-decoration: none;" class="p-3">자유게시판</router-link>
          <router-link :to="{ name: 'LoveView' }" style="text-decoration: none;" class="p-3">연애게시판</router-link>
          <router-link :to="{ name: 'SecretView' }" style="text-decoration: none;" class="p-3">비밀게시판</router-link>
          <router-link :to="{ name: 'FriendView' }" style="text-decoration: none;" class="p-3">친구게시판</router-link>
          <router-link :to="{ name: 'SignupView' }" style="text-decoration: none;">Signup</router-link>
        </div>
          <span v-if="this.$store.state.token">
            <router-link :to="{ name: 'ProfileView', params: { username: this.$store.state.userName }}" class="d-flex align-items-end flex-column" id="username" style="color:white; text-decoration: none;">
              <img :src="profileSmallImg" alt="Profile" class="profileSmallImg" v-if="profileSmallImg">
              <img src="./assets/profileImg.png" alt="Profile" class="profileSmallImg" v-else>
              <span class="font3" style="font-size:20px;">
                {{ $store.state.userName }} 님 환영합니다.
              </span>
            </router-link>
            <router-link to="#" @click.native="logout" class="d-flex align-items-end flex-column font3" style="color:white; font-size:15px; text-decoration: none;">Logout</router-link>
          </span> 
          <span v-else>
            <router-link class="font1" :to="{ name: 'LoginView' }">Login</router-link> 
          </span>
      </div>
      <router-view @login="isLogin=true" />
      <div class="vue-container">
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function () {
    return {
      myStyle: {
        backgroundColor: "#16a085"
      },
      profileSmallImg: null,
    }
  },
  methods: {

    logout() {
      localStorage.removeItem(`${this.$store.state.userName}`)
      this.$store.dispatch('logout')
    },
  },
  created: function() {

    if (localStorage.getItem(`${this.$store.state.userName}`)){
      this.profileSmallImg = localStorage.getItem(`${this.$store.state.userName}`)
    }
  },
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Brush+Script&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gugi&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Gugi&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Gugi&family=IBM+Plex+Sans+KR:wght@300&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
}

#nav {
  padding: 10px;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: gold;
}

h1 {
  color: white;
}

label {
  color: white;
}

.AppLogo {
  width: 150px;
  height: 100px;
}

.vue-container{
  height: 100vh;
}

.profileSmallImg {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.nanum {
  font-size : 30px;
  font-family : 'Nanum Brush Script', cursive;
}

.gugi {
  font-family: 'Gugi', cursive;
  font-size : 30px;
}
.font1 {
  font-family: 'Gugi', cursive;
}
.font2{
  font-family: 'Black Han Sans', sans-serif;
}

.font3{
  font-family: 'IBM Plex Sans KR', sans-serif;
}

.boardname{
  color:gold;
  font-family: 'Gugi', cursive;
  font-size: 70px;
}
.detailtitle{
  color:gold;
  font-family: 'Gugi', cursive;
  font-weight: 10;
  font-size: 30px;
}
</style>
