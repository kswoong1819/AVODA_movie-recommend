<template>
  <div>
    <h2>유저 평점 순</h2>
    <div class="row d-flex justify-content-center">
      <figure v-for="movie in movies" :key="movie.id" class="snip1436 col-6 col-md-4 col-lg-2">
        <img v-if="movie.image" :src="movie.image" class="img-thumbnail" style="height: 15rem; width: 11rem;" :alt="movie.title" />
        <img v-if="!movie.image" src="@/assets/replace.jpg" style="height: 15rem; width: 11rem;" :alt="movie.title" />
        <figcaption>
          <p>{{ movie.title }}</p>
          <p>{{ movie.subtitle }}</p>
          <router-link type="button" class="read-more" :to="{ name: 'MovieDetail', params: {movie_title : movie.title, movie_id : movie.id } }">영화 상세</router-link>
        </figcaption>
      </figure>
    </div>
  </div>
</template>

<script>
import axios from "axios"

const SERVER_URL = "http://127.0.0.1:8000"

export default {
  name: "HottestMovie",
  data: function() {
    return {
      movies: [],
      total: {}
    }
  },
  methods: {
    ratingSort: function() {
      let i = 1
      for (i=1; i<127; ++i) {
        axios.get(SERVER_URL + "/movies/" +`${i}`+ "/review/")
          .then(res => {
            if (res.data.length > 1) {
              this.movies.push(res.data[0].movie)
              // res.data.forEach((movie) => {
              //   if (`id_${movie.movie.id}` in this.total) {
              //     this.total[`id_${movie.movie.id}`] += movie.rank
              //   } else {
              //     this.total[`id_${movie.movie.id}`] = movie.rank
              //   }
              // })
            }
          })
          .catch(() => {})
      }
    }
  },
  created() {
    this.ratingSort();
  }
};
</script>

<style>
</style>