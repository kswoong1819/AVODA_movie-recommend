<template>
  <div class="mb-5">
      <input type="text" v-model="keyword" @keypress.enter="searchMovie">
      <button @click="searchMovie">검색</button>
  </div>
</template>

<script>
export default {
    name: 'MovieSearch',
    data() {
        return {
            keyword: '',
        }
    },
    methods : {
        searchMovie() {
            if (!this.keyword) {
                alert('검색어를 입력하세요')
            } else {            
                this.$emit('search-movie', this.keyword)
            }
        },
    },


}
</script>
<style>
div > input {
    width: 50%;
}
</style>