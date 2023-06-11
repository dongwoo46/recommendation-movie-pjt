<template>
  <div>
    <h1 class="font1" style="color:gold; font-size:50px;">SignUp</h1>
    <br>
    <form class="font3 form-container" @submit.prevent="signUp">
      <div>
        <label class="labels" for="username">사용자 이름: </label>
        <input type="text" id="username" v-model="userdata.username">
      </div>

      <div>
        <label class="labels" for="password">비밀번호: </label>
        <input  type="password" id="password" v-model="userdata.password1">
      </div>

      <div>
        <label class="labels" for="passwordConfirm">비밀번호 확인: </label>
        <input type="password" id="passwordConfirm" v-model="userdata.password2" @keyup.enter="signUp">
      </div>

      <button type="button" class="btn btn-success">회원가입</button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'SingupView',
  data: function () {
    return {
      userdata: {
        username: null,
        password1: null,
        password2: null,
      }
    }
  },

  methods: {
    signUp: function () {
      const username = this.userdata.username
      const password1 = this.userdata.password1
      const password2 = this.userdata.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>
.font1 {
  font-family: 'Gugi', cursive;
}
.font2{
  font-family: 'Black Han Sans', sans-serif;
}

.font3{
  font-family: 'IBM Plex Sans KR', sans-serif;
}
.form-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid gold;
  border-radius: 5px;
  background-color: #fff;
}

.labels {
  color:black;
  font-size: large;
  font-family: 'IBM Plex Sans KR', sans-serif;
}
</style>