<template>
  <div>
    <nav class="sticky-top navbar navbar-expand-lg navbar-light">
      <router-link class="navbar-brand home-nav home-btn" to="/">AbodA</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto home-nav">
          <li class="nav-item active">
            <router-link class="nav-link" :to="{ name: 'Recommend' }">영화 추천 </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Community' }">커뮤니티 </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" v-if="!isLoggedIn" :to="{ name: 'Login' }">로그인 </router-link> 
          </li>
          <li class="nav-item">
            <router-link class="nav-link" v-if="!isLoggedIn" :to="{ name: 'Signup' }">회원가입</router-link> 
          </li>
          <li class="nav-item">
            <router-link class="nav-link" v-if="isLoggedIn" to="/accounts/logout" @click.native="logout" >로그아웃</router-link> 
          </li>
        </ul>
      </div>
    </nav>
    <router-view 
      class="container"
      @submit-login-data="login" 
      @submit-signup-data="signup" 
    />
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
    }
  },
  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },

    signup(signupData) {
       axios.post(SERVER_URL + '/rest-auth/signup/', signupData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home' })
        })
        .catch(() => {
          alert('입력된 정보를 확인해주세요.')
        })
    },

    login(loginData) {
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home' })
        })
        .catch(() => {
          alert('아이디와 비밀번호를 확인하고 다시 로그인 해주세요.')
        })
    },

    logout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/rest-auth/logout/', null, config)
        .catch(err => console.log(err.response))
        .finally(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home' })
        })
    },
  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');

body {
 font-family: 'Roboto Condensed', sans-serif;
}

.nav-item {
 font-family: 'Do Hyeon', sans-serif;
}

.nav {
  background: rgb(206, 205, 205);
}

.home-nav {
  font-size: 1.5rem;  
}

.home-btn {  
  color: rgb(0, 0, 0);  
  text-align: center;
  font-family: 'Suez One', serif;
}

.btn-primary {
  background-color: #6c757d;
  border-color: #6c757d;
}

</style>
