<template>
  <form class="m-t" role="form">
    <p>Perfectly designed and precisely prepared admin theme with over 50 pages with extra new web app views.
      <!--Continually expanded and constantly improved Inspinia Admin Them (IN+)-->
    </p>
    <p>Login in. To see it in action.</p>
    <div class="form-group">
      <input type="email" v-model="useremail" class="form-control" placeholder="Email" required>
    </div>
    <div class="form-group">
      <input type="password" v-model="userpass" class="form-control" placeholder="Password" required>
    </div>
    <p>{{errorMsg}}</p>
    <button v-on:click="login($event)" class="btn btn-primary block full-width m-b">Login</button>
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
            login(e) {
                e.preventDefault();
                var formData = {
                    'email': this.useremail,
                    'password': this.userpass
                }
                this.$store.dispatch('login', formData)
                //  this.$router.push('/')
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
