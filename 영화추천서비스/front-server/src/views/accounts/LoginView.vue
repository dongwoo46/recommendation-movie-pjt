<template>
  <div>
    <h1 class="font1" style="color:gold; font-size:50px;">Login</h1>
    <br>
    <form @submit.prevent="login">
      <div>
        <label for="username">username: </label>
        <input type="text" id="username" v-model="userdata.username"><br>
      </div>

      <div>
        <label for="password">password: </label>
        <input type="password" id="password" v-model="userdata.password" @keyup.enter="login">  
      </div>

      <button type="button" class="btn btn-success">Login</button>
    </form>
    </div>
</template>

<script>

export default {
  name: 'LoginView',
  data: function () {
    return {
      userdata: {
        username: null,
        password: null,
      },
    }
  },
  methods: {
    login: function () {

      const username = this.userdata.username
      const password = this.userdata.password
      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    },
  }
}
</script>