<template>
  <div class='container'>
    <h1>영화추천</h1>
    <hr>
    <br>
    <HottestMovie />
    <RatingNaver />
    <hr>
    <RatingTmdb />
    <hr>
    <GroupGenre @search-genre="searchGenre" />
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

import GroupGenre from '@/components/movieRecommend/GroupGenre.vue'
import RatingNaver from '@/components/movieRecommend/RatingNaver.vue'
import RatingTmdb from '@/components/movieRecommend/RatingTmdb.vue'
import HottestMovie from '@/components/movieRecommend/HottestMovie.vue'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieRecommend',
  components: {
    GroupGenre,
    RatingNaver,
    RatingTmdb,
    HottestMovie
  },
  data() {
    return {
      movies: []
    }
  },
  methods: {
    searchGenre: function (genreKeyword) {
      axios.get(SERVER_URL + "/movies/")
        .then(res => {
          const resultMovies = res.data.filter(movie => movie.genre.includes(genreKeyword))
          this.movies = _.sampleSize(resultMovies, 6)
        })
        .catch(err => console.error(err.response))
    }
  },
}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Raleway:400,500,800);
figure.snip1436 {
  font-family: 'Raleway', Arial, sans-serif;
  position: relative;
  overflow: hidden;
  margin: 10px;
  min-width: 230px;
  max-width: 315px;
  max-height: 230px;
  width: 100%;
  color: #000000;
  text-align: left;
  background-color: rgb(238, 238, 238);
  font-size: 16px;
}
figure.snip1436:hover {
  border: 2px solid black;
  border-radius: 10px;
}
figure.snip1436 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
}
figure.snip1436 img {
  max-width: 100%;
  -webkit-transition-delay: 0.2s;
  transition-delay: 0.2s;
  backface-visibility: hidden;
}
figure.snip1436 figcaption {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  -webkit-transform: scale(0.5) translate(0%, -50%);
  transform: scale(0.5) translate(0%, -50%);
  -webkit-transform-origin: 50% 0%;
  -ms-transform-origin: 50% 0%;
  transform-origin: 50% 0%;
  z-index: 1;
  opacity: 0;
  padding: 0 30px;
}
figure.snip1436 h3,
figure.snip1436 p {
  line-height: 1.5em;
}
figure.snip1436 h3 {
  margin: 0;
  font-weight: 800;
  text-transform: uppercase;
}
figure.snip1436 p {
  font-size: 0.8em;
  font-weight: 500;
  margin: 0 0 15px;
}
figure.snip1436 .read-more {
  border: 2px solid #000000;
  padding: 0.5em 1em;
  font-size: 0.8em;
  text-decoration: none;
  color: #000000;
  display: inline-block;
}
figure.snip1436 .read-more:hover {
  background-color: #000000;
  color: #ffffff;
}
figure.snip1436:hover img,
figure.snip1436.hover img {
  -webkit-animation: snip1436 0.45s linear forwards;
  animation: snip1436 0.45s linear forwards;
  -webkit-animation-iteration-count: 1;
  animation-iteration-count: 1;
}
figure.snip1436:hover figcaption,
figure.snip1436.hover figcaption {
  -webkit-transform: scale(1) translate(0, -50%);
  transform: scale(1) translate(0, -50%);
  opacity: 1;
  -webkit-transition-delay: 0.35s;
  transition-delay: 0.35s;
}
@-webkit-keyframes snip1436 {
  50% {
    -webkit-transform: scale(0.8) translateX(0%);
    transform: scale(0.8) translateX(0%);
    opacity: 0.5;
  }
  100% {
    -webkit-transform: scale(0.8) translateX(-150%);
    transform: scale(0.8) translateX(-150%);
    opacity: 0.5;
  }
}
@keyframes snip1436 {
  50% {
    -webkit-transform: scale(0.8) translateX(0%);
    transform: scale(0.8) translateX(0%);
    opacity: 0.5;
  }
  100% {
    -webkit-transform: scale(0.8) translateX(-150%);
    transform: scale(0.8) translateX(-150%);
    opacity: 0.5;
  }
}
</style>