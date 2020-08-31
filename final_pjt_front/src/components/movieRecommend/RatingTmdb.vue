<template>
  <div>
    <h2>TMDB 평점 순</h2>
    <div class="row d-flex justify-content-center">
      <figure v-for="movie in movies" :key="movie.id" class="snip1436 col-6 col-md-4 col-lg-2">
        <img
          v-if="movie.poster_path"
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          class="img-thumbnail"
          style="height: 15rem; width: 11rem;"
          :alt="movie.title"
        />
        <img
          v-if="!movie.imposter_pathage"
          src="@/assets/replace.jpg"
          style="height: 15rem; width: 11rem;"
          :alt="movie.title"
        />
        <figcaption>
          <p>{{ movie.title }}</p>
          <p>{{ movie.subtitle }}</p>
          <router-link
            type="button"
            class="read-more"
            :to="{ name: 'MovieDetail', params: {movie_title : movie.title, movie_id : movie.id } }"
          >영화 상세</router-link>
        </figcaption>
      </figure>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import _ from "lodash"

const TMDB_API_URL = "https://api.themoviedb.org/3/trending/all/day"
const TMDB_API_KEY = "---"

export default {
  name: "RatingTmdb",
  data: function() {
    return {
      movies: [],
    }
  },
  methods: {
    ratingSort() {
      axios
        .get(TMDB_API_URL, {
          params: {
            api_key: TMDB_API_KEY,
            language: "ko",
          }
        })
        .then(res => {
          const ratingResult = res.data.results.filter(movie => movie.vote_average > 6.5)
          this.movies = _.sampleSize(ratingResult, 6)
        })
        .catch(err => {
          console.error(err.response)
        })
    },
  },
  created() {
    this.ratingSort()
  }
}
</script>

<style>
</style>
