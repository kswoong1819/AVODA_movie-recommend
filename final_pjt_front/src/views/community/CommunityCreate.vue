<template>
  <div>
    <h1>새 글쓰기</h1>
    <form>
        <div class="form-group">
            <label for="title">제목</label>
            <input v-model="articleData.title" type="text" class="form-control" placeholder="제목을 작성하세요." id="title">
        </div>
        <div class="form-group">
            <label for="content">내용</label>
            <textarea v-model="articleData.content" class="form-control" placeholder="내용을 작성하세요." id="content" rows="3"></textarea>
        </div>        
        <button @click="createArticle" type="submit" class="btn btn-primary">제출</button>    
    </form>  
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "CommunityCreate",
  data() {
    return {
      articleData: {
        title: null,
        content: null,
      }
    };
  },
  methods: {
    createArticle(event) {
      event.preventDefault()
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/articles/', this.articleData, config)
        .then(() => { 
          console.log('post 됨')           
          this.$router.push({ name: 'Community' })
        })
        .catch(err => console.log(err.response.data))
    },
    checkLoggedIn() {
      if (!this.$cookies.isKey('auth-token')) {
        alert('로그인 후 사용가능합니다')
        this.$router.push({ name: 'Login' })
      } 
    }
  },
  created() {
    this.checkLoggedIn()
  },
}
</script>

<style>

</style>
