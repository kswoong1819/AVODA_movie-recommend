<template>
  <div>
    <h2>영화 DB에 넣는곳</h2>
    <MovieSearch @search-movie="getMovie" />

  </div>
</template>


<script type="text/javascript" src="https://openapi.naver.com/v1/search/movie.json"></script>
<script>

const SERVER_URL = 'http://localhost:8000'
// const API_URL = '/v1/search/movie.json'
const API_URL = 'https://openapi.naver.com/v1/search/movie.json'
// const API_KEY = process.env.VUE_APP_TMDB_API_KEY

const API_KEY = process.env.VUE_APP_NAVER_API_KEY
const API_PWD = process.env.VUE_APP_NAVER_API_PWD

import axios from 'axios'
import MovieSearch from '@/components/movieCreate/MovieSearch.vue'


// npm i vue-axios-cors
// import Vue from 'vue'
// import AxiosPlugin from 'vue-axios-cors';
// Vue.use(AxiosPlugin)


// npm i cors
// const cors = require('cors');
// app.use(cors()); /* 1번*/

/* 2번 */
// app.use(cors({
//     origin: SERVER_URL,
//     credentials: true,
// }));

// ,
//         {
//         withCredentials: true,
//         }


export default {
  name : 'MovieCreate',
  components : {
      MovieSearch,
  },
  data() {
    return {
      movieData: {
        title: null,
        content: null,
      }
    };
  },
  methods: {
    createMovie() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // movie 생성은 Header: Token / Body: { title: , content: }
      axios.post(SERVER_URL + '/movies/', this.movieData, config)
        .then(res => { 
          console.log(res.data) 
          this.$router.push({ name: 'List' })
        })
        .catch(err => console.log(err.response.data))
    },
    getMovie(keyword) {
        console.log(keyword)
        axios.get(API_URL, {
        params: {
          query: keyword,
        //   display: 5
        }, 
        headers: { 
            'X-Naver-Client-Id': API_KEY, 
            'X-Naver-Client-Secret': API_PWD,
            // 'Access-Control-Allow-Origin': '*',        
        }
        }) .then((response)=>{        
        console.log(response)
        // this.videos = response.data.items
      }).catch((error)=>{        
        console.log(error.response.data)
      })
    },   
  },
}
</script>

<style>

</style>