<template>
  <form class="animated fadeInDown" role="form" >
    <p>Login in. To see it in action.</p>
    <div class="form-group">
      <input type="email" v-model="useremail" class="form-control" placeholder="Email" required>
    </div>
    <div class="form-group">
      <input type="password" v-model="userpass" class="form-control" placeholder="Password" required>
    </div>
    <p>{{errorMsg}}</p>
    <button v-on:click="login($event)" class="btn btn-primary block full-width m-b">Login</button>
    <a href="#"><small>Forgot password?</small></a>
    <p class="text-muted text-center"><small>Do not have an account?</small></p>
    <a class="btn btn-sm btn-white btn-block" href="/#/register">Create an account</a>
  </form>
</template>

<script>
    export default {
        name: 'login',
        methods: {
            login() {
                var formData = {
                    'email': this.useremail,
                    'password': this.userpass
                }
                this.$store.dispatch('login', formData)
            },
        },
        computed: {
            errorMsg: function() {
                return this.$store.errorMsg
            }
        },
        data: function() {
            return {
                useremail: '',
                userpass: '',
            }
        }

    }

</script>
