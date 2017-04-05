<template>
  <div class="animated fadeInDown">

    <div class="row">
            <div class="col-md-6 text-white hidden-xs">
                <h2 class="font-bold">Welcome to ClassGotcha <span class="label label-primary">Beta</span></h2>
            <p>ClassGotcha is a tool that makes the life of college students easier.</p>
            <p> It can help you organize, communicate and share learning materials at one place.</p>
            <p> All kinds of learning activities are automatically pushed to your calendar, including but not limited to homework, quiz, exams and projects. </p>
            <p>If you want to ask questions and talk to classmates, this facebook like timeline and instant chatroom will make everyone in your class easy to find.</p>
            <p> You can also share notes to earn money, and be accessible to all the notes shared by your classmates.
            </p>

            </div>
            <div class="col-md-6 col-xs-12">
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


         <router-link :to="{name:'register'}" class="btn btn-sm btn-white btn-block">Create an account</router-link>

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
