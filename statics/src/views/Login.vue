<template>
  <div class="animated fadeInDown">
    <p>Login in. To see it in action.</p>
    <div class="form-group">
      <input type="email" v-model="email" class="form-control" placeholder="Email" required>
    </div>
    <div class="form-group">
      <input type="password" @keyup.enter="login($event)" v-model="password" class="form-control" placeholder="Password" required>
    
    </div>
                            <p class="text-danger font-bold">{{errorMsg}}</p>
    
    <button @click="login($event)" class="btn btn-primary block full-width m-b">Login</button>
    <a href="#"><small>Forgot password?</small></a>
    
    <p class="text-muted text-center"><small>Do not have an account?</small></p>
    <a class="btn btn-sm btn-white btn-block" href="/#/register">Create an account</a>
  </div>
</template>

<script>
    export default {
        name: 'login',
        data() {
            return {
                email: '',
                password: '',
                errorMsg: '',
            }
        },
        methods: {
            login() {
                var formData = {
                    'email': this.email,
                    'password': this.password
                }
                this.$store.dispatch('login', formData)
                    .catch(() => {
                        this.errorMsg = 'Unable to login with provided email and password.'
                    })
            },
        }
    }

</script>
