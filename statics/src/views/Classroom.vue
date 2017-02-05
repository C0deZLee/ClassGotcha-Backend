<template>
  <div class="page animated fadeInRight">
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
  <div class="wrapper wrapper-content">
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
      <div class="col-md-2" v-for="professor in professors">
        <table class="table small m-b-xs">
          <tbody>
            <tr>
              <td>
                <strong>{{professor.full_name}}</strong> <a class="m-l" :href="professor_page_url(professor.id)">Detail</a>
              </td>
            </tr>
            <tr>
              <td>
                email: <strong>{{professor.email}}</strong>
              </td>
            </tr>
            <tr>
              <td>
                office: <strong>{{professor.office}}</strong>
              </td>
            </tr>
            <tr>
              <td>
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
          <h3>Class Files</h3>
          <ul class="folder-list m-b-md" style="padding: 0">
             <li>
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}}"> 
                  <i class="fa fa-align-justify"></i> All Files
                </router-link>
              </li>
                <li v-show="showFolder('Note')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Note'}}"> 
                  <i class="fa fa-certificate"></i> Notes <span class="label label-warning pull-right">16</span> 
                </router-link>
              </li>
              <li v-show="showFolder('Lecture')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Lecture'}}"> 
                  <i class="fa fa-inbox"></i> Lectures
                </router-link>
              </li>
              <li v-show="showFolder('Lab')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Lab'}}"> 
                  <i class="fa fa-flask"></i> Labs
                </router-link>
              </li>
              <li v-show="showFolder('Homework')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Homework'}}"> 
                  <i class="fa fa-file-text-o"></i> Homeworks <span class="label label-danger pull-right">2</span>
                </router-link>
              </li>
              <li v-show="showFolder('Exam')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Exam'}}"> 
                  <i class="fa fa-bolt"></i> Exams
                </router-link>
              </li>
          </ul>
        </div>
      </div>
      <div class="ibox">
        <div class="ibox-content">
          <h3>Your Classmates</h3>
          <div class="user-friends">
            <a v-for="student in current_classroom.students"><img alt="image" class="img-circle" :src="student.avatar.avatar2x"></a>
          </div>
          <p>
            <a :href="students_page_url">More..</a>
          </p>
        </div>
      </div>
      <div class="ibox">
        <div class="ibox-content">
          <h3>Create a Group</h3>
          <h5>Location</h5>
          <input type="text" placeholder="IST 231" class="form-control">
          <h5>Time</h5>
          <input type="text" placeholder="4/12 5:00pm-6:00pm" class="form-control">
          <h5>People invited</h5>
          <div class="user-friends">
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a4.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a5.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a6.jpg"></a>
            <a href=""><img alt="add people" class="img-circle" src="modules/classrooms/img/a6.jpg"></a>
          </div>
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
            <li v-if="moment.creator.id === user_id && moment.solved === false"><a @click="addSolve(moment.id)">Mark as solved</a></li>
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
            <small class="text-muted">{{momentTime(moment.created)}}</small>
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
              <small class="text-muted">{{momentTime(comment.created)}}</small>
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
          <a @click="showAddTask" >
            <div class="vertical-timeline-icon navy-bg" v-show="user_in_classroom">
              <i class="fa fa-star" ></i>
            </div>
          </a>
          <div class="vertical-timeline-content" v-show="user_in_classroom">
            <div class="row">
              <div class="col-md-10">
                <h2>Add a new task to classroom?</h2>
              </div>
              <div class="col-md-2">
                <a @click="showAddTask"> <span class="label label-primary pull-right"><i :class="add_task_button_class"></span></a>
              </div>
            </div>
            <div v-show="add_task">
              <div class="row">
                <div class="col-md-12">
                  <select class="form-control m-b" v-model="task_category">
                    <option value="1">Assignment</option>
                    <option value="2">Quiz</option>
                    <option value="3">Exam</option>
                  </select>
                </div>
              </div>
               
              <div class="row">
                <div class="col-md-12">
                  <input class="form-control m-b" v-model="task_title" placeholder="eg. Homework 1"></input>
                </div>

                <div class="col-md-12" v-show="task_category==2 || task_category==3">
                  <input type="radio" v-model="task_subcategory" value="1" id="in-class" name="a">
                    <label for="in-class"></label> Take home 
                    <i class="m-l" ></i>
                      <input type="radio"  v-model="task_subcategory" value="2" id="take-home" name="a">
                    <label for="take-home"></label> In class
                    <i class="m-l" ></i>
                      <input type="radio" v-model="task_subcategory" value="3" id="other-time" name="a">
                    <label for="other-time" v-show="task_category==3"></label> <span v-show="task_category==3"> Other Time</span>
                </div>

                <div class="col-md-12 m-t">
                  <div class="form-group">
                    <div class="input-group date">
                      <input type="text" v-show="task_subcategory==1" placeholder="Due time?" v-model="task_due_datetime" id="task-due-datetime" class="form-control" />
                      <input type="text" v-show="task_subcategory==2" placeholder="Which day?" v-model="task_due_date" id="task-due-date" class="form-control" />
                      <input type="text" v-show="task_subcategory==3" placeholder="Start at?" v-model="task_start" id="task-start" class="form-control" />
                      <input type="text" v-show="task_subcategory==3" placeholder="End at?" v-model="task_end" id="task-end" class="form-control" />
                      <span class="input-group-addon">
                      <span class="fa fa-calendar"></span>
                    </div>
                  </div>
                </div>
                <div class="col-md-12" v-show="task_subcategory==3">
                  <input class="form-control m-b" v-model="task_location" placeholder="Location?"></input>                  
                </div>  
                  <div class="col-md-12">
                  <textarea class="form-control m-b" v-model="task_dscr" placeholder="Describe it in more detail? (optional)"></textarea>
                  <p v-show="task_errMsg">{{task_errMsg}}</p>
                  
                </div>
              </div>
              <a @click="postTask($event)" :disabled="invaildTask()" class="btn btn-sm btn-primary">Add</a>
            </div>
          </div>
          <div v-for="task in tasks" class="vertical-timeline-block">
            <!-- 1) Homework 2) Quiz 3) Exam-->            
            <div class="vertical-timeline-icon" :class="{ 'blue-bg': task.category === 1, 'yellow-bg':task.category === 2, 'red-bg': task.category === 3}">
              <i class="fa" :class="{ 'fa-file-text': task.category === 1, 'fa-pencil':task.category === 2, ' fa-warning': task.category === 3}"></i>
            </div>
            <div class="vertical-timeline-content">
              <h2>{{task.task_name}}</h2>
              <p>{{task.description}}
              </p>
              <a href="#" class="btn btn-sm btn-primary"> More info</a>
              <span class="vertical-date">
              {{task.formatted_end_time}} <br>
              <small>{{taskTime(task.formatted_end_date, 3)}}</small>
              </span>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>
<script>
    import { customTime, toUtcString, formatDate } from 'utils/timeFilter'
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
                // moment
                content: '',
                question: false,
                dropzone: false,
                // comment
                comment_content: '',
                comment_id: -1,
                // task
                add_task: false,
                add_task_button_class: 'fa fa-plus',

                task_category: 1, // 1: homework, 2: quiz, 3: exam
                task_subcategory: 1, // 1: take home, 2: in class, 3: other time
                task_location: '',
                task_title: '',
                task_dscr: '',

                task_due_datetime: null,
                task_due_date: null,
                task_start: null,
                task_end: null,

                task_errMsg: ''

            }
        },
        methods: {
            // Data Loading
            getClassroomData() {
                this.$store.dispatch('getClassroom', this.$route.params.classroom_id)
            },
            // Classroom Add/Drop
            addClassroom() {
                this.$store.dispatch('addClassroom', this.$route.params.classroom_id)
            },
            remClassroom() {
                this.$store.dispatch('remClassroom', this.$route.params.classroom_id)
            },
            // Moments 
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
            // Tasks
            postTask() {
                if (!this.invaildTask()) {
                    /* global Date:true */
                    const data = {
                        formData: {
                            task_name: this.task_title,
                            description: this.task_dscr,
                            due_datetime: this.task_due_datetime ? toUtcString(new Date(this.task_due_datetime)) : null,
                            due_date: this.task_due_date ? toUtcString(new Date(this.task_due_date)) : null,
                            start: this.task_start ? toUtcString(new Date(this.task_start)) : null,
                            end: this.task_end ? toUtcString(new Date(this.task_end)) : null,
                            location: this.task_location,
                            category: parseInt(this.task_category),
                            classroom: parseInt(this.$route.params.classroom_id)
                        },
                        pk: this.$route.params.classroom_id
                    }
                    this.$store.dispatch('postClassroomTask', data)
                    this.clearTask()
                } else {
                    this.task_errMsg = 'Did you miss something?'
                    this.task_due_datetime = null
                    this.task_due_date = null
                    this.task_start = null
                    this.task_end = null
                }
            },
            // Utils
            invaildTask() {
                if (this.task_title === '')
                    return true
                else if (this.task_subcategory === '1' && !this.task_due_datetime)
                    return true
                else if (this.task_subcategory === '2' && !this.task_due_date)
                    return true
                else if (this.task_subcategory === '3' && !(this.task_start && this.task_end))
                    return true
                else
                    return false
            },
            showFolder(name) {
                for (let i in this.current_classroom.folders) {
                    if (this.current_classroom.folders[i].name === name)
                        return true
                }
                return false
            },
            momentTime(time) {
                return customTime(time)
            },
            taskTime(time, type) {
                return formatDate(time, type)
            },
            clearTask() {
                this.task_due_datetime = null
                this.task_due_date = null
                this.task_start = null
                this.task_end = null

                this.task_subcategory = 1
                this.task_errMsg = ''
                this.task_title = ''
                this.task_dscr = ''
                this.task_location = ''
            },
            professor_page_url(pk) {
                return '/#/professor/id/' + pk
            },
            user_page_url(pk) {
                return '/#/profile/id/' + pk
            },
            // taskBg(category) {
            //     if (category === 1) // Homework
            //         return 'blue-bg'
            //     else if (category === 2) // Quiz
            //         return 'yellow-bg'
            //     else if (category === 3) // Exam
            //         return 'red-bg'
            // },
            // taskIcon(category) {
            //     if (category === 1) // Homework
            //         return 'fa fa-file-text'
            //     else if (category === 2) // Quiz
            //         return 'fa fa-pencil'
            //     else if (category === 3) // Exam
            //         return 'fa fa-list-alt'
            // },
            // UI Switches
            showAddTask() {
                this.add_task = !this.add_task
                if (this.add_task) this.add_task_button_class = 'fa fa-minus'
                else this.add_task_button_class = 'fa fa-plus'
            },
            showCommentBox(moment) {
                this.comment_content = ''
                this.comment_id = moment.id
            },
            showDropzone() {
                this.dropzone = !this.dropzone
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
            tasks() {
                return this.$store.getters.classroomTasks
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
        created() {
            // Once the vue instance is created, load data
            this.getClassroomData()
        },
        mounted() {
            /* global $:true */
            // enable all datetime pickers
            $('#task-due-datetime').datetimepicker().on(
                'dp.change', () => { this.task_due_datetime = $('#task-due-datetime').val() }
            )
            $('#task-due-date').datetimepicker({ format: 'L' }).on(
                'dp.change', () => { this.task_due_date = $('#task-due-date').val() }
            )
            $('#task-start').datetimepicker().on(
                'dp.change', () => { this.task_start = $('#task-start').val() }
            )
            $('#task-end').datetimepicker().on(
                'dp.change', () => { this.task_end = $('#task-end').val() }
            )
        },
        watch: {
            // execute getClassroomData if route changes
            '$route': 'getClassroomData',
            // clear date info if user choosed different task type
            // 'task_category': 'clearTask',
            // 'task_subcategory': 'clearTask'
        },
    }

</script>
