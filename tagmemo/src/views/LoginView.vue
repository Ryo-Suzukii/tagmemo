<template>
  <div class="login-view">
    <h2>{{ $t('login') }}</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">{{  $t('login') }}</button>
    </form>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    handleLogin() {
      // Handle login logic here
      console.log('Email:', this.email);
      console.log('Password:', this.password);
    }
  }
};
</script>

<style scoped>
h2 {
  text-align: center;
}
.login-view {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
