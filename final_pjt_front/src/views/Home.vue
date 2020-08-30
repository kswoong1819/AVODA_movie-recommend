<template>
  <div class='container'>    
    <h1 class="main mt-4">AbodA</h1>
    <MovieSearch @search-movies="serchMovies" />
    <MovieSearchResult :movies="movies" />
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

import MovieSearch from './mainpage/MovieSearch.vue'
import MovieSearchResult from './mainpage/MovieSearchResult.vue'


export default {
  name: 'Home',
  data() {
    return {
      movies: []
    }
  },
  components: {
    MovieSearch,
    MovieSearchResult,
  },
  methods: {
    serchMovies: function (keyword) {
      axios.get(SERVER_URL + "/movies/")
        .then(res => {
          console.log(keyword)
          const resultMovies = res.data.filter(movie => movie.title.includes(keyword))
          this.movies = resultMovies
          console.log(this.movies)
        })
        .catch(err => console.error(err.response))
    }
  },
}
</script>

<style scope>

@import url('https://fonts.googleapis.com/css2?family=Suez+One&display=swap');
h1.main {
  color: rgb(0, 0, 0);
  font-size: 150px; 
  text-align: center;
  font-family: 'Suez One', serif;
}


</style>