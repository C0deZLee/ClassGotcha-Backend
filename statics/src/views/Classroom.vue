<template>
  <div class="page">
    <div class="row wrapper border-bottom white-bg page-heading">
      <div class="col-lg-10">
        <h2>{{currentClassroom.class_short}} 
          <button title="Create new cluster" v-on:click="addClassroom()" class="btn btn-primary btn-xm">
          <i class="fa fa-plus"></i> 
          <span class="bold">Add To My Classroom</span>
          </button>
        </h2>
        <ol class="breadcrumb">
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a>Classrooms</a>
          </li>
          <li class="active">
            <strong>{{currentClassroom.class_short}}</strong>
          </li>
        </ol>
      </div>
    </div>
    <div class="wrapper wrapper-content animated fadeInRight">
      <div class="row m-b-lg m-t-lg">
        <div class="col-md-6">
          <div class="profile-image">
            <img src="modules/classrooms/img/CS.png" class="img-circle circle-border m-b-md" alt="profile">
          </div>
          <div class="profile-info">
            <div class="">
              <div>
                <h2 class="no-margins">
                  {{currentClassroom.class_short}}
                </h2>
                <h4>
                  Section {{currentClassroom.class_section}}
                </h4>
                <small>
                {{currentClassroom.description}}
                </small>
              </div>
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
                  <strong>{{currentClassroom.class_credit}}</strong> Credits
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
        Semester Process
      </p>
      <div class="progress">
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
            <p class="small">
              Name: <a href="">Professor Name</a><br>Office Hour: 11:00AM - 13:00AM Mon/Thu <br> Office: 220 IST<br> Email: buu1@psu.edu<br>
              <br>
              <span class="font-bold">Rating: <i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i> </span>
            <ul class="tag-list" style="padding: 0">
              <li><a href=""><i class="fa fa-tag"></i> Harsh</a></li>
              <li><a href=""><i class="fa fa-tag"></i> Huge Work Load</a></li>
            </ul>
            </p>
            <br>
          </div>
        </div>
        <div class="ibox">
          <div class="ibox-content">
            <h3>Class Notes</h3>
            <div class="btn-group">
              <a href="/#/classroom/id/demo/notes/" type="button" class="btn btn-success dropdown-toggle btn-lg">
              <span class="fa fa-file"></span>
              </a>
            </div>
            <div class="btn-group">
              <a type="button" class="btn btn-info dropdown-toggle btn-lg">
              <span class="fa fa-stack-exchange"></span>
              </a>
            </div>
            <div class="btn-group">
              <button type="button" class="btn btn-primary dropdown-toggle btn-lg " data-toggle="dropdown">
              <span class="fa fa-file-picture-o"></span>
              </button>
            </div>
            <div class="btn-group">
              <button type="button" class="btn btn-danger dropdown-toggle btn-lg" data-toggle="dropdown">
              <span class="fa fa-file-powerpoint-o"></span>
              </button>
            </div>
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
        <div class="ibox">
          <div class="ibox-content">
            <h3>Your Classmates</h3>
            <div class="user-friends">
              <a v-for="student in currentClassroom.students" href=""><img alt="image" class="img-circle" :src="student.avatar.avatar2x"></a>
            </div>
            <p>
              <a :href="studentsPagePath">More..</a>
              <!--<router-link to="/classroom/id/:classroom_id/students">More..</router-link>-->
            </p>
          </div>
        </div>
      </div>
      <div class="col-lg-5">
        <div class="social-feed-box">
          <div class="social-action">
            <a class="btn btn-info btn-rounded btn-block" data-toggle="modal" data-target="#post-moment"> Post New Moment</a>
            <div class="modal inmodal in" id="post-moment" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
              <div class="vertical-alignment-helper">
                <div class="modal-dialog vertical-align-center">
                  <div class="modal-dialog">
                    <div class="modal-content animated fadeIn">
                      <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                        <textarea class="form-control" v-model.lazy="content" placeholder="Wanna say something?"></textarea>
                      </div>
                      <div class="modal-footer">
                        <input type="radio"  name="question" v-model="question" class="" value="question">Post as a question
                        <button @click="postMoment"  data-dismiss="modal" class="pull-right btn btn-primary">Submit</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="social-feed-box" v-for="moment in moments">
          <div class="pull-right social-action dropdown">
            <button data-toggle="dropdown" class="dropdown-toggle btn-white"> <i class="fa fa-angle-down"></i></button>
            <ul class="dropdown-menu m-t-xs">
              <li><a href="#">Report</a></li>
            </ul>
          </div>
          <div class="social-avatar">
            <a href="" class="pull-left">
            <img alt="image" :src="moment.creator.avatar.avatar2x">
            </a>
            <div class="media-body">
              <a href="#"> {{moment.creator.full_name}} </a>
              <span v-show="moment.solved" class="label label-primary">Solved</span>
              <span v-show="moment.solved!==null&&!moment.solved" class="label label-warning">Problem</span>
              <small class="text-muted">{{formatTime(moment.created)}}</small>
            </div>
          </div>
          <div class="social-body">
            <p>
              {{moment.content}}
            </p>
            <img src="img/gallery/3.jpg" class="img-responsive">
            <div class="btn-group">
              <button @click="addLike(moment)" class="btn btn-white btn-xs"><i class="fa fa-thumbs-up"></i> {{moment.likes}} Like this! </button>
              <button @click="showCommentBox(moment)" class="btn btn-white btn-xs"><i class="fa fa-comments"></i> Comment</button>
            </div>
          </div>
          <div class="social-footer" v-show="moment.comments.length > 0 || moment.id === show_comment_id">
            <div class="social-comment" v-for="comment in moment.comments">
              <a href="" class="pull-left">
              <img alt="image" :src="comment.creator.avatar.avatar1x">
              </a>
              <div class="media-body">
                <a href="">{{comment.creator.full_name}}</a> 
                <small class="text-muted">{{formatTime(comment.created)}}</small>
                <br/>
                {{comment.content}}
              </div>
            </div>
            <div class="social-comment" v-show="moment.id === show_comment_id">
              <a href="" class="pull-left">
              <img alt="image" :src="userAvatar">
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
            <div class="vertical-timeline-icon navy-bg">
              <i class="fa fa-question"></i>
            </div>
            <div class="vertical-timeline-content">
              <h2>Add a new due?</h2>
              <textarea class="form-control" placeholder="Homwwork due tomorrow?"></textarea>
              <a href="#" class="btn btn-sm btn-primary"> More info</a>
              <span class="vertical-date">
                <select>
                  <option value ="volvo">Homework</option>
                  <option value ="saab">Quiz</option>
                  <option value="opel">Exam</option>
                  <option value="audi">Meeting</option>
                </select>
              </span>
            </div>
          </div>
          <div class="vertical-timeline-block">
            <div class="vertical-timeline-icon navy-bg">
              <i class="fa fa-briefcase"></i>
            </div>
            <div class="vertical-timeline-content">
              <h2>Group Meeting</h2>
              <p>We have set up a group meeting on 135 Pattee Library.
              </p>
              <a href="#" class="btn btn-sm btn-primary"> More info</a>
              <span class="vertical-date">
              Today <br>
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

<style>
    .vertical-alignment-helper {
        display: table;
        height: 100%;
        width: 100%;
        pointer-events: none;
    }
    
    .vertical-align-center {
        /* To center vertically */
        display: table-cell;
        vertical-align: middle;
        pointer-events: none;
    }
    
    .modal-content {
        /* Bootstrap sets the size of the modal in the modal-dialog class, we need to inherit it */
        width: inherit;
        height: inherit;
        /* To center horizontally */
        margin: 0 auto;
        pointer-events: all;
    }

</style>

<script>
    import { customTime } from 'utils/timeFilter'

    // VUe doesn't provide a method that can run after component load
    export default {
        name: 'Classroom',
        data: function() {
            return {
                content: '',
                question: '',
                comment_content: '',
                show_comment_id: -1
            }
        },
        methods: {
            formatTime(time) {
                return customTime(time)
            },
            addClassroom() {
                this.$store.dispatch('addClassroom', this.$route.params.classroom_id)
            },
            getClassroomData() {
                this.$store.dispatch('getClassroom', this.$route.params.classroom_id)
                this.$store.dispatch('getClassroomMoments', this.$route.params.classroom_id)
            },
            vaildUser() {
                this.$store.dispatch('validateClassroom', this.$route.params.classroom_id)
            },
            postMoment() {
                const formData = {
                    content: this.content,
                    classroom_id: this.$route.params.classroom_id,
                    question: this.question
                }
                this.$store.dispatch('postMoment', formData)
                this.content = ''
            },
            postComment(e) {
                e.preventDefault()
                const data = {
                    formData: { content: this.comment_content },
                    id: this.show_comment_id,
                }
                this.$store.dispatch('postMomentComment', data)
                this.comment_content = ''
                this.show_comment_id = -1
            },
            addLike(moment) {
                this.$store.dispatch('addMomentLike', moment.id)
                moment.likes += 1
            },
            addSolve(pk) {

            },
            showCommentBox(moment) {
                this.comment_content = ''
                this.show_comment_id = moment.id
            },
        },
        computed: {
            currentClassroom() {
                return this.$store.getters.currentClassroom
            },
            userInClassroom() {
                return this.$store.getters.userInClassroom
            },
            moments() {
                return this.$store.getters.classroomMoments
            },
            userAvatar() {
                return this.$store.getters.userAvatar.avatar2x
            },
            studentsPagePath() {
                return '/#/classroom/id/' + this.$route.params.classroom_id + '/students'
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
