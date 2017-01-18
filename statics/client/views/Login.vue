<template>
  <form class="m-t" role="form">
    <p>Perfectly designed and precisely prepared admin theme with over 50 pages with extra new web app views.
        <!--Continually expanded and constantly improved Inspinia Admin Them (IN+)-->
    </p>
    <p>Login in. To see it in action.</p>
      <div class="form-group">
          <input type="email" v-model="useremail" class="form-control" placeholder="Email" required >
      </div>
      <div class="form-group">
          <input type="password" v-model="userpass" class="form-control" placeholder="Password" required >
      </div>
      <p>{{errorMsg}}</p>      
      <button v-on:click="getToken($event)" class="btn btn-primary block full-width m-b">Login</button>
      <button v-on:click="$root.checkAuth" class="btn btn-primary block full-width m-b">Auth Verify</button>
      <a href="#"><small>Forgot password?</small></a>
      <p class="text-muted text-center"><small>Do not have an account?</small></p>
      <a class="btn btn-sm btn-white btn-block" href="/#/register">Create an account</a>
  </form>
</template>

<script>
  export default {
    name: 'login',
    methods: {
      getToken: function(e) {
        e.preventDefault();
        var formData = {
          'email': this.useremail,
          'password': this.userpass
        }
        this.$http.post('http://localhost:8000/account/login/', formData).then((response) => {
          // success
          // store auth token 
          this.$root.authToken = response.data.token
          // write token to cookie, expires in 1 day
          this.$cookie.set('token', response.data.token, 1)
          // load user data
          this.$http.get('http://localhost:8000/account/me/', {
            headers: {
              'Authorization': 'JWT ' + this.$root.authToken
            }
          }).then(response => {
            this.$root.user = response.data
            console.log(this.$root.user)
          })
          // load user class
          this.$http.get('http://localhost:8000/account/classrooms/', {
            headers: {
              'Authorization': 'JWT ' + this.$root.authToken
            }
          }).then(response => {
            this.$root.classrooms = response.data
            console.log(this.$root.classrooms)
          })

          // redirect to home page
          this.$router.push('/')
        }, (response) => {
          // failed
          this.errorMsg = response.data.non_field_errors[0]
        });
      },
    },
    data: function() {
      return {
        useremail: '',
        userpass: '',
        errorMsg: '',
        token: ''
      }
    }

  }
</script>