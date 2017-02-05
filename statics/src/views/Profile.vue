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
    <div class="wrapper wrapper-content animated fadeInUp">
      <div class="row">
        <div class="col-lg-3">
          <div class="contact-box center-version">
            <a>
              <h3>Name Card</h3>
              <img alt="image" class="img-circle" :src="user.avatar.avatar2x">
              <h3 class="m-b-xs"><strong>{{user.full_name}}</strong></h3>
              <div class="font-bold">@{{user.username}}</div>
              <span class="label label-warning">Level {{user.level}}</span>
              <div class="m-t-md">
                <strong>About Me</strong>  <i class="fa fa-edit"></i>
                <br>
                {{user.about_me}}
              </div>
            </a>
            <div class="contact-box-footer">
              <div class="m-t-xs btn-group">
                <a class="btn btn-xm btn-primary"><i class="fa fa-user-plus"></i> Send Firend Request</a>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-9">
          <div class="ibox">
            <div class="ibox-content">
              <div class="row">
                <div class="col-lg-12">
                  <div class="m-b-md">
                    <h2>Level and Awards</h2>
                  </div>
                  <dl class="dl-horizontal">
                    <dt>Level:</dt>
                    <dd>
                      <span class="label label-warning">Level {{user.level}}</span>
                    </dd>
                  </dl>
                </div>
              </div>
              <div class="row">
                <div class="col-lg-12">
                  <dl class="dl-horizontal">
                    <dt>Exp:</dt>
                    <dd>
                      <div class="progress progress-striped active m-b-sm">
                        <div style="width: 60%;" class="progress-bar"></div>
                      </div>
                      <small>Project completed in <strong>60%</strong>. Remaining close the project, sign a contract and invoice.</small>
                    </dd>
                  </dl>
                </div>
              </div>
              <div class="row">
                <div class="col-lg-12">
                  <dl class="dl-horizontal">
                    <dt>Badges:</dt>
                    <dd>
                      None
                    </dd>
                  </dl>
                </div>
              </div>
              <div class="row m-t-sm">
                <div class="col-lg-12">
                  <div class="panel blank-panel">
                    <div class="panel-heading">
                      <div class="panel-options">
                        <ul class="nav nav-tabs">
                          <li class="active"><a href="#tab-1" data-toggle="tab">Rencent activity</a></li>
                          <li class=""><a href="#tab-2" data-toggle="tab">Personal Information</a></li>
                          <li class=""><a href="#tab-4" data-toggle="tab">Security</a></li>
                          <li class="" v-if="myProfile"><a href="#tab-3" data-toggle="tab">Badges Process</a></li>
                          <li class="" v-if="myProfile"><a href="#tab-3" data-toggle="tab">Self</a></li>
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
                              <label class="col-sm-2 control-label">Avatar</label>
                              <div class="col-sm-5">
                                 <img alt="image" :src="user.avatar.avatar2x" class="img-circle circle-border">
                                <button class="btn btn-white col-sm-offset-1" @click="toggleShow"> {{change_avatar_button_message}}</button>
                                </div> 
                            </div>
                            <div class="form-group">
                                <div class="col-sm-7 col-sm-offset-2">
                                <upload-avatar 
                                @crop-success="cropImg"
                                @crop-upload-success="cropUploadSuccess"
                                v-model="show"
                                :width="512"
                                :height="512"
                                :headers="headers"
                                img-format="png"></upload-avatar>
                                </div>
                            </div>

                            <div class="form-group">
                              <label class="col-sm-2 control-label">Name</label>
                              <div class="col-sm-4"><input type="text" placeholder="First Name" class="form-control"></div>
                              <div class="col-sm-4"><input type="text" placeholder="Last Name" class="form-control"></div>
                            </div>
                                                        <div class="form-group">
                              <label class="col-sm-2 control-label">About me</label>
                              <div class="col-sm-10"><textarea type="text" :placeholder="user.about_me" class="form-control"></div>
                            </div>
                            <div class="form-group">
                              <label class="col-sm-2 control-label">Gender</label>
                              <div class="col-sm-4">
                                <select class="form-control" name="account">
                                  <option>I don't want to tell</option>
                                  <option>Man</option>
                                  <option>Woman</option>
                                </select>
                              </div>
                            </div>
                            <div class="form-group">
                              <label class="col-sm-2 control-label">Phone</label>
                              <div class="col-sm-4"><input type="text" v-mask="'(###) ###-####'" placeholder="(###) ###-####" class="form-control"></div>
                            </div>
                            <div class="form-group">
                              <label class="col-sm-2 control-label">Birthday</label>
                              <div class="col-sm-4"><input type="text" v-mask="'##-##-####'" placeholder="mm-dd-yyyy" class="form-control"></div>
                            </div>
                            <div class="hr-line-dashed"></div>
                            
                            <div class="form-group">
                              <label class="col-lg-2 control-label">Major</label>
                              <div class="col-lg-5">   <select class="form-control" name="account">
                                  <option>Select your major...</option>
                                  <option>Man</option>
                                  <option>Woman</option>
                                </select></div>
                            </div>
                            <div class="form-group">
                              <label class="col-lg-2 control-label">Class of</label>
                              <div class="col-lg-5">   <select class="form-control" name="account">
                                  <option>I'm class of...</option>
                                  <option>2016</option>
                                  <option>2017</option>
                                  <option>2018</option>
                                  <option>2019</option>
                                  <option>2020</option>
                                </select></div>
                            </div>
                            <div class="hr-line-dashed"></div>
                            <div class="form-group">
                              <div class="col-sm-4 col-sm-offset-2">

                                <button class="btn btn-primary" type="submit">Save changes</button>
                              </div>
                            </div>
                          </div>
                      
                       
                        </div>
                               <div class="tab-pane" id="tab-4">
                          <form method="get" class="form-horizontal">
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
                              <div class="col-sm-4 col-sm-offset-2">
                                <button class="btn btn-primary" type="submit">Save changes</button>
                              </div>
                            </div>
                          </form>
                      
                       
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

    export default {
        name: 'Profile',
        components: {
            'upload-avatar': Upload,
        },
        data: () => {
            return {
                show: false,
                user: {},
                change_avatar_button_message: 'Change avatar',
                img_data: '',
                headers: {
                    'Authorization': 'JWT ' + cookie.getCookie("token"),
                    'X-CSRFToken': cookie.getCookie('csrftoken')
                }
            }
        },
        computed: {
            myProfile() {
                return (this.$route.params.user_id === 'me' || this.$route.params.user_id === this.$store.getters.userID.toString())
            },
        },
        methods: {
            editName() {
                // TODO
            },
            editAboutMe() {
                // TODO
            },
            getUser() {
                if (this.$route.params.user_id === 'me')
                    this.user = this.$store.getters.me
                else {
                    // TODO: cannot load user immediatily after dispath getUser
                    this.$store.dispatch('getUser', this.$route.params.user_id)
                    this.user = this.$store.getters.loadedUser
                }
            },
            toggleShow() {
                this.show = !this.show
                if (this.show)
                    this.change_avatar_button_message = 'Cancel'
                else
                    this.change_avatar_button_message = 'Change avatar'

            },
            cropImg(img_data) {
                this.img_data = img_data
            },
            cropUploadSuccess(jsonData, field) {
                this.$store.dispatch('getSelf')
            }
        },
        created() {
            this.getUser()
        },
        watch: {
            // execute getClassroomData if route changes
            '$route': 'getUser',
        },
    }

</script>
