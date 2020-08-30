import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import MovieRecommend from '../views/movies/MovieRecommend.vue'
import MovieDetail from '../views/movies/MovieDetail.vue'
import CommunityList from '../views/community/CommunityList.vue'
import CommunityDetail from '../views/community/CommunityDetail.vue'
import CommunityCreate from '../views/community/CommunityCreate.vue'
import CommunityEdit from '../views/community/CommunityEdit.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/movies/recommend',
    name: 'Recommend',
    component: MovieRecommend
   },
   {
    path: '/movies/detail',
    name: 'MovieDetail',
    component: MovieDetail
   },
   {
    path: '/community',
    name: 'Community',
    component: CommunityList
   },
   {
    path: '/community/article',
    name: 'ArticleDetail',
    component: CommunityDetail
   },
   {
    path: '/community/new',
    name: 'CreateArticle',
    component: CommunityCreate    
   },
   {
    path: '/community/article/new',
    name: 'EditArticle',
    component: CommunityEdit    
   },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
