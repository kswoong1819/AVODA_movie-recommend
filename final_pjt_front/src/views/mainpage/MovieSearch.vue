<template>
  <div>
    <input class="form-control" v-model="keyword" @keypress.enter="searchMovie" type="text" placeholder="Search" aria-label="Search">
  </div>
</template>

<script>
export default {
  name: 'MovieSearch',
  data: function () {
    return {
        keyword: '',
    }
  },
  methods: {
    searchMovie: function () {
      if (!this.keyword.trim()){
        alert('영화 제목을 입력해주세요!')
      } else {
        this.$emit('search-movies', this.keyword.trim())
        this.keyword=''
      }
    }
  },
}
</script>

<style>

</style>