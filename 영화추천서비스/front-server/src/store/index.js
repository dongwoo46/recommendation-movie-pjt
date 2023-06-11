import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    freeboards: [
    ],
    loveboards: [
    ],
    secretboards: [
    ],
    friendboards: [
    ],
    boards:[],
    token: null,
    userName: null,
    selectedImg: null,
    communityParams : null,
    currentUserFollowings: [],
    currentUserFollowers: [],
  },
  getters: {
    isLogin(state) {
      
      return state.token ? true : false
    }
  },
  mutations: {
    GET_FREEBOARDS(state, freeboards) {
      state.freeboards = freeboards
    },
    GET_LOVEBOARDS(state, loveboards) {
      state.loveboards = loveboards
    },
    GET_SECRETBOARDS(state, secretboards) {
      state.secretboards = secretboards
    },
    GET_FRIENDBOARDS(state, friendboards) {
      state.friendboards = friendboards
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'MovieView'})
    },
    SAVE_USERNAME(state, userName) {
      state.userName = userName
    },
    
  },
  actions: {
    // 자유게시판
    getFreeBoards(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/freeboard/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_FREEBOARDS', res.data)
          
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // 연애게시판
    getLoveBoards(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/loveboard/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_LOVEBOARDS', res.data)
          
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // 비밀게시판
    getSecretBoards(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/secretboard/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_SECRETBOARDS', res.data)
          
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // 친구게시판
    getFriendBoards(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/friendboard/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_FRIENDBOARDS', res.data)
          
        })
        .catch((err) => {
        console.log(err)
      })
    },

    
    signUp(context, payload) {
      console.log('사인업')
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERNAME', username)
        })
        .catch((err) => {
        console.log(err)
        alert('회원 정보가 유효하지 않습니다.')
        
      })
    },
    login(context, payload) {
      console.log('로그인')
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('SAVE_USERNAME', username)
        })
      .catch(err => { 
        alert('올바른 회원 정보를 입력해주세요.')
        console.log(err)
      })

    },
    logout(context) {
      axios({
        method: 'post',
        url : `${API_URL}/accounts/logout/`
      })
      .then(res => {
        console.log(res)
        context.commit('SAVE_TOKEN', null)
        context.commit('SAVE_USERNAME', null)
        router.push({ name: 'LoginView' })
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})

