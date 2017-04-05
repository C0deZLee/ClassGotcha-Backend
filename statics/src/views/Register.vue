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
               <div class="row">
                  <h1 class="text-center"> Register</h1>
                  <div class="form-group col-md-6">
                     <span class="help-block m-b-none">First Name</span>
                     <input v-model="first_name" type="text" class="form-control" name="first_name" placeholder="First Name" required>
                     <p class="text-danger font-bold">{{firstMsg}}</p>
                  </div>
                  <div class="form-group col-md-6">
                     <span class="help-block m-b-none">Last Name</span>
                     <input v-model="last_name" type="text" class="form-control" name="last_name" placeholder="Last Name" required>
                     <p class="text-danger font-bold">{{lastMsg}}</p>
                  </div>
               </div>
               <div class="form-group">
                  <span class="help-block m-b-none">Username</span>
                  <input v-model="username" type="text" class="form-control" name="username" placeholder="Username" required>
                  <p class="text-danger font-bold">{{usernameMsg}}</p>
               </div>
               <div class="form-group">
                  <span class="help-block m-b-none">Email</span>
                  <input v-model="email" type="email" class="form-control" name="email" placeholder="Email" required>
                  <p class="text-danger font-bold">{{emailMsg}}</p>
               </div>
               <div class="form-group">
                  <span class="help-block m-b-none">Password</span>
                  <input v-model="password" type="password" class="form-control" name="password" placeholder="Password" required>
                  <p class="text-danger font-bold">{{passwordMsg}}</p>
               </div>
               <div class="form-group">
                  <input type="checkbox" v-model="checked" id="check" name="check" required>
                  <label for="check"></label> 
                  <i class="m-r"></i>I want to contribute to<a data-toggle="modal" data-target="#terms"> COIL research project</a>
                  <p class="text-danger font-bold">{{policyMsg}}</p>
               </div>
               <button @click="getToken($event)" class="btn btn-primary block full-width m-b">Register</button>
               <p class="text-muted text-center"><small>Already have an account?</small></p>
               <router-link class="btn btn-sm btn-white btn-block" :to="{ name: 'login'}">Login</router-link>
            </div>
         </div>
      </div>
      <div class="modal inmodal " id="terms" tabindex="-1" role="dialog" aria-hidden="true">
         <div class="modal-dialog">
            <div class="modal-content animated fadeInDown">
               <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                  <h4 class="modal-title">Consent for Exempt Research</h4>
                  <h5>The Pennsylvania State University</h5>
               </div>
               <div class="modal-body">
                  <p>Title of Project:  ClassGotcha: Goal-oriented Personalized Online Learning Management System Supported by Educational Data Mining		</p>
                  <p> Principal Investigator: Qiyuan Li</p>
                  <p>Telephone Number: 814-441-5027</p>
                  <p>Advisor: Dr. Kyle Peck</p>
                  <p>Advisor Telephone Number: 814-863-7380</p>
                  <p>You are being invited to volunteer to participate in a research study. This summary explains information about this research.	</p>
                  <p>We are asking you to be in this research because we need your help to test the effectiveness of a personalized learning management system, ClassGotcha, as a user of it. This research is being done to find out whether the personalized learning profile is effective in improving the student retention. </p>
                  <p>In this research, you just need to use this learning management system to facilitate your study as you usually did with any other learning management tools. No extra action is required.
                     Your data created by using the tool will be assigned to a random ID and analyzed to investigate whether this tool is useful for improve student retention. There would be a pre-survey and a post-survey before and after you using the tool, you are free to skip any questions you prefer not to answer. Your homework records, and exam records will be used after removing any personal identifiers. No one other than the research team will access to your data, and they will analyze the data without personal identifiers most of the times. After the research finished, the data will be kept on server as long as you use the tool. It will be deleted as you required or five years after the research finishes if you don’t use the tool in the future.
                  </p>
                  <p>If you have questions or concerns, you should contact Qiyuan Li at 814-441-5027.   If you have questions regarding your rights as a research subject or concerns regarding your privacy, you may contact the Office for Research Protections at 814-865-1775. </p>
                  <p>Your participation is voluntary and you may decide to stop at any time.  You do not have to answer any questions that you do not want to answer. </p>
                  <p>INFORMED CONSENT TO TAKE PART IN RESEARCH </p>
                  <p>Electronic Signature of Person Giving Informed Consent </p>
                  <p>Before making the decision about being in this research you should have:</p>
                  Discussed this research study with an investigator<br>
                  Read the information in this form, and<br>
                  Had the opportunity to ask any questions you may have. <br>
                  <p>Typing your name below means that you have received this information, have asked the questions you currently have about the research and those questions have been answered. Please print a copy of this consent form to keep for future reference.</p>
                  <p><strong>Electronic Signature of Subject</strong></p>
                  <p>By typing your name below, you indicate that you voluntarily choose to be in this research and agree to allow your information to be used and shared as described above. </p>
                  <div class="form-group"><label>Signature</label>
                     <input type="text" class="form-control" :placeholder="first_name+' '+last_name"> 
                  </div>
                  <div class="form-group"><label>Time</label>
                     <input type="text" class="form-control" :value="timeNow()" disabled> 
                  </div>

                  
               </div>
               <div class="modal-footer">
                  <button type="button" class="btn btn-primary" @click="checked=true" data-dismiss="modal">Agree</button>
                  <button type="button" class="btn btn-white" data-dismiss="modal">Close</button>
               </div>
            </div>
         </div>
      </div>
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
                firstMsg: '',
                policyMsg: '',

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
                    first_name: this.first_name,
                    last_name: this.last_name,
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
                else
                    this.$store.dispatch('register', formData)
                    .catch((error) => {
                        for (let e in error.data) {
                            if (e === 'email') {
                                this.emailMsg = error.data[e][0]
                            } else if (e === 'username') {
                                this.usernameMsg = error.data[e][0]
                            }
                        }
                    })
            },

            timeNow() {
                /* global moment:rue */
                return moment().format('MMM D YYYY, h:mm:ss a')
            }
        },
    }

</script>
