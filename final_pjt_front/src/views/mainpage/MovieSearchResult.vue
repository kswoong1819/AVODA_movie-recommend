<template>
  <div class="mt-4 row">
    <div v-for="movie in movies" :key="movie.id" class="col-md-10 col-lg-9 col-xl-6 mb-r">

      <div class="card card-body mb-3">
        <div class="media d-block d-md-flex">
          <img class="d-flex avatar-2 mb-md-0 mb-3 mx-auto" :src="movie.image" :alt="movie.title">
          <div class="media-body text-center text-md-left ml-md-3 ml-0">
            <h3>{{ movie.title }}</h3>
            <p>{{ movie.subtitle }}</p>
            <p>{{ movie.director }}</p>
            <p>{{ movie.actor }}</p>
            <router-link type="button" class="btn btn-primary btn-md" :to="{ name: 'MovieDetail', params: {movie_title : movie.title, movie_id : movie.id } }">
              영화 상세
            </router-link>   
            <span class="badge"><i class="fas fa-user" aria-hidden="true"> {{ movie.userRating }}</i></span>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieSearchResult',
  props: {
    movies: Array,
  },  
}
</script>

<style>
@media (min-width: 768px) {
    .media .avatar-2 {
        width: 130px;
    }
}

@media (max-width: 767px) {
    .media .avatar-2 {
        width: 160px;
    }
}

.card img.rounded-circle {
    border-radius: 50%;
}

.media-body {
  font-family: 'Noto Serif KR', serif;
}
</style>