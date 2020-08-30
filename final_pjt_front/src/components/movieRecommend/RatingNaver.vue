<template>
  <div>
    <h2>네이버 평점 순</h2>
    <div class="row d-flex justify-content-center">
      <figure  v-for="movie in movies" :key="movie.id" class="snip1436 col-6 col-md-4 col-lg-2">
        <img v-if="movie.image" :src="movie.image" class="img-thumbnail" style="height: 15rem; width: 11rem;" :alt="movie.title">
        <img v-if="!movie.image" src="@/assets/replace.jpg" style="height: 15rem; width: 11rem;" :alt="movie.title">
        <figcaption>
          <p>{{ movie.title }}</p>
          <p>{{ movie.subtitle }}</p>
          <router-link type="button" class="read-more" :to="{ name: 'MovieDetail', params: {movie_title : movie.title, movie_id : movie.id } }">
            영화 상세
          </router-link> 
        </figcaption>
      </figure >
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'RatingNaver',
  data: function () {
    return {
      movies: [],
    }
  },
  methods: {
    ratingSort: function () {
      axios.get(SERVER_URL + "/movies/")
        .then((res) => {
          const ratingResult = res.data.filter(movie => movie.userRating > 9)
          this.movies = _.sampleSize(ratingResult, 6)
        })
        .catch(err => console.error(err.response))
    }
  },
  created() {
    this.ratingSort()
  }
}
</script>

<style>

</style>