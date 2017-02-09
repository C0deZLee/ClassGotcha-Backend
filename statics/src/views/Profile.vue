<template>
   <div>
      <div class="row wrapper border-bottom white-bg page-heading">
         <div class="col-sm-4">
            <h2>Profile</h2>
            <ol class="breadcrumb">
               <li>
                  <router-link to="{name:'home'}">Home</router-link>
               </li>
               <li class="active">
                  <strong>Profile</strong>
               </li>
            </ol>
         </div>
      </div>
      <div class="wrapper wrapper-content animated fadeInRight">
         <div class="row">
            <div class="col-lg-3">
               <h2>My Name Card</h2>
               <div class="contact-box">
                  <a>
                     <div class="col-sm-4">
                        <div class="text-center">
                           <img v-if="user.avatar" alt="image" class="img-circle m-t-xs img-responsive" :src="user.avatar.avatar2x">
                           <avatar v-else class="img-circle m-t-xs img-responsive" :size="100" :username="user.full_name"></avatar>
                           <div class="m-t-xs font-bold">@{{user.username}}</div>
                        </div>
                     </div>
                     <div class="col-sm-8">
                        <h3><strong>{{user.full_name}}</strong> 
                           <span class="label label-warning">Level {{user.level}}</span>
                        </h3>
                        <address>
                           <strong>Major:</strong> {{majorByID(user.major)}}<br>
                           <strong>Class:</strong> {{user.school_year}}<br>
                           <strong>About Me</strong><br>
                           {{user.about_me}}
                        </address>
                     </div>
                     <div class="clearfix"></div>
                  </a>
               </div>
            </div>
            <div class="col-lg-9">
               <dl class="m-t-xl dl-horizontal">
                  <dt>Level:</dt>
                  <dd>
                     <span class="label label-warning">Level {{user.level}}</span>
                  </dd>
               </dl>
               <dl class="dl-horizontal">
                  <dt>Exp:</dt>
                  <dd>
                     <div class="progress progress-striped active m-b-sm">
                        <div style="width: 60%;" class="progress-bar"></div>
                     </div>
                     <small><strong>600</strong>/1000, You are 400 exp from next level!</small>
                  </dd>
               </dl>
               <dl class="dl-horizontal">
                  <dt>Badges:</dt>
                  <dd>
                    under development
                  </dd>
               </dl>
            </div>
         </div>
         <div class="row">
            <div class="col-lg-12">
               <div class="ibox">
                  <div class="ibox-content">
                     <div class="row m-t-sm">
                        <div class="col-lg-12">
                           <div class="panel blank-panel">
                              <div class="panel-heading">
                                 <div class="panel-options">
                                    <ul class="nav nav-tabs">
                                       <li class="active"><a href="#tab-1" data-toggle="tab">Rencent activity</a></li>
                                       <li class=""><a href="#tab-2" data-toggle="tab">Personal Information</a></li>
                                       <li class=""><a href="#tab-3" data-toggle="tab">Badges Process</a></li>
                                       <li class=""><a href="#tab-3" data-toggle="tab">Self</a></li>
                                    </ul>
                                 </div>
                              </div>
                              <div class="panel-body">
                                 <div class="tab-content">
                                    <div class="tab-pane active" id="tab-1">
                                       <div class="feed-activity-list">
                                          <div class="feed-element">
                                             <a href="#" class="pull-left">
                                             <img alt="image" class="img-circle" src="img/a2.jpg">
                                             </a>
                                             <div class="media-body ">
                                                <small class="pull-right">2h ago</small>
                                                <strong>Mark Johnson</strong> posted message on <strong>Monica Smith</strong>                                                                site. <br>
                                                <small class="text-muted">Today 2:10 pm - 12.06.2014</small>
                                                <div class="well">
                                                   Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy
                                                   text ever since the 1500s. Over the years, sometimes
                                                   by accident, sometimes on purpose (injected humour and
                                                   the like).
                                                </div>
                                             </div>
                                          </div>
                                          <div class="feed-element">
                                             <a href="#" class="pull-left">
                                             <img alt="image" class="img-circle" src="img/a3.jpg">
                                             </a>
                                             <div class="media-body ">
                                                <small class="pull-right">2h ago</small>
                                                <strong>Janet Rosowski</strong> add 1 photo on <strong>Monica Smith</strong>.
                                                <br>
                                                <small class="text-muted">2 days ago at 8:30am</small>
                                             </div>
                                          </div>
                                          <div class="feed-element">
                                             <a href="#" class="pull-left">
                                             <img alt="image" class="img-circle" src="img/a4.jpg">
                                             </a>
                                             <div class="media-body ">
                                                <small class="pull-right text-navy">5h ago</small>
                                                <strong>Chris Johnatan Overtunk</strong> started following
                                                <strong>Monica Smith</strong>. <br>
                                                <small class="text-muted">Yesterday 1:21 pm - 11.06.2014</small>
                                                <div class="actions">
                                                   <a class="btn btn-xs btn-white"><i class="fa fa-thumbs-up"></i> Like </a>
                                                   <a class="btn btn-xs btn-white"><i class="fa fa-heart"></i> Love</a>
                                                </div>
                                             </div>
                                          </div>
                                          <div class="feed-element">
                                             <a href="#" class="pull-left">
                                             <img alt="image" class="img-circle" src="img/a5.jpg">
                                             </a>
                                             <div class="media-body ">
                                                <small class="pull-right">2h ago</small>
                                                <strong>Kim Smith</strong> posted message on <strong>Monica Smith</strong>                                                                site. <br>
                                                <small class="text-muted">Yesterday 5:20 pm - 12.06.2014</small>
                                                <div class="well">
                                                   Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy
                                                   text ever since the 1500s. Over the years, sometimes
                                                   by accident, sometimes on purpose (injected humour and
                                                   the like).
                                                </div>
                                             </div>
                                          </div>
                                          <div class="feed-element">
                                             <a href="#" class="pull-left">
                                             <img alt="image" class="img-circle" src="img/profile.jpg">
                                             </a>
                                             <div class="media-body ">
                                                <small class="pull-right">23h ago</small>
                                                <strong>Monica Smith</strong> love <strong>Kim Smith</strong>.
                                                <br>
                                                <small class="text-muted">2 days ago at 2:30 am - 11.06.2014</small>
                                             </div>
                                          </div>
                                          <div class="feed-element">
                                             <a href="#" class="pull-left">
                                             <img alt="image" class="img-circle" src="img/a7.jpg">
                                             </a>
                                             <div class="media-body ">
                                                <small class="pull-right">46h ago</small>
                                                <strong>Mike Loreipsum</strong> started following <strong>Monica Smith</strong>.
                                                <br>
                                                <small class="text-muted">3 days ago at 7:58 pm - 10.06.2014</small>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="tab-pane" id="tab-2">
                                      
                                       <div class="form-horizontal">
                                                                                   <div class="hr-line-dashed"></div>
                                          <div class="form-group">
                                             <label class="col-lg-2 control-label">Email</label>
                                             <div class="col-lg-5"><input type="text" disabled :placeholder="user.email" class="form-control"></div>
                                          </div>
                                          <div class="form-group">
                                             <label class="col-lg-2 control-label">Username</label>
                                             <div class="col-lg-5"><input type="text" disabled :placeholder="user.username" class="form-control"></div>
                                          </div>
                                          <div class="form-group">
                                             <label class="col-lg-2 control-label">Password</label>
                                             <div class="col-lg-5">
                                                <button class="btn btn-white" type="submit"> <i class="fa fa-lock"></i> Change password</button>
                                             </div>
                                          </div>
                                          <div class="hr-line-dashed"></div>
                                          <div class="form-group">
                                             <label class="col-sm-2 control-label">Avatar</label>
                                             <div class="col-sm-5">
                                                <img v-if="user.avatar" alt="image" class="img-circle" :src="user.avatar.avatar2x">
                                                <avatar v-else class="img-circle" :size="64" :username="user.full_name"></avatar>
                                                <button class="btn btn-white col-sm-offset-1" @click="toggleShow"> {{change_avatar_button_message}}</button>
                                             </div>
                                          </div>
                                          <div class="form-group">
                                             <div class="col-sm-7 col-sm-offset-2">
                                                <upload-avatar 
                                                   @crop-success="cropImg"
                                                   @crop-upload-success="cropUploadSuccess"
                                                   v-model="show"
                                                   :width="128"
                                                   :height="128"
                                                   :headers="headers"
                                                   img-format="png"></upload-avatar>
                                             </div>
                                          </div>
                                          <div class="form-group">
                                             <label class="col-sm-2 control-label">Name</label>
                                             <div class="col-sm-4"><input type="text" placeholder="First Name" v-model="user.first_name" class="form-control"></div>
                                             <div class="col-sm-4"><input type="text" placeholder="Last Name" v-model="user.last_name" class="form-control"></div>
                                          </div>
                                          <div class="form-group">
                                             <label class="col-sm-2 control-label">About me</label>
                                             <div class="col-sm-8"><textarea type="text" v-model="user.about_me" class="form-control"></div>
                                          </div>
                                          <div class="form-group">
                                             <label class="col-sm-2 control-label">Gender</label>
                                             <div class="col-sm-4">
                                                <select class="form-control" v-model="user.gender" name="account">
                                                   <option value="Idw">I don't want to tell</option>
                                                   <option value="Man">Man</option>
                                                   <option value="Woman">Woman</option>
                                                </select>
                                             </div>
                                          </div>
                                          <!--<div class="form-group">
                                             <label class="col-sm-2 control-label">Phone</label>
                                             <div class="col-sm-4"><input type="text" v-mask="'(###) ###-####'" placeholder="(###) ###-####" class="form-control"></div>
                                          </div>
                                          <div class="form-group">
                                             <label class="col-sm-2 control-label">Birthday</label>
                                             <div class="col-sm-4"><input type="text" v-mask="'##-##-####'" placeholder="mm-dd-yyyy" class="form-control"></div>
                                          </div>-->
                                          <div class="hr-line-dashed"></div>
                                          <div class="form-group">
                                             <label class="col-lg-2 control-label">Major</label>
                                             <div class="col-lg-5">
                                                <select class="form-control" v-model="user.major" name="account">
                                                   <option v-for="major in majors" :value="major.id">{{major.major_short}}</option>
                                                </select>
                                             </div>
                                          </div>
                                          <div class="form-group">
                                             <label class="col-lg-2 control-label">Class of</label>
                                             <div class="col-lg-5">
                                                <select class="form-control" v-model="user.school_year" name="account">
                                                   <option>I'm class of...</option>
                                                   <option>2016</option>
                                                   <option>2017</option>
                                                   <option>2018</option>
                                                   <option>2019</option>
                                                   <option>2020</option>
                                                </select>
                                             </div>
                                          </div>
                                          <div class="hr-line-dashed"></div>
                                          <div class="form-group">
                                             <div class="col-sm-4 col-sm-offset-2">
                                                <button class="btn btn-primary" @click="postChange()">Save changes</button>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="tab-pane" id="tab-3">
                                       <table class="table table-striped">
                                          <thead>
                                             <tr>
                                                <th>Status</th>
                                                <th>Title</th>
                                                <th>Start Time</th>
                                                <th>End Time</th>
                                                <th>Comments</th>
                                             </tr>
                                          </thead>
                                          <tbody>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Completed</span>
                                                </td>
                                                <td>
                                                   Create project in webapp
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here',
                                                      making it look like readable.
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Accepted</span>
                                                </td>
                                                <td>
                                                   Various versions
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Sent</span>
                                                </td>
                                                <td>
                                                   There are many variations
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by
                                                      injected humour, or randomised words which
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Reported</span>
                                                </td>
                                                <td>
                                                   Latin words
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      Latin words, combined with a handful of model sentence structures
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Accepted</span>
                                                </td>
                                                <td>
                                                   The generated Lorem
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Sent</span>
                                                </td>
                                                <td>
                                                   The first line
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Reported</span>
                                                </td>
                                                <td>
                                                   The standard chunk
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Completed</span>
                                                </td>
                                                <td>
                                                   Lorem Ipsum is that
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here',
                                                      making it look like readable.
                                                   </p>
                                                </td>
                                             </tr>
                                             <tr>
                                                <td>
                                                   <span class="label label-primary"><i class="fa fa-check"></i> Sent</span>
                                                </td>
                                                <td>
                                                   Contrary to popular
                                                </td>
                                                <td>
                                                   12.07.2014 10:10:1
                                                </td>
                                                <td>
                                                   14.07.2014 10:16:36
                                                </td>
                                                <td>
                                                   <p class="small">
                                                      Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical
                                                   </p>
                                                </td>
                                             </tr>
                                          </tbody>
                                       </table>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>
<script>
    import Upload from 'components/UploadAvatar'
    import * as cookie from 'utils/cookie'
    import Avatar from 'vue-avatar'

    export default {
        name: 'Profile',
        components: {
            'upload-avatar': Upload,
            'avatar': Avatar.Avatar
        },
        data: () => {
            return {
                show: false,
                user: {
                    about_me: '',
                    email: '',
                    birthday: null,
                    created: '',
                    gender: '',
                    first_name: '',
                    classrooms: [],
                    phone: '',
                    last_name: '',
                    last_login: null,
                    level: 1,
                    major: '',
                    pending_friends: '',
                    professor: '',
                    school_year: '',
                    tasks: '',
                    username: ''
                },
                majors: [],
                change_avatar_button_message: 'Change avatar',
                img_data: '',
                headers: {
                    'Authorization': 'JWT ' + cookie.getCookie("token"),
                    'X-CSRFToken': cookie.getCookie('csrftoken')
                }
            }
        },
        methods: {
            editName() {
                // TODO
            },
            postChange() {
                this.$store.dispatch('updateSelf', this.user)
            },
            loadData() {
                this.user = this.$store.getters.me
                this.$store.dispatch('getMajors')
                    .then(() => {
                        this.majors = this.$store.getters.majors
                    })
                // else {
                //     // TODO: cannot load user immediatily after dispath getUser
                //     this.$store.dispatch('getUser', this.$route.params.user_id)
                //     this.user = this.$store.getters.loadedUser
                // }
            },
            toggleShow() {
                this.show = !this.show
                if (this.show)
                    this.change_avatar_button_message = 'Cancel'
                else
                    this.change_avatar_button_message = 'Change avatar'
            },
            majorByID(id) {
                for (let i in this.majors) {
                    if (this.majors[i].id === id)
                        return this.majors[i].major_short
                }
                return ''
            },
            cropImg(img_data) {
                this.img_data = img_data
            },
            cropUploadSuccess(jsonData, field) {
                this.$store.dispatch('getSelf')
            }
        },
        created() {
            this.loadData()
        },
        // watch: {
        //     // execute getClassroomData if route changes
        //     '$route': 'getUser',
        // },
    }

</script>
