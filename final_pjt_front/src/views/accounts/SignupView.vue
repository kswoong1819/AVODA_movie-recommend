<template>
  <div>
    <h1>회원가입</h1>
    <form @keypress.enter="signup">
      <div class="form-group">
        <label for="username">아이디</label>
        <input v-model="signupData.username" type="text" class="form-control" id="username">
        <small id="username" class="form-text text-muted">아이디를 작성해주세요.</small>
      </div>
      <div class="form-group">
        <label for="password1">Password</label>
        <input v-model="signupData.password1" type="password" class="form-control" id="password1">
        <small id="password1" class="form-text text-muted">비밀번호를 작성해주세요.</small>
      </div>
      <div class="form-group">
        <label for="password2">Password</label>
        <input v-model="signupData.password2" type="password" class="form-control" id="password2">
        <small id="password2" class="form-text text-muted">비밀번호를 다시 한번 작성해주세요.</small>
      </div>
      <button @click="signup" class="btn btn-primary">확인</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignupView",
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null
      }
    };
  },
  methods: {
    signup(event) {
      event.preventDefault()
      this.$emit("submit-signup-data", this.signupData)
    }
  }
};
</script>

<style>
</style>