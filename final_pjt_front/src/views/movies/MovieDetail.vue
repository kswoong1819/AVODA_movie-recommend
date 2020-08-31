<template>
  <div>
    <br>
    <hr/>
    
    <div class="mt-4 row">
      <div class="card card-body mb-3">
        <div class="media d-block d-md-flex">
          <img class="d-flex avatar-2 mb-md-0 mb-3 mx-auto" style="height: 30vw; width: 20vw;" :src="`https://image.tmdb.org/t/p/w500${movie_info.poster_path}`" :alt="movie.title">
          <div class="media-body text-center text-md-left ml-md-3 ml-0">
            <h2>{{ movie_info.title }}</h2>
            <p>{{ movie.subtitle }}</p>

            <span>네이버 평점 : {{movie.userRating}}</span>
            <k-progress :percent="movie.userRating*10" status="success" :show-text="false" active></k-progress>
            
            <span>TMDB 평점 : {{movie_info.vote_average}}</span>
            <k-progress :percent="movie_info.vote_average*10" status="error" :show-text="false" active></k-progress>

            <div class="row">
              <div class="col-lg-3">
                <div class="rating-block">
                  <h4>Average user rating</h4>
                  <h2 class="bold padding-bottom-7">{{ rank_avg }} <small>/ 5</small></h2>
                </div>
              </div>
              <div class="col-lg-9">
                <div>
                  <h4 class="d-inline">Rating breakdown </h4>
                  <button class="btn btn-dark" @click="rankInfo"><i class="fas fa-redo"></i></button>
                </div>
                <i class="fas fa-star text-warning"></i>1
                <k-progress class="d-inline" :percent="rank_info[1]*10" status="error" :show-text="false" :line-height="10" active></k-progress>
                <i class="fas fa-star text-warning"></i>2
                <k-progress class="d-inline" :percent="rank_info[2]*10" status="error" :show-text="false" :line-height="10" active></k-progress>
                <i class="fas fa-star text-warning"></i>3
                <k-progress class="d-inline" :percent="rank_info[3]*10" status="error" :show-text="false" :line-height="10" active></k-progress>
                <i class="fas fa-star text-warning"></i>4
                <k-progress class="d-inline" :percent="rank_info[4]*10" status="error" :show-text="false" :line-height="10" active></k-progress>
                <i class="fas fa-star text-warning"></i>5
                <k-progress class="d-inline" :percent="rank_info[5]*10" status="error" :show-text="false" :line-height="10" active></k-progress>
              </div>	
            </div>
          </div>
        </div>
      </div>
    </div>

    <ul class="nav nav-tabs nav-justified md-tabs indigo" id="myTabJust" role="tablist">
      <li class="nav-item">
        <a class="nav-link active" id="home-tab-just" data-toggle="tab" href="#home-just" role="tab" aria-controls="home-just"
          aria-selected="true">주요정보</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" id="profile-tab-just" data-toggle="tab" href="#profile-just" role="tab" aria-controls="profile-just"
          aria-selected="false">예고편</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" id="contact-tab-just" data-toggle="tab" href="#contact-just" role="tab" aria-controls="contact-just"
          aria-selected="false">리뷰</a>
      </li>
    </ul>
    <div class="tab-content card pt-5" id="myTabContentJust">
      <div class="tab-pane fade show active" id="home-just" role="tabpanel" aria-labelledby="home-tab-just">
        <div class="mx-5">
          <p>감독 : {{ movie.director }}</p>
          <p>배우 : {{ movie.actor }}</p>
          <p>{{ movie_info.overview }}</p>
        </div>
      </div>
      <div class="tab-pane fade" id="profile-just" role="tabpanel">
        <div class="embed-responsive embed-responsive-16by9">
          <iframe 
            class="embed-responsive-item"
            :src="`https://www.youtube.com/embed/${video.id.videoId}`"
            allowfullscreen
          ></iframe>
        </div>
      </div>
      <div class="tab-pane fade" id="contact-just" role="tabpanel" aria-labelledby="contact-tab-just">
        <div class="mx-5">
          <ReviewList :movie_id="movie.id" @get-rank="rankInfo"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewList from '@/components/movieDetail/ReviewList.vue'
// import ReviewCreate from '@/components/movieDetail/ReviewCreate.vue'


const SERVER_URL = 'http://127.0.0.1:8000'
const API_KEY = '---'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const TMDB_API_URL = 'https://api.themoviedb.org/3/search/movie'
const TMDB_API_KEY = '---'

export default {
    name : 'MovieDetail',
    data() {
      return {
        movie: {},
        video: [],
        movie_info: [],
        rank_info: null,
        rank_avg: 0,
      }
    },
    components: {
      ReviewList
    },
    methods: {
      movieDetail () {
        const movie_id = this.$route.params.movie_id
        axios.get(SERVER_URL+'/movies/'+movie_id+'/')
        .then(res => {
            this.movie = res.data
          })
          .catch(err => console.error(err.response))
      },

      inputVideos () {
        const movie_title = this.$route.params.movie_title
        this.inputValue = movie_title + ' 예고편'
        axios.get(API_URL, {
          params: {
            key: API_KEY,
            part: 'snippet',
            type: 'video',
            q: this.inputValue
          }
        })
        .then(res => {
          res.data.items.forEach(item => {
            const parser = new DOMParser()
            const doc = parser.parseFromString(item.snippet.title, 'text/html')
            item.snippet.title = doc.body.innerText
          })
          this.video = res.data.items[0]
        })
        .catch(err => {
          console.error(1)
          console.error(err)
        })
      },

      movieInfo () {
        const movie_title = this.$route.params.movie_title
        this.inputValue = movie_title
        axios.get(TMDB_API_URL, {
          params: {
            api_key: TMDB_API_KEY,
            language: 'ko',
            query: this.inputValue
          }
        })
        .then(res => {
          this.movie_info = res.data.results[0]
        })
        .catch(err => {
          console.error(2)
          console.error(err.response)
        })
      },

      rankInfo () {
        const movie_id = this.$route.params.movie_id
        let rank_cnt = [0, 0, 0, 0, 0, 0]
        let rank_total = 0
        let total_cnt = 0
        axios.get(SERVER_URL + "/movies/" +`${movie_id}`+ "/review/")
          .then(res => {
            res.data.forEach(rank => {
              rank_cnt[rank.rank] += 1
              total_cnt += 1
              rank_total += rank.rank
            })
            let avg = rank_total / total_cnt
            this.rank_avg = avg.toFixed(1)
            this.rank_info = rank_cnt
          })
          .catch(err => {
            console.error(err.response)
          })
      },
    },
    created() {      
      this.movieDetail()
      this.inputVideos()
      this.movieInfo()
      this.rankInfo()
    },
    
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@500&display=swap');

#myTabContentJust{
  font-family: 'Noto Serif KR', serif;
}
.btn-grey{
  background-color:#D8D8D8;
	color:#FFF;
}
.rating-block{
	background-color:#FAFAFA;
	border:1px solid #EFEFEF;
	padding:15px 15px 20px 15px;
	border-radius:3px;
}
.bold{
	font-weight:700;
}
.padding-bottom-7{
	padding-bottom:7px;
}
</style>
