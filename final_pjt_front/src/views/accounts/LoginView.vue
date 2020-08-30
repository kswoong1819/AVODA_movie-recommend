<template>
  <div>
    <h1>Login</h1>
    <form @keypress.enter="login">
      <div class="form-group">
        <label for="username">아이디</label>
        <input v-model="loginData.username" type="text" class="form-control" id="username">
        <small id="username" class="form-text text-muted">아이디를 작성해주세요.</small>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="loginData.password" type="password" class="form-control" id="password">
        <small id="password" class="form-text text-muted">비밀번호를 작성해주세요.</small>
      </div>
      <button @click="login" class="btn btn-primary">확인</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login(event) {
      event.preventDefault()
      this.$emit('submit-login-data', this.loginData)
    }
  },
}
</script>

<style>
</style>