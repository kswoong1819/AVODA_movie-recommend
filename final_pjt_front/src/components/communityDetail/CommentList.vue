<template>
  <div class="mt-4">
    
    <div class="input-group">
      <div class="input-group-prepend">
        <span class="input-group-text" id="basic-addon1"><i class="far fa-comment-dots"></i></span>
      </div>
      <input v-model="commentData.content" class="form-control" placeholder="댓글을 작성하세요." id="content" rows="3" />
      <button @click="createComment" type="submit" class="btn btn-dark">작성</button>
    </div>                  
    <hr>
    <div class="comment" v-for="comment in comments.slice().reverse()" :key="`comment_${comment.id}`"> 
        <!-- 여기 모달!!! -->
        <CommentEdit @edit-comment="getComments" :comment="comment" :article_id="article_id" />

        <div class="courses-container">
            <div class="course">
                <div class="course-preview">
                    <h2>{{comment.user.username}}</h2>            
                </div>
                <div class="course-info">
                    <h5 class="text-break">{{comment.content}}</h5>
                    <div class="d-flex justify-content-end">
                        <button @click="checkUser(comment.id)" data-toggle="modal" :data-target="`#comment_${comment.id}`" class="fucn align-items-end"><i class="fas fa-edit"></i></button>
                        <button @click="DeleteComment(comment.id)" class="fucn"><i class="far fa-trash-alt"></i></button>
                    </div>
                    <div class="d-flex justify-content-start">
                        <p class="my-auto datetime">작성 : {{comment.created_at}} | </p>
                        <p class="my-auto datetime">수정 : {{comment.updated_at}}</p>                        
                    </div>
                </div>
            </div>
        </div>                
        <hr>
    </div>            
  </div>
</template>

<script>
import axios from "axios"
import CommentEdit from "./CommentEdit"

const SERVER_URL = "http://localhost:8000"


export default {
    name: 'CommentList',
    components: {
        CommentEdit,
    },
    props: {
        article_id: Number,
    },
    data () {
        return {
            comments: [],
            config : {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            },
            commentData : {
                content: null,                
                // article: this.article_id,
            },            
        }
    },    
    computed: {
        
    },
    methods: {
        getComments() {             
        axios.get(SERVER_URL+'/articles/'+this.article_id+'/comment/', this.config)
        .then(res => {                                                   
            this.comments = res.data                
        })
        .catch(err => {console.error(err.response)})
        },
        createComment() {
            event.preventDefault()           
            axios.post(SERVER_URL+'/articles/'+this.article_id+'/comment/', this.commentData, this.config)
                .then(() => {                   
                // this.$router.push({ name: 'Community' })
                    this.getComments()             
                    this.commentData.content = null
                    alert('댓글 작성됨')
                })
                .catch(err => console.log(err.response.data))
        },

        DeleteComment(comment_id) {  
            this.checkUser(comment_id) 
            axios.delete(SERVER_URL+'/articles/'+this.article_id+'/comment/'+comment_id+'/', this.config)
            .then(() => {                                  
                this.getComments()                      
                alert('댓글 삭제됨')          
            })
            .catch(err => console.error(err.response))
        },        
        checkUser(comment_id) { 
            axios.get(SERVER_URL+'/articles/'+this.article_id+'/comment/'+comment_id+'/check/', this.config)
            .then(() => {                                                               
            })
            .catch(err => {
                console.error(err.response);console.log(err)
                alert('작성한 본인만 가능합니다.')                   
                })
            },

    },
    mounted() {        
        this.getComments()
    },

}
</script>

<style>
.fucn{
  background-color: #23272b;
}
.course-preview {
    background-color: #23272b;
}

</style>