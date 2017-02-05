<template>
    <div class="animated fadeInDown">
      <p>Create account to see it in action.</p>
            <div class="row">
                <div class="form-group col-md-6">
                  <input v-model="first_name" type="text" class="form-control" name="first_name" placeholder="First Name" required>
                  <p class="text-danger font-bold">{{firstMsg}}</p>
              </div>
                            <div class="form-group col-md-6">
                  <input v-model="last_name" type="text" class="form-control" name="last_name" placeholder="Last Name" required>
                      <p class="text-danger font-bold">{{lastMsg}}</p>
              </div>
            </div>
              <div class="form-group">
                  <input v-model="username" type="text" class="form-control" name="username" placeholder="Username" required>
                      <p class="text-danger font-bold">{{usernameMsg}}</p>
              </div>
              <div class="form-group">
                  <input v-model="email" type="email" class="form-control" name="email" placeholder="Email" required>
                      <p class="text-danger font-bold">{{emailMsg}}</p>
              </div>
              <div class="form-group">
                  <input v-model="password" type="password" class="form-control" name="password" placeholder="Password" required>
                      <p class="text-danger font-bold">{{passwordMsg}}</p>
              </div>
            <div class="form-group">
                 <input type="checkbox" v-model="checked" id="check" name="check" required>
                 <label for="check"></label> 
                 <i class="m-r"></i>Agree the terms and policy 
             </div> 
              <button @click="getToken($event)" class="btn btn-primary block full-width m-b">Register</button>

              <p class="text-muted text-center"><small>Already have an account?</small></p>
              <router-link class="btn btn-sm btn-white btn-block" :to="{ name: 'login'}">Login</router-link>
        </div>
</template>

<script>
    export default {
        name: 'register',
        data() {
            return {
                checked: false,
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
        methods: {
            getToken(e) {
                e.preventDefault()
                this.usernameMsg = ''
                this.emailMsg = ''
                this.passwordMsg = ''
                this.lastMsg = ''
                this.firstMsg = ''
                const formData = {
                    username: this.username.replace(/%20/g, ''),
                    email: this.email.replace(/%20/g, ''),
                    password: this.password,
                    first_name: this.first_name.replace(/%20/g, ''),
                    last_name: this.last_name.replace(/%20/g, ''),
                }

                if (!formData.first_name)
                    this.firstMsg = 'This field is required'
                else if (!formData.last_name)
                    this.lastMsg = 'This field is required'
                else if (!formData.username)
                    this.usernameMsg = 'This field is required'
                else if (!formData.email)
                    this.emailMsg = 'This field is required'
                else if (!formData.password)
                    this.passwordMsg = 'This field is required'
                else if (this.checked)
                    this.$store.dispatch('register', formData).catch((error) => {
                        for (let e in error.data) {
                            console.log(e, error.data[e][0])
                            if (e === 'email') {
                                this.emailMsg = error.data[e][0]
                            } else if (e === 'username') {
                                this.usernameMsg = error.data[e][0]
                            }
                        }
                    })
            }
            // error(){
            //     this.emailMsg = response.data.email[0]
            //         this.usernameMsg = response.data.username[0]
            //         this.passwordMsg = response.data.password[0]
            // }
        },
    }
    // UI

</script>
