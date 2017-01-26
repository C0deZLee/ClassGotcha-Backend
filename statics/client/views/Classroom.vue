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
                                    CS 311
                                </h2>
                                <h4>abcd1234@psu.edu</h4>
                                <small>
                                    There are many variations of passages of Lorem Ipsum available, but the majority
                                    have suffered alteration in some form Ipsum available.
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <table class="table small m-b-xs">
                        <thead>
                            &nbsp&nbspSummary
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <strong>6-9</strong> Projects
                                </td>
                                <td>
                                    <strong>10</strong> Weekly Quizs
                                </td>

                            </tr>
                            <tr>
                                <td>
                                    <strong>1</strong> Midterm
                                </td>
                                <td>
                                    <strong>1</strong> Final
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>154</strong> Classmates
                                </td>
                                <td>
                                    <strong>2</strong> Papers
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
                <div class="profile-image">
                    <img src="http://www.cse.psu.edu/~buu1/bhuvan-mots.jpg" class="img-circle circle-border m-b-md" alt="profile">
                </div>
                <a>
                    <h3>Professor Name</h3>
                </a>

                <p class="small">
                    Office Hour: 11:00AM - 13:00AM Mon/Thu <br> Office: 220 IST<br> Email: buu1@psu.edu<br>
                    <br>
                    <span class="font-bold">Rating: <i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i><i class="fa fa-star text-navy"></i> </span>

                    <ul class="tag-list" style="padding: 0">
                    <li><a href=""><i class="fa fa-tag"></i> Harsh</a></li>
                    <li><a href=""><i class="fa fa-tag"></i> Huge Work Load</a></li>
                    </ul>
                    </p>
                    <p>
                        .
                    </p>
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
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a3.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a1.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a2.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a4.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a5.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a6.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a7.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a8.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a2.jpg"></a>
            <a href=""><img alt="image" class="img-circle" src="modules/classrooms/img/a1.jpg"></a>

        </div>
        <p>
            <a>More..</a></p>
    </div>
</div>

</div>

<div class="col-lg-5">
    <div class="social-feed-box">
        <div class="social-action">
            <textarea class="form-control" placeholder="Wanna say something?"></textarea>
            <input type="radio" name="gender" value="Problem">This is a problem
            <button ng-click="addPost()" class="pull-right btn btn-sm btn-primary">Submit</button>
            <br>
        </div>

    </div>
    <div class="social-feed-box" ng-if="showPost">

        <div class="pull-right social-action dropdown">
            <button data-toggle="dropdown" class="dropdown-toggle btn-white">
                                <i class="fa fa-angle-down"></i>
                            </button>
            <ul class="dropdown-menu m-t-xs">
                <li><a href="#">Report</a></li>
            </ul>
        </div>

        <div class="social-avatar">
            <a href="" class="pull-left">
                <img alt="image" src="modules/classrooms/img/a4.jpg">
            </a>
            <div class="media-body">
                <a href="#">
                                    Steve Lee
                                </a>
                <span class="label label-warning ">Question</span>
                <small class="text-muted">Today - 04.10.2016</small>
            </div>
        </div>
        <div class="social-body">
            <p>
                I'm stuck on Problem 4!
            </p>

            <div class="btn-group">
                <button class="btn btn-white btn-xs"><i class="fa fa-thumbs-up"></i> Like this!</button>
                <button class="btn btn-white btn-xs"><i class="fa fa-comments"></i> Comment</button>
            </div>
        </div>

    </div>

    <div class="social-feed-box">

        <div class="pull-right social-action dropdown">
            <button data-toggle="dropdown" class="dropdown-toggle btn-white">
                                <i class="fa fa-angle-down"></i>
                            </button>
            <ul class="dropdown-menu m-t-xs">
                <li><a href="#">Report</a></li>
            </ul>
        </div>
        <div class="social-avatar">
            <a href="" class="pull-left">
                <img alt="image" src="modules/classrooms/img/a1.jpg">
            </a>
            <div class="media-body">
                <a href="#">
                                    Andrew Williams
                                </a>
                <span class=" label label-primary">Solved</span>
                <small class="text-muted">Today 4:21 pm - 12.06.2014</small>
            </div>
        </div>
        <div class="social-body">
            <p>
                So when is our first meeting?
            </p>

            <div class="btn-group">
                <button class="btn btn-white btn-xs"><i class="fa fa-thumbs-up"></i> Like this!</button>
                <button class="btn btn-white btn-xs"><i class="fa fa-comments"></i> Comment</button>
            </div>
        </div>

    </div>

    <div class="social-feed-box">

        <div class="pull-right social-action dropdown">
            <button data-toggle="dropdown" class="dropdown-toggle btn-white">
                                <i class="fa fa-angle-down"></i>
                            </button>
            <ul class="dropdown-menu m-t-xs">
                <li><a href="#">Report</a></li>
            </ul>
        </div>
        <div class="social-avatar">
            <a href="" class="pull-left">
                <img alt="image" src="modules/classrooms/img/a6.jpg">
            </a>
            <div class="media-body">
                <a href="#">
                                    Judy Hopps
                                </a>
                <small class="text-muted">Today 4:21 pm - 12.06.2014</small>
            </div>
        </div>
        <div class="social-body">
            <p>
                Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.
                Packages and web page editors now use Lorem Ipsum as their default model text.
            </p>
            <img src="modules/classrooms/img/gallery/3.jpg" class="img-responsive">
            <div class="btn-group">
                <button class="btn btn-white btn-xs"><i class="fa fa-thumbs-up"></i> Like this!</button>
                <button class="btn btn-white btn-xs"><i class="fa fa-comments"></i> Comment</button>
            </div>
        </div>
        <div class="social-footer">
            <div class="social-comment">
                <a href="" class="pull-left">
                    <img alt="image" src="modules/classrooms/img/a1.jpg">
                </a>
                <div class="media-body">
                    <a href="#">
                                        Andrew Williams
                                    </a> Internet tend to repeat predefined chunks as necessary, making
                    this the first true generator on the Internet. It uses a dictionary of over 200 Latin words.
                    <br/>
                    <a href="#" class="small"><i class="fa fa-thumbs-up"></i> 26 Like this!</a> -
                    <small class="text-muted">12.06.2014</small>
                </div>
            </div>

            <div class="social-comment">
                <a href="" class="pull-left">
                    <img alt="image" src="modules/classrooms/img/a2.jpg">
                </a>
                <div class="media-body">
                    <a href="#">
                                        Andrew Williams
                                    </a> Making this the first true generator on the Internet. It uses
                    a dictionary of.
                    <br/>
                    <a href="#" class="small"><i class="fa fa-thumbs-up"></i> 11 Like this!</a> -
                    <small class="text-muted">10.07.2014</small>
                </div>
            </div>

            <div class="social-comment">
                <a href="" class="pull-left">
                    <img alt="image" src="modules/classrooms/img/a8.jpg">
                </a>
                <div class="media-body">
                    <a href="#">
                                        Judy Hopps
                                    </a> Making this the first true generator on the Internet. It uses
                    a dictionary of.
                    <br/>
                    <a href="#" class="small"><i class="fa fa-thumbs-up"></i> 11 Like this!</a> -
                    <small class="text-muted">10.07.2014</small>
                </div>
            </div>

            <div class="social-comment">
                <a href="" class="pull-left">
                    <img alt="image" src="modules/classrooms/img/a3.jpg">
                </a>
                <div class="media-body">
                    <textarea class="form-control" placeholder="Write comment..."></textarea>
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
                    standard dummy text ever since.</p>
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
                    Lorem Ipsum has been the industry's. </p>
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
                    placeat iure tempora laudantium ipsa ad debitis unde? Iste voluptatibus minus veritatis qui ut.</p>
                <a href="#" class="btn btn-sm btn-success"> Download document </a>
                <span class="vertical-date"> In 2 days <br><small>Apr 12</small></span>
            </div>
        </div>
    </div>
</div>
</div>
</div>
</div>
</template>

<script>
    // VUe doesn't provide a method that can run after component load
    export default {
        name: 'Classroom',
        methods: {
            addClassroom() {
                this.$store.dispatch('addClassroom', this.$route.params.classroom_id)
            },
            getClassroomData() {
                this.$store.dispatch('getClassrooms', this.$route.params.classroom_id)
            },
            vaildUser() {
                this.$store.dispatch('validateClassroom', this.$route.params.classroom_id)
            }
        },
        computed: {
            currentClassroom() {
                return this.$store.getters.currentClassroom
            },
            userInClassroom() {
                return this.$store.getters.userInClassroom
            }
        },
        data: function() {
            return {}
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
