<template>
  <div>
    <div class="container">
      <h2 class="text-center mt-4">아무거나 보지 않는다</h2>
      <button type="button" class="btn btn-secondary float-right">
        <router-link style="color: white" :to="{ name: 'CreateArticle'}">글쓰기</router-link>
      </button>
    </div>
    <div class="container mt-5">
      <div class="table-responsive">
        <table class="table table-striped table-dark text-white table-hover">
            <thead class="text-center">
                <tr>
                    <th>작성자</th>
                    <th colspan="2">제목</th>
                    <!-- <th class="text-truncate">내용</th>                     -->
                    <th>작성일</th>
                    <th>수정일</th>
                    <!-- <th>상세</th> -->
                    <!-- <th>Type</th> -->
                </tr>
            </thead>
            <tbody class="text-center">
                <tr v-for="article in articles" :key="`article_${article.id}`">
                    <td>
                        <div class="font-weight-bold">{{ article.user.username }}</div>
                    </td>
                    <td colspan="2">
                        <h6><router-link :to="{ name: 'ArticleDetail', params: {article_id : article.id } }">
                            {{ article.title }}
                          </router-link> 
                        </h6>
                    </td>
                    <!-- <td>
                      {{article.content}}
                    </td> -->
                    <td class="datetime">{{article.created_at}}<br></td>
                    <td class="datetime">{{article.updated_at}}</td>
                    <!-- <td><i class="fa fa-external-link external-link"></i></td> -->
                    <!-- <td>Business</td> -->                                        
                </tr>               
            </tbody>
        </table>
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios"

const SERVER_URL = "http://localhost:8000"

export default {
  name: 'CommunityList',
  components: {
    
  },
  data() {
    return {
      articles: [],
      // isLoggedIn: false,
    }
  },
  methods: {
    fetchArticles() {
        const config = {
            headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
        }
        axios.get(SERVER_URL + "/articles/", config)
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
    checkLoggedIn() {
      if (!this.$cookies.isKey('auth-token')) {
        alert('로그인 후 사용가능합니다')
        this.$router.push({ name: 'Login' })
      } 
    },
  },
  created() {
    this.checkLoggedIn(),
    this.fetchArticles()
  },
  mounted() {
    // this.isLoggedIn = this.$cookies.isKey('auth-token')
  },
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Assistant');
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

div > h2 {
  font-family: 'Jua', sans-serif;
}

body {
  background: #eee;
  font-family: Assistant, sans-serif
}

a {
  color: #eee;
  text-decoration: none;
}

a:hover 
{
  color:#00A0C6; 
  text-decoration:none; 
  cursor:pointer;  
}

.datetime {
  font-size: 0.8rem;
  font-style: italic;
}

</style>