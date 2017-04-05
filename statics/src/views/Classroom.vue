<template>
  <div class="page animated fadeInRight">
  <div>
    <div class="row m-b-lg m-t-lg">
      <div class="col-md-6">
       <div class="profile-image">
          <img src="~img/major/math.jpg" class="img-circle circle-border m-b-md" alt="profile">
        </div>
        <div class="profile-info">
          <div>
            <h2 class="no-margins">
              {{current_classroom.class_short}}  
              <button @click="addClassroom()" class="btn btn-primary" v-if="!user_in_classroom">
              <i class="fa fa-plus"></i> 
              Add To My Classroom
              </button>
              <a v-else class="text-primary" title="Quit this classroom" @click="remClassroom()"><i class="fa fa-sign-out"></i> </a>
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
               professor: 
             </td>
             <td>
               <strong>{{professor.full_name}} <router-link :to="{name:'professor', params:{professor_id:professor.id}}" class="m-l" >Detail</router-link></strong> 
             </td>
            </tr>
            <tr>
              <td>
                email:
              </td>
              <td>  <strong>{{professor.email}}</strong></td>
            </tr>
            <tr>
              <td>
                office:
              </td>
              <td>
                 <strong class="pull-right">{{professor.office}}</strong>
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
      Semester Process
    </p>
    <div class="progress  m-b">
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
                <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}}"> 
                  <i class="fa fa-align-justify"></i> All Files
                </router-link>
              </li>
                <li v-show="showFolder('Note')">
                <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Note'}}"> 
                  <i class="fa fa-certificate"></i> Notes <span class="label label-warning pull-right">16</span> 
                </router-link>
              </li>
              <li v-show="showFolder('Lecture')">
                <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Lecture'}}"> 
                  <i class="fa fa-inbox"></i> Lectures
                </router-link>
              </li>
              <li v-show="showFolder('Lab')">
                <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Lab'}}"> 
                  <i class="fa fa-flask"></i> Labs
                </router-link>
              </li>
              <li v-show="showFolder('Homework')">
                <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Homework'}}"> 
                  <i class="fa fa-file-text-o"></i> Homeworks <span class="label label-plain pull-right">2</span>
                </router-link>
              </li>
              <li v-show="showFolder('Exam')">
                <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Exam'}}"> 
                  <i class="fa fa-bolt"></i> Exams
                </router-link>
              </li>
          </ul>
        </div>
      </div>
      <div class="ibox">
        <div class="ibox-content">
          <h3>Your Classmates</h3>
          <div class="user-friends row">
            <a v-if="index!=18" class="col-sm-2" v-for="(student, index) in current_classroom.students">
              <img alt="image" class="img-circle" v-if="student.avatar" :src="student.avatar.avatar1x">
            <avatar v-else :size="42" :username="student.full_name"></avatar>
              </a>
          </div>
          <p>
            <router-link :to="{name:'classroomStudents', params:{classroom_id:$route.params.classroom_id}}" class="m-t">More..</router-link>
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
            <a href=""><img alt="image" class="img-circle" src="~img/avatar/a1.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="~img/avatar/a2.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="~img/avatar/a4.jpg"></a>
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
          <router-link :to="{name:'userDetail', params:{user_id:moment.creator.id}}" class="pull-left">
          <img v-if="moment.creator.avatar" :src="moment.creator.avatar.avatar1x" alt="image" class="img-circle" >
            <avatar v-else class="m-r" :size="40" :username="moment.creator.full_name"></avatar>
          </router-link>
          <div class="media-body">
            <router-link :to="{name:'userDetail', params:{user_id:moment.creator.id}}">
               {{moment.creator.full_name}}
            </router-link>
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
            <router-link :to="{name:'userDetail', params:{user_id:comment.creator.id}}" class="pull-left">
            <img v-if="comment.creator.avatar" class="img-circle" alt="image" :src="comment.creator.avatar.avatar1x">
              
            <avatar v-else :size="32" class="m-r" :username="comment.creator.full_name"></avatar>
            </router-link>
            <div class="media-body">
              <a href="">{{comment.creator.full_name}}</a> 
              <small class="text-muted">{{momentTime(comment.created)}}</small>
              <br/>
              {{comment.content}}
            </div>
          </div>
          <div class="social-comment" v-show="moment.id === comment_id">
            <a href="" class="pull-left">

            <img v-if="user_avatar" alt="image" :src="user_avatar.avatar1x">
            <avatar v-else :size="42" :username="user_full_name"></avatar>
            
            </a>
            <div class="media-body">
              <textarea class="form-control" v-model="comment_content" @keyup.enter="postComment($event)"  placeholder="Write comment..."></textarea>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-lg-4">
        <task></task>
  </div>
</template>
<script>
    import ClassroomTask from 'components/ClassroomTask'
    import Upload from 'components/UploadImg'
    import Avatar from 'vue-avatar'
    // VUe doesn't provide a method that can run after component load
    export default {
        name: 'Classroom',
        components: {
            'upload': Upload,
            'task': ClassroomTask,
            'avatar': Avatar.Avatar
        },
        data() {
            return {
                // moment
                content: '',
                question: false,
                dropzone: false,
                // comment
                comment_content: '',
                comment_id: -1,
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

            // Utils
            showFolder(name) {
                for (let i in this.current_classroom.folders) {
                    if (this.current_classroom.folders[i].name === name)
                        return true
                }
                return false
            },
            momentTime(time) {
                /* global moment:true */
                return moment(time).fromNow()
            },
            // UI Switches
            showAddTask() {
                /* global $:true */
                this.add_task = !this.add_task
                if (this.add_task) this.add_task_button_class = 'fa fa-minus'
                else this.add_task_button_class = 'fa fa-plus'
                $('#add-task').modal('show')

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
            user_avatar() {
                return this.$store.getters.userAvatar
            },
            user_full_name() {
                return this.$store.getters.userFullName
            },
            professors() {
                return this.$store.getters.classroomProfessors
            },
            user_id() {
                return this.$store.getters.userID
            }

        },
        created() {
            // Once the vue instance is created, load data
            this.getClassroomData()
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
