<template>
    <form class="m-t" role="form">
      <p>Create account to see it in action.</p>
              <div class="form-group">
                  <input v-model="username" type="text" class="form-control" placeholder="Username" required>
                  <p>{{usernameMsg}}</p>
              </div>
              <div class="form-group">
                  <input v-model="email" type="email" class="form-control" placeholder="Email" required>
                  <p>{{emailMsg}}</p>
              </div>
              <div class="form-group">
                  <input v-model="password" type="password" class="form-control" placeholder="Password" required>
                  <p>{{passwordMsg}}</p>
              </div>
              <div class="form-group">
                    <div class="checkbox i-checks"><label> <input type="checkbox" required><i></i> Agree the terms and policy </label></div>
              </div>
              <button v-on:click="getToken($event)" class="btn btn-primary block full-width m-b">Register</button>

              <p class="text-muted text-center"><small>Already have an account?</small></p>
              <a class="btn btn-sm btn-white btn-block" href="/#/login">Login</a>
        </form>
</template>

<script>
  export default {
    name: 'register',
    methods: {
      getToken: function(e) {
        e.preventDefault();
        var formData = {
          'username': this.username,
          'email': this.email,
          'password': this.password
        }
        this.$http.post('http://localhost:8000/account/register/', formData).then((response) => {
          //success
          this.$root.authToken = response.data.token
          this.$router.push('/')
        }, (response) => {
          //failed
          this.emailMsg = response.data.email[0]
          this.usernameMsg = response.data.username[0]
          this.passwordMsg = response.data.password[0]

        });
      },
    },
    data: function() {
      return {
        username: '',
        email: '',
        password: '',
        usernameMsg: '',
        emailMsg: '',
        passwordMsg: ''
      }
    }
  }
  // UI
</script>