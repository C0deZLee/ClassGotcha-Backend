<template>
   <div class="page">
   <!--<div class="row wrapper border-bottom white-bg page-heading">
      <div class="col-lg-10">
        <h2>{{current_classroom.class_short}} 
         
        </h2>
        <ol class="breadcrumb">
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a>Classrooms</a>
          </li>
          <li class="active">
            <strong>{{current_classroom.class_short}}</strong>
          </li>
        </ol>
      </div>
      </div>-->
   <div class="wrapper wrapper-content animated fadeInRight">
      <div class="row m-b-lg m-t-lg">
         <div class="col-md-6">
            <div class="profile-image">
               <img src="img/CS.png" class="img-circle circle-border m-b-md" alt="profile">
            </div>
            <div class="profile-info">
               <div>
                  
                     <h2 class="no-margins">
                        {{current_classroom.class_short}}  
                        <button @click="addClassroom()" class="btn btn-primary" v-show="!user_in_classroom">
                        <i class="fa fa-plus"></i> 
                         Add To My Classroom
                        </button>

                       <button @click="remClassroom()"  class="btn" v-show="user_in_classroom">
                        <i class="fa fa-check"></i> 
                         Enrolled
                        </button>
                        
                     </h2>
                     <h4>
                        Section {{current_classroom.class_section}}
                     </h4>
                     <small>
                     {{current_classroom.description}}
                     </small>
                  
               </div>
            </div>
         </div>
         <div class="col-md-2">
            <table class="table small m-b-xs">
               <thead>
                  Summary
               </thead>
               <tbody>
                  <tr>
                     <td>
                        <strong>{{current_classroom.class_credit}}</strong> Credits
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <strong>1</strong> Midterm
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <strong>154</strong> Classmates
                     </td>
                  </tr>
               </tbody>
            </table>
         </div>
      </div>
      <p>
         Semester Progcess
      </p>
      <div class="progress progress-mini">
         <div style="width: 25%" class="progress-bar progress-bar-primary">
         </div>
         <div style="width: 1%" class="progress-bar progress-bar-danger">
         </div>
         <div style="width: 25%" class="progress-bar progress-bar-primary">
         </div>
         <div style="width: 1%" class="progress-bar progress-bar-warning">
         </div>
         <div style="width: 25%" class="progress-bar progress-bar-primary">
         </div>
      </div>
   </div>
   <div class="row">
      <div class="col-lg-3">
         <div class="ibox">
            <div class="ibox-content">
               <div class="pull-right dropdown">
                  <button data-toggle="dropdown" class="dropdown-toggle btn-white" aria-haspopup="true" aria-expanded="false">
                  <i class="fa fa-angle-down"></i>
                  </button>
                  <ul class="dropdown-menu m-t-xs">
                     <li><a href="#">Contact Professor</a></li>
                     <li><a href="#">Make an Appointment</a></li>
                  </ul>
               </div>
               <h3>Professor Info</h3>
               <!--<div class="profile-image">
                    <img src="http://www.cse.psu.edu/~buu1/bhuvan-mots.jpg" class="img-circle circle-border m-b-md" alt="profile">
                </div>-->
                <div v-for="professor in professors">
               <p> Name: <a :href="professor_page_url(professor.id)">{{professor.full_name}}</a><br> Office: 220 IST<br> Email: buu1@psu.edu<br>
                  <br>
                  <span class="font-bold">Rating: <i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i> </span>
               </p>
               <ul class="tag-list m-b" style="padding: 0">
                  <li><a href=""><i class="fa fa-tag"></i> Awesome</a></li>
                  <li><a href=""><i class="fa fa-tag"></i> Great Lecturer</a></li>
               </ul>
               <br>
               <br>
                 <button class="btn btn-white m-b">
                     yo
                  </button>
               </div>
            </div>
         </div>
         <div class="ibox">
            <div class="ibox-content">
               <h3>Class Notes</h3>
               <ul class="folder-list m-b-md" style="padding: 0">
                  <li class="text-navy"><a href="/#/classroom/id/demo/notes/"> <i class="fa fa-inbox"></i> Notes <span class="label label-warning pull-right">16</span> </a></li>
                  <li><a href="mailbox.html"> <i class="fa fa-envelope-o"></i> Lectures</a></li>
                  <li><a href="mailbox.html"> <i class="fa fa-certificate"></i> Labs</a></li>
                  <li><a href="mailbox.html"> <i class="fa fa-file-text-o"></i> Homeworks <span class="label label-danger pull-right">2</span></a></li>
                  <li><a href="mailbox.html"> <i class="fa fa-trash-o"></i> Exams</a></li>
               </ul>
               <a>More...</a>
            </div>
         </div>
 
         <div class="ibox">
            <div class="ibox-content">
               <h3>Your Classmates</h3>
               <div class="user-friends">
                  <a v-for="student in current_classroom.students" href=""><img alt="image" class="img-circle" :src="student.avatar.avatar2x"></a>
               </div>
               <p>
                  <a :href="students_page_url">More..</a>
                  <!--<router-link to="/classroom/id/:classroom_id/students">More..</router-link>-->
               </p>
            </div>
         </div>
                 <div class="ibox">
            <div class="ibox-content">
               <h3>Create a Group</h3>
               <h5>People invited</h5>
               <div class="user-friends">
                  <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a4.jpg"></a>
                  <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a5.jpg"></a>
                  <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a6.jpg"></a>
                  <a href=""><img alt="add people" class="img-circle" src="modules/classrooms/img/a6.jpg"></a>
               </div>
               <h5>Location</h5>
               <input type="text" placeholder="IST 231" class="form-control">
               <h5>Time</h5>
               <input type="text" placeholder="4/12 5:00pm-6:00pm" class="form-control">
               <br>    
               <a href="#" class="btn btn-sm btn-primary"> Invite!</a>
            </div>
         </div>
      </div>
      <div class="col-lg-5">
          <div class="ibox float-e-margins" v-show="user_in_classroom" id="new-moment">
        <div class="ibox-title">
                        <div class="input-group">
                      <textarea class="form-control" v-model.lazy="content" placeholder="Wanna say something?"></textarea>
                      <span class="input-group-addon btn btn-primary" @click="showDropzone"> <i class="fa fa-camera"></i> </span>
                        </div>
                         <upload v-if="dropzone" ref="dropzone"></upload>
                                </div>
                                <div class="ibox-content" style="padding:10px 10px 15px">
                                    <div class="m-b-10">
                                     <input type="checkbox" v-model="question" id="check" name="check" required>
                                    <label for="check"></label> 
                                    Post as a question
                                    <button @click="postMoment"  data-dismiss="modal" class=" btn btn-sm btn-primary pull-right">Post</button>
                                    </div>
                        </div>         
                      </div>
         <div class="social-feed-box" v-for="moment in moments">
            <div class="pull-right social-action dropdown">
               <button data-toggle="dropdown" class="dropdown-toggle btn-white"> <i class="fa fa-angle-down"></i></button>
               <ul class="dropdown-menu m-t-xs">
                  <li><a @click="addReport(moment.id)">Report</a></li>
                  <li v-if="moment.creator.id === user_id"><a @click="delMoment(moment.id)">Delete</a></li>
               </ul>
            </div>
            <div class="social-avatar">
               <a href="" class="pull-left">
               <img alt="image" class="img-circle" :src="moment.creator.avatar.avatar2x">
               </a>
               <div class="media-body">
                  <a :href="user_page_url(moment.creator.id)"> {{moment.creator.full_name}} </a>
                  <span v-show="moment.solved" class="label label-primary">Solved</span>
                  <span v-show="moment.solved!==null&&!moment.solved" class="label label-warning">Question</span>
                  <small class="text-muted">{{formatTime(moment.created)}}</small>
               </div>
            </div>
            <div class="social-body">
               <p>
                  {{moment.content}}
               </p>
               <img v-if="moment.images" :src="moment.images" class="img-responsive">
               <div class="btn-group">
                  <button @click="addLike(moment)" class="btn btn-white btn-xs"><i class="fa fa-thumbs-up"></i> {{moment.likes}} Like this! </button>
                  <button @click="showCommentBox(moment)" class="btn btn-white btn-xs"><i class="fa fa-comments"></i> Comment</button>
               </div>
            </div>
            <div class="social-footer" v-show="moment.comments.length > 0 || moment.id === comment_id">
               <div class="social-comment" v-for="comment in moment.comments">
                  <a href="" class="pull-left">
                  <img class="img-circle" alt="image" :src="comment.creator.avatar.avatar1x">
                  </a>
                  <div class="media-body">
                     <a href="">{{comment.creator.full_name}}</a> 
                     <small class="text-muted">{{formatTime(comment.created)}}</small>
                     <br/>
                     {{comment.content}}
                  </div>
               </div>
               <div class="social-comment" v-show="moment.id === comment_id">
                  <a href="" class="pull-left">
                  <img alt="image" :src="user_avatar">
                  </a>
                  <div class="media-body">
                     <textarea class="form-control" v-model="comment_content" @keyup.enter="postComment($event)"  placeholder="Write comment..."></textarea>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <div class="col-lg-4 m-b-lg">
         <div id="vertical-timeline" class="vertical-container light-timeline no-margins">
            <div class="vertical-timeline-block">
               <div class="vertical-timeline-icon navy-bg" v-show="user_in_classroom">
                  <i class="fa fa-star"></i>
               </div>
               <div class="vertical-timeline-content" v-show="user_in_classroom">
                <div class="row">
                    <div class="col-md-10">
                  <h2>Add a new task to classroom?</h2>
                  </div>

                  <div class="col-md-2">
                    <a @click="showAddTask"> <span class="label label-primary pull-right"><i :class="add_task_button_class"></span></a>

                    </div>
                </div>
                  <div v-if="add_task">
                     <div class="row">
                        <div class="col-md-5">
                           <input class="form-control m-b" v-model="task_title" placeholder="ex. Homework 1"></input>
                        </div>
                        <div class="col-md-7">
                           <!--<span class="vertical-date">
                              <select class="form-control m-b">
                                 <option >-Type-</option>
                                 <option value="Homework">Homework</option>
                                 <option value="Lab">Homework</option>
                                 <option value="Quiz">Quiz</option>
                                 <option value="Exam">Exam</option>
                              </select>
                           </span>-->
                           <div class="form-group">
                              <div class="input-group date">
                                 <input type="text" placeholder="Time" v-model="task_time" id="datetimepicker" class="form-control" />
                                 <span class="input-group-addon">
                                 <span class="glyphicon glyphicon-calendar"></span>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="row">
                        <div class="col-sm-8">
                           
                        </div>
                        <div class="col-md-12">
                        <textarea class="form-control m-b" v-model="task_dscr" placeholder="Homwwork due tomorrow?"></textarea>
                        </div>
                     </div>
                        <a @click="postTask()" class="btn btn-sm btn-primary"> Add</a>
                     
                  </div>
               </div>
               <div v-for="task in current_classroom.tasks" class="vertical-timeline-block">
                  <div class="vertical-timeline-icon navy-bg">
                     <i class="fa fa-briefcase"></i>
                  </div>
                  <div class="vertical-timeline-content">
                     <h2>{{task.task_name}}</h2>
                     <p>{{task.description}}
                     </p>
                     <a href="#" class="btn btn-sm btn-primary"> More info</a>
                     <span class="vertical-date">
                     {{task.formatted_due_datetime}} <br>
                     <small>Apr 1</small>
                     </span>
                  </div>
               </div>
               <div class="vertical-timeline-block">
                  <div class="vertical-timeline-icon yellow-bg">
                     <i class="fa fa-file-text"></i>
                  </div>
                  <div class="vertical-timeline-content">
                     <h2>Homework</h2>
                     <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
                        standard dummy text ever since.
                     </p>
                     <a href="#" class="btn btn-sm btn-success"> Download document </a>
                     <span class="vertical-date">
                     Tomorrow <br>
                     <small>Apr 11</small>
                     </span>
                  </div>
               </div>
               <div class="vertical-timeline-block">
                  <div class="vertical-timeline-icon red-bg">
                     <i class="fa fa-pencil"></i>
                  </div>
                  <div class="vertical-timeline-content">
                     <h2>In-class Quiz</h2>
                     <p>Go to shop and find some products. Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                        Lorem Ipsum has been the industry's. 
                     </p>
                     <a href="#" class="btn btn-sm btn-danger">More Info</a>
                     <span class="vertical-date"> Tomorrow <br><small>Apr 11</small></span>
                  </div>
               </div>
               <div class="vertical-timeline-block">
                  <div class="vertical-timeline-icon yellow-bg">
                     <i class="fa fa-file-text"></i>
                  </div>
                  <div class="vertical-timeline-content">
                     <h2>Homework</h2>
                     <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto, optio, dolorum provident rerum aut hic quasi
                        placeat iure tempora laudantium ipsa ad debitis unde? Iste voluptatibus minus veritatis qui ut.
                     </p>
                     <a href="#" class="btn btn-sm btn-success"> Download document </a>
                     <span class="vertical-date"> In 2 days <br><small>Apr 12</small></span>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>

<script>
    import { customTime } from 'utils/timeFilter'
    // import Dropzone from 'vue2-dropzone'
    import Upload from 'components/UploadImg'

    // VUe doesn't provide a method that can run after component load
    export default {
        name: 'Classroom',
        components: {
            'upload': Upload,
        },
        data: function() {
            return {
                content: '',
                question: false,
                // comment
                comment_content: '',
                comment_id: -1,
                // task
                add_task: false,
                add_task_button_class: 'fa fa-plus',
                task_title: '',
                task_dscr: '',
                task_time: '',
                dropzone: false
            }
        },
        methods: {
            // UI 
            showAddTask() {
                this.add_task = !this.add_task
                if (this.add_task)
                    this.add_task_button_class = 'fa fa-minus'
                else
                    this.add_task_button_class = 'fa fa-plus'

                /* global $:true */
                setTimeout(() => {
                    $('#datetimepicker').datetimepicker()
                }, 100)
            },
            showCommentBox(moment) {
                this.comment_content = ''
                this.comment_id = moment.id
            },
            showDropzone() {
                this.dropzone = !this.dropzone
            },
            formatTime(time) {
                return customTime(time)
            },

            addClassroom() {
                this.$store.dispatch('addClassroom', this.$route.params.classroom_id)
            },
            remClassroom() {
                this.$store.dispatch('remClassroom', this.$route.params.classroom_id)
            },
            addLike(moment) {
                this.$store.dispatch('addMomentLike', moment.id)
                moment.likes += 1
            },
            addReport(pk) {
                this.$store.dispatch('reportMoment', pk)
            },
            addSolve(pk) {
                this.$store.dispatch('solveMoment', pk)
            },
            getClassroomData() {
                this.$store.dispatch('getClassroom', this.$route.params.classroom_id)
                this.$store.dispatch('getClassroomMoments', this.$route.params.classroom_id)
            },
            postMoment() {
                const formData = {
                    content: this.content,
                    classroom_id: this.$route.params.classroom_id,
                    question: this.question
                }
                this.$store.dispatch('postMoment', formData).then(() => {
                    this.content = ''
                    this.dropzone = false
                })

            },
            delMoment(pk) {
                this.$store.dispatch('delMoment', pk)
            },
            postComment(e) {
                e.preventDefault()
                const data = {
                    formData: { content: this.comment_content },
                    id: this.comment_id,
                }
                this.$store.dispatch('postMomentComment', data)
                this.comment_content = ''
                this.comment_id = -1
            },
            postTask() {
                /* global Date:true */
                const task_time = Date.parse(this.task_time)
                const data = {
                    formData: { description: this.task_dscr, due: task_time, task_name: this.task_title, type: 1 },
                    pk: this.$route.params.classroom_id
                }
                this.$store.dispatch('postClassroomTask', data)
            },
            professor_page_url(pk) {
                return '/#/professor/id/' + pk
            },
            user_page_url(pk) {
                return '/#/profile/id/' + pk
            }


        },
        computed: {
            current_classroom() {
                return this.$store.getters.currentClassroom
            },
            user_in_classroom() {
                return this.$store.getters.userInClassroom
            },
            moments() {
                return this.$store.getters.classroomMoments
            },
            user_avatar() {
                return this.$store.getters.userAvatar.avatar2x
            },
            professors() {
                return this.$store.getters.classroomProfessors
            },
            students_page_url() {
                return '/#/classroom/id/' + this.$route.params.classroom_id + '/students'
            },
            user_id() {
                return this.$store.getters.userID
            }

        },
        created: function() {
            // after component is created, load data
            this.getClassroomData()
        },
        watch: {
            // execute getClassroomData if route changes
            '$route': 'getClassroomData'
        },
    }

</script>
