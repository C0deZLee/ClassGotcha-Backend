<template>
  <div class="animated fadeInDown">

    <div class="row">
            <div class="col-md-6 text-white hidden-xs">
                <h2 class="font-bold">Welcome to ClassGotcha <span class="label label-primary">Beta</span></h2>

                <p>
                    Perfectly designed and precisely prepared admin theme with over 50 pages with extra new web app views.
                </p>

                <p>
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.
                </p>

                <p>
                    When an unknown printer took a galley of type and scrambled it to make a type specimen book.
                </p>

                <p>
                    <small>It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.</small>
                </p>

            </div>
            <div class="col-md-6">
                <div class="ibox-content">
      <h1 class="text-center"> Login</h1>
                        <div class="form-group">
                            <span class="help-block m-b-none">Email</span>
      <input type="email" v-model="email" class="form-control" placeholder="Email" required>

                        </div>
                        <div class="form-group">
                            <span class="help-block m-b-none">Password</span>
                            
      <input type="password" @keyup.enter="login($event)" v-model="password" class="form-control" placeholder="Password" required>

                        </div>
                         <p class="text-danger font-bold">{{errorMsg}}</p>
    
    <button @click="login($event)" class="btn btn-primary block full-width m-b">Login</button>

                        <a href="#">
                            <small>Forgot password?</small>
                        </a>

                           <p class="text-muted text-center"><small>Do not have an account?</small></p>


    <a class="btn btn-sm btn-white btn-block" href="/#/register">Create an account</a>

                </div>
            </div>
        </div>
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
