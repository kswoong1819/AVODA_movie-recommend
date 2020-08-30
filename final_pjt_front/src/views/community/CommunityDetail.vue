<template>
  <div>
    <div class="container">

      <button type="button" class="btn btn-secondary btn-sm float-right">
        <router-link style="color: white" :to="{ name: 'CreateArticle' }">새 글쓰기</router-link>
      </button>
      <br>
      <h3 class="text-center font-size-big">{{article.title}}</h3>
      <hr>
      
      <div class="font-size-md">
          {{article.content}}
      </div>  
      <br>
      <div class="datetime float-right">
          작성 : {{article.created_at}} |
          수정 : {{article.updated_at}}
      </div>
      <hr>
      <div>
        <button @click="articleDelete" class="btn btn-secondary btn-sm float-right">글 삭제</button>
        <button class="btn btn-secondary btn-sm float-right">
            <router-link style="color: white" :to="{ name: 'EditArticle', params: {article_id : article_id } }">글 수정</router-link>
        </button>
      </div>
    </div>
     <br>
    <CommentList :article_id="article_id" />

  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/communityDetail/CommentList.vue'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "CommunityDetail",
  data() {
    return {
      article: {},
      article_id : this.$route.params.article_id,
      config : {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      },
    };
  },
  components: {
      CommentList,
  },
  methods: {
    articleDetail () {                   
        axios.get(SERVER_URL+'/articles/'+this.article_id+'/', this.config)
        .then(res => {                                       
            this.article = res.data    
        })
        .catch(err => {console.error(err.response)})
    },

    articleDelete () {    
        this.checkUser()
        axios.delete(SERVER_URL+'/articles/'+this.article_id+'/', this.config)
        .then(() => {                                  
            this.$router.push({ name: 'Community' })        
        })
        .catch(err => console.error(err.response))
    },
    checkUser() { 
      axios.get(SERVER_URL+'/articles/'+this.article_id+'/check/', this.config)
      .then(() => {                                                               
      })
      .catch(err => {
        console.error(err.response);console.log(err)
        alert('작성한 본인만 가능합니다.')        
        })
    },

  },
  created() {      
    this.articleDetail()    
  },
}
</script>

<style>
.font-size-big {
  font-size: 3rem;
}

.font-size-md {
  font-size: 1.5rem;
}
</style>