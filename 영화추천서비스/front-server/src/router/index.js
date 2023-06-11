import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/movies/MovieView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import LoginView from '@/views/accounts/LoginView'
import SignupView from '@/views/accounts/SignupView'
import ProfileView from '@/views/profile/ProfileView'
import FollowerView from '@/views/profile/FollowerView'
import FollowingView from '@/views/profile/FollowingView'

// 자유게시판
import FreeView from '@/views/freeboard/FreeView'
import FreeDetailView from '@/views/freeboard/FreeDetailView'
import FreeCreateView from '@/views/freeboard/FreeCreateView'

// 연애게시판
import LoveView from '@/views/loveboard/LoveView'
import LoveDetailView from '@/views/loveboard/LoveDetailView'
import LoveCreateView from '@/views/loveboard/LoveCreateView'

// 비밀게시판
import SecretView from '@/views/secretboard/SecretView'
import SecretDetailView from '@/views/secretboard/SecretDetailView'
import SecretCreateView from '@/views/secretboard/SecretCreateView'

// 친구게시판
import FriendView from '@/views/friendboard/FriendView'
import FriendDetailView from '@/views/friendboard/FriendDetailView'
import FriendCreateView from '@/views/friendboard/FriendCreateView'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView,
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView,
  },
  {
    path: '/moviedetail/:moviePk',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  // 자유 게시판
  {
    path: '/freeboard',
    name: 'FreeView',
    component: FreeView,
  },
  {
    path: '/freeboard/:id',
    name: 'FreeDetailView',
    component: FreeDetailView,
  },

  {
    path: '/freeboard/create',
    name: 'FreeCreateView',
    component: FreeCreateView,
  },
  // 연애 게시판
  {
    path: '/loveboard',
    name: 'LoveView',
    component: LoveView,
  },
  {
    path: '/loveboard/:id',
    name: 'LoveDetailView',
    component: LoveDetailView,
  },

  {
    path: '/loveboard/create',
    name: 'LoveCreateView',
    component: LoveCreateView,
  },
  // 비밀 게시판
  {
    path: '/secretboard',
    name: 'SecretView',
    component: SecretView,
  },
  {
    path: '/secretboard/:id',
    name: 'SecretDetailView',
    component: SecretDetailView,
  },

  {
    path: '/secretboard/create',
    name: 'SecretCreateView',
    component: SecretCreateView,
  },
  // 친구 게시판
  {
    path: '/friendboard',
    name: 'FriendView',
    component: FriendView,
  },
  {
    path: '/friendboard/:id',
    name: 'FriendDetailView',
    component: FriendDetailView,
  },

  {
    path: '/friendboard/create',
    name: 'FriendCreateView',
    component: FriendCreateView,
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/profile/:username/followerList',
    name: 'FollowerView',
    component: FollowerView,
  },
  {
    path: '/profile/:username/followingList',
    name: 'FollowingView',
    component: FollowingView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
