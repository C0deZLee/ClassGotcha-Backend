<template>
    <form class="animated fadeInDown" role="form">
      <p>Create account to see it in action.</p>
            <div class="row">
                <div class="form-group col-md-6">
                  <input v-model="first_name" type="text" class="form-control" placeholder="First Name" required>
                  <p class="text-danger font-bold">{{firstMsg}}</p>
              </div>
                            <div class="form-group col-md-6">
                  <input v-model="last_name" type="text" class="form-control" placeholder="Last Name" required>
                      <p class="text-danger font-bold">{{lastMsg}}</p>
              </div>
            </div>
              <div class="form-group">
                  <input v-model="username" type="text" class="form-control" placeholder="Username" required>
                      <p class="text-danger font-bold">{{usernameMsg}}</p>
              </div>
              <div class="form-group">
                  <input v-model="email" type="email" class="form-control" placeholder="Email" required>
                      <p class="text-danger font-bold">{{emailMsg}}</p>
              </div>
              <div class="form-group">
                  <input v-model="password" type="password" class="form-control" placeholder="Password" required>
                      <p class="text-danger font-bold">{{passwordMsg}}</p>
              </div>
            <div class="form-group">
                <div class="checkbox i-checks"><label> <input type="checkbox"><i></i> Agree the terms and policy </label></div>
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
            getToken() {
                const formData = {
                    username: this.username.replace(/%20/g, ''),
                    email: this.email.replace(/%20/g, ''),
                    password: this.password,
                    first_name: this.first_name.replace(/%20/g, ''),
                    last_name: this.last_name.replace(/%20/g, ''),
                }
                if (!formData.first_name)
                    this.firstMsg = 'This field is needed'
                else if (!formData.last_name)
                    this.lastMsg = 'This field is needed'
                else if (!formData.username)
                    this.usernameMsg = 'This field is needed'
                else if (!formData.email)
                    this.emailMsg = 'This field is needed'
                else if (!formData.password)
                    this.passwordMsg = 'This field is needed'

                else
                    this.$store.dispatch('register', formData).then(() => {
                        console.log('success')
                    }, () => {
                        console.log('failed')
                    })
            },
            // error(){
            //     this.emailMsg = response.data.email[0]
            //         this.usernameMsg = response.data.username[0]
            //         this.passwordMsg = response.data.password[0]
            // }
        },
        data() {
            return {
                username: '',
                email: '',
                password: '',
                last_name: '',
                first_name: '',
                usernameMsg: '',
                emailMsg: '',
                passwordMsg: '',
                lastMsg: '',
                firstMsg: ''
            }
        },
        updated() {
            /* global $:true */
            $(document).ready(function() {
                console.log('ready')
                $('.i-checks').iCheck({
                    checkboxClass: 'icheckbox_square-green',
                    radioClass: 'iradio_square-green',
                })
            })

        }
    }
    // UI

</script>
