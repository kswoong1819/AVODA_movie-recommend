<template>
  <div>
    <div class="input-group">
      <div class="input-group-prepend">
        <span class="input-group-text" id="basic-addon1"><i class="far fa-comment-dots"></i></span>
      </div>
      <input v-model="reviewData.content" class="form-control" placeholder="댓글을 작성하세요." id="content" rows="3" />
      <button @click="createReview" type="submit" class="btn btn-dark">작성</button>
    </div>

    <div class="form-check form-check-inline" >
      <input class="form-check-input" v-model="reviewData.rank" type="radio" name="exampleRadios" id="exampleRadios1" value="1" checked>
      <label class="form-check-label" for="exampleRadios1" ><i class="fas fa-star text-warning"></i></label>
    </div>
    <div class="form-check form-check-inline" >
      <input class="form-check-input" v-model="reviewData.rank" type="radio" name="exampleRadios" id="exampleRadios2" value="2" checked>
      <label class="form-check-label" for="exampleRadios2" ><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></label>
    </div>
    <div class="form-check form-check-inline" >
      <input class="form-check-input" v-model="reviewData.rank" type="radio" name="exampleRadios" id="exampleRadios3" value="3" checked>
      <label class="form-check-label" for="exampleRadios3" ><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></label>
    </div>
    <div class="form-check form-check-inline" >
      <input class="form-check-input" v-model="reviewData.rank" type="radio" name="exampleRadios" id="exampleRadios4" value="4" checked>
      <label class="form-check-label" for="exampleRadios4" ><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></label>
    </div>
    <div class="form-check form-check-inline" >
      <input class="form-check-input" v-model="reviewData.rank" type="radio" name="exampleRadios" id="exampleRadios5" value="5" checked>
      <label class="form-check-label" for="exampleRadios5" ><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></label>
    </div>
    <hr />
    <div class="review" v-for="review in reviews.slice().reverse()" :key="`review_${review.id}`">
      <!-- 여기 모달!!! -->
      <reviewEdit @edit-review="getReviews" :review="review" :movie_id="movie_id" />

      <div class="courses-container">
        <div class="course">
          <div class="course-preview">
            <h2>{{review.user.username}}</h2>
            <div v-if="review.rank === 1" class="card-text"><i class="fas fa-star text-warning"></i></div>
            <div v-else-if="review.rank === 2" class="card-text"><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></div>
            <div v-else-if="review.rank === 3" class="card-text"><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></div>
            <div v-else-if="review.rank === 4" class="card-text"><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></div>
            <div v-else-if="review.rank === 5" class="card-text"><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i><i class="fas fa-star text-warning"></i></div>
          </div>
          <div class="course-info">
            <h5 class="text-break">{{review.content}}</h5>
            <div class="d-flex justify-content-end">
              <button @click="checkUser(review.id)" data-toggle="modal" :data-target="`#review_${review.id}`" class="fucn align-items-end"><i class="fas fa-edit"></i></button>
              <button @click="DeleteReview(review.id)" class="fucn"><i class="far fa-trash-alt"></i></button>
            </div>
            <div class="d-flex justify-content-start">
                <p class="my-auto datetime">작성 : {{review.created_at}} | </p>
                <p class="my-auto datetime">수정 : {{review.updated_at}}</p>                        
            </div>                            
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios"
import ReviewEdit from "./ReviewEdit"

const SERVER_URL = "http://localhost:8000"

export default {
  name: "ReviewList",
  components: {
    ReviewEdit
  },
  props: {
    movie_id: Number
  },
  data() {
    return {
      reviews: [],
      config: {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      },
      reviewData: {
        content: null,
        rank: 1
      }
    }
  },
  computed: {},
  methods: {
      getReviews() {             
          console.log('요청왔고11')
          console.log(this.movie_id)
          // axios.get(SERVER_URL+'/movies/'+this.movie_id+'/review/', this.config)
          axios.get(SERVER_URL+'/movies/'+this.movie_id+'/review/')
          .then(res => {      
              this.reviews = res.data    
              this.$emit('get-rank')
          })
          .catch(err => {console.error(err.response)})
      },
      createReview() {
          event.preventDefault()           
          axios.post(SERVER_URL+'/movies/'+this.movie_id+'/review/', this.reviewData, this.config)
              .then(() => {                                   
                  this.getReviews()             
                  this.reviewData.content = null
                  alert('댓글 작성됨')
              })
              .catch(err => console.log(err.response.data))
      },

      DeleteReview(review_id) {   
          this.checkUser(review_id)
          axios.delete(SERVER_URL+'/movies/'+this.movie_id+'/review/'+review_id+'/', this.config)
          .then(() => {                                  
              this.getReviews()                      
              alert('댓글 삭제됨')          
          })
          .catch(err => console.error(err.response))
      },      
      checkUser(review_id) { 
        axios.get(SERVER_URL+'/movies/'+this.movie_id+'/review/'+review_id+'/check/', this.config)
        .then(() => {                                                               
        })
        .catch(err => {
          console.error(err.response);console.log(err)
          alert('작성한 본인만 가능합니다.')             
          })
      },  
    },
    mounted() {        
        this.getReviews()
    },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Muli&display=swap');

* {
	box-sizing: border-box;
}

.course {
	background-color: #fff;
	border-radius: 10px;
	box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
	display: flex;
	max-width: 100%;
	margin: 20px;
	overflow: hidden;
	width: 100%;
}

.course h6 {
	opacity: 0.6;
	margin: 0;
	letter-spacing: 1px;
	text-transform: uppercase;
}

.course h2 {
	letter-spacing: 1px;
	margin: 10px 0;
}
.card-text {
  font-size: 15px;
}

.course-preview {
	background-color: #2A265F;
	color: #fff;
	padding: 30px;
  padding-top: 5px;
  padding-bottom: 10px;
	max-width: 250px;
}

.course-preview a {
	color: #fff;
	display: inline-block;
	font-size: 12px;
	opacity: 0.6;
	margin-top: 30px;
	text-decoration: none;
}

.course-info {
	padding: 30px;
  padding-top: 15px;
  padding-bottom: 15px;
	position: relative;
	width: 100%;
}

.progress-container {
	position: absolute;
	top: 30px;
	right: 30px;
	text-align: right;
	width: 150px;
}

.progress {
	background-color: #ddd;
	border-radius: 3px;
	height: 5px;
	width: 100%;
}

.progress::after {
	border-radius: 3px;
	background-color: #2A265F;
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	height: 5px;
	width: 66%;
}

.progress-text {
	font-size: 10px;
	opacity: 0.6;
	letter-spacing: 1px;
}

.fucn {
	background-color: #2A265F;
	border: 0;
	border-radius: 50px;
	box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
	color: #fff;
	font-size: 16px;
	padding: 12px 25px;
	letter-spacing: 1px;
}
</style>