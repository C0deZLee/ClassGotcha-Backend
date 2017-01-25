<template>
      <div >
          <div class="row  border-bottom white-bg dashboard-header">
            <div class="col-sm-4">
                <h2>Welcome back! {{username()}}! Your token is {{token()}}</h2>
                <small>Here is something you need to do today</small>
                <ul class="list-group clear-list m-t">
                    <li class="list-group-item fist-item">
                                        <span class="pull-right">
                                            10:30 am
                                        </span>
                        <span class="label label-success">1</span> Adviser meeting
                    </li>
                    <li class="list-group-item">
                                        <span class="pull-right">
                                            6:30 am
                                        </span>
                        <span class="label label-info">2</span> Attend CS311's help Session
                    <li class="list-group-item">
                                        <span class="pull-right">
                                            08:00 pm
                                        </span>
                        <span class="label label-primary">3</span> Art classs drawing due
                    </li>
                    <li class="list-group-item">
                                        <span class="pull-right">
                                            11:00 pm
                                        </span>
                        <span class="label label-default">4</span> Reading material feedback due
                    </li>
                    <li class="list-group-item">
                                        <span class="pull-right">
                                            12:00 am
                                        </span>
                        <span class="label label-primary">5</span> CS465 Homework submission
                    </li>
                </ul>
            </div>
            <div class="col-sm-8">
                  <div ui-calendar="uiConfig.calendar"  class="calendar" ng-model="eventSources"></div>
            </div>
          </div>


  <div class="row">
    <div class="col-lg-12">
      <div class="wrapper wrapper-content">
        <div class="row">
          <div class="col-lg-4">
              <div class="ibox float-e-margins">
                  <div class="ibox-title">
                      <h5>New Message!</h5> <span class="label label-primary">IN+</span>
                      <div ibox-tools></div>
                  </div>
                  <div class="ibox-content">
                      <div>

                          <div class="pull-right text-right">
                              <bar-chart data="main.BarChart.data" options="main.BarChart.options"></bar-chart>
                              <br/>
                              <small class="font-bold">4/10 14:05pm</small>
                          </div>
                          <h4>CS 311 TA replied your question!
                              <br/>
                              <small class="m-r"><a ui-sref="flot_chart"> Click here to see! </a></small>
                          </h4>
                      </div>
                  </div>
              </div>
              <div class="ibox float-e-margins">
                  <div class="ibox-title">
                      <h5>Read below comments and tweets</h5>
                      <div ibox-tools></div>
                  </div>
                  <div class="ibox-content no-padding">
                      <ul class="list-group">
                          <li class="list-group-item">
                              <p><a class="text-info" href="">@ Monica smith</a>The class notes of CS311 this week is up, check it out if you miss anyof them.</p>
                              <small class="block text-muted"><i class="fa fa-clock-o"></i> 1 minuts ago</small>
                          </li>
                          <li class="list-group-item">
                              <p><a class="text-info" href="">@mick Smith</a> Thanks for note, it was pretty helpful!</p>
                              <div class="text-center m">
                                  <span id="sparkline8"></span>
                              </div>
                              <small class="block text-muted"><i class="fa fa-clock-o"></i> 2 hours ago</small>
                          </li>
                          <li class="list-group-item">
                              <p><a class="text-info" href="">@Kevin Smith</a> The math Home work is due on Wednesday , instructor extended the DL agian :) </p>
                              <small class="block text-muted"><i class="fa fa-clock-o"></i> 2 minuts ago</small>
                          </li>
                          <li class="list-group-item ">
                              <p><a class="text-info" href="">@Jonathan Febrick</a> Finished the Drawing project, The requiremnt for the detail was high this time </p>
                              <small class="block text-muted"><i class="fa fa-clock-o"></i> 1 hour ago</small>
                          </li>
                          <li class="list-group-item">
                              <p><a class="text-info" href="">@Alan Marry</a> @Jonathan have not started the drawing project yet, still need more tool for this projects:)</p>
                              <small class="block text-muted"><i class="fa fa-clock-o"></i> 1 minuts ago</small>
                          </li>
                          <li class="list-group-item">
                              <p><a class="text-info" href="">@Kevin Smith</a> Anyone wannt to do the CS311 projects after the help session  </p>
                              <small class="block text-muted"><i class="fa fa-clock-o"></i> 2 minuts ago</small>
                          </li>
                      </ul>
                  </div>
              </div>
          </div>
          <div class="col-lg-4">
              <div class="ibox float-e-margins">
                  <div class="ibox-title">
                      <h5>Your daily feed</h5>

                      <!-- This is example of local custom ibox tools -->
                      <div class="ibox-tools">
                          <span class="label label-warning-light">10 Messages</span>
                      </div>
                  </div>
                  <div class="ibox-content">

                      <div>
                          <div class="feed-activity-list">

                              <div class="feed-element">
                                 <a ui-sref="profile" class="pull-left">
                                      <img alt="image" class="img-circle" src="modules/classrooms/img/profile.jpg">
                                  </a>

                                  <div class="media-body ">
                                      <small class="pull-right">2h ago</small>
                                      <strong>Monica Smith</strong> posted notes of CS221. <br>
                                      <small class="text-muted">Today 5:60 pm - 12.06.2014</small>

                                  </div>
                              </div>

                              <div class="feed-element">
                                  <a ui-sref="profile" class="pull-left">
                                      <img alt="image" class="img-circle" src="modules/classrooms/img/a2.jpg">
                                  </a>

                                  <div class="media-body ">
                                      <small class="pull-right">1h ago</small>
                                      <strong>Mark Johnson</strong> added memo on <strong>Monica Smith's</strong> note. <br>
                                      <small class="text-muted">Today 7:10 pm - 12.06.2014</small>
                                  </div>
                              </div>
                              <div class="feed-element">
                                  <a ui-sref="profile" class="pull-left">
                                      <img alt="image" class="img-circle" src="modules/classrooms/img/a3.jpg">
                                  </a>

                                  <div class="media-body ">
                                      <small class="pull-right">30min ago</small>
                                      <strong>Janet Rosowski</strong> add 1 photo on <strong>Monica Smith's note</strong>. <br>
                                      <small class="text-muted">2 days ago at 8:30am</small>
                                  </div>
                              </div>
                              <div class="feed-element">
                                  <a ui-sref="profile" class="pull-left">
                                      <img alt="image" class="img-circle" src="modules/classrooms/img/a4.jpg">
                                  </a>

                                  <div class="media-body ">
                                      <small class="pull-right text-navy">5h ago</small>
                                      <strong>Chris Johnatan Overtunk</strong> started following <strong>Monica Smith</strong>. <br>
                                      <small class="text-muted">Yesterday 1:21 pm - 11.06.2014</small>
                                      <div class="actions">
                                          <a class="btn btn-xs btn-white"><i class="fa fa-thumbs-up"></i> Like </a>
                                          <a class="btn btn-xs btn-white"><i class="fa fa-heart"></i> Love</a>
                                      </div>
                                  </div>
                              </div>
                              <div class="feed-element">
                                  <a ui-sref="profile" class="pull-left">
                                      <img alt="image" class="img-circle" src="modules/classrooms/img/a5.jpg">
                                  </a>

                                  <div class="media-body ">
                                      <small class="pull-right">2h ago</small>
                                      <strong>Kim Smith</strong> posted message on <strong>Monica Smith</strong> site. <br>
                                      <small class="text-muted">Yesterday 5:20 pm - 12.06.2014</small>
                                      <div class="well">
                                          I was absent on Tuesday's CS 311 class,Is it  possible that someone can share the notes
                                          with me? .
                                      </div>
                                      <div class="pull-right">
                                          <a class="btn btn-xs btn-white"><i class="fa fa-thumbs-up"></i> Like </a>
                                      </div>
                                  </div>
                              </div>
                              <div class="feed-element">
                                  <a ui-sref="profile" class="pull-left">
                                      <img alt="image" class="img-circle" src="modules/classrooms/img/profile.jpg">
                                  </a>

                                  <div class="media-body ">
                                      <small class="pull-right">23h ago</small>
                                      <strong>Monica Smith</strong> started following <strong>Kim Smith</strong>. <br>
                                      <small class="text-muted">2 days ago at 2:30 am - 11.06.2014</small>
                                  </div>
                              </div>
                              <div class="feed-element">
                                  <a ui-sref="profile" class="pull-left">
                                      <img alt="image" class="img-circle" src="modules/classrooms/img/a7.jpg">
                                  </a>

                                  <div class="media-body ">
                                      <small class="pull-right">46h ago</small>
                                      <strong>Mike Loreipsum</strong> started following <strong>Monica Smith</strong>. <br>
                                      <small class="text-muted">3 days ago at 7:58 pm - 10.06.2014</small>
                                  </div>
                              </div>
                          </div>

                          <button class="btn btn-primary btn-block m-t"><i class="fa fa-arrow-down"></i> Show More</button>

                      </div>

                  </div>
              </div>

          </div>
          <div class="col-lg-4">
              <div class="ibox float-e-margins">
                  <div class="ibox-title">
                      <h5>Your Schedule Today</h5>
                      <div ibox-tools></div>
                  </div>
                  <div class="ibox-content ibox-heading">
                      <h3>You have meeting today!</h3>
                      <small><i class="fa fa-map-marker"></i> First Meeting is on 10:30am. Check your schedule to see detail.</small>
                  </div>
                  <div class="ibox-content inspinia-timeline">

                      <div class="timeline-item">
                          <div class="row">
                              <div class="col-xs-3 date">
                                  <i class="fa fa-briefcase"></i>
                                  10:30 am
                                  <br/>
                                  <small class="text-navy">2 hour ago</small>
                              </div>
                              <div class="col-xs-7 content no-top-border">
                                  <p class="m-b-xs"><strong>Meeting</strong></p>

                                  <p>meeet with adiver Mahon and talk about the schedule next semester .</p>

                                  <p><line-chart data="main.LineChart.data" options="main.LineChart.options"></line-chart></p>
                              </div>
                          </div>
                      </div>
                      <div class="timeline-item">
                          <div class="row">
                              <div class="col-xs-3 date">
                                  <i class="fa fa-file-text"></i>
                                  11:30 am
                                  <br/>
                                  <small class="text-navy"></small>
                              </div>
                              <div class="col-xs-7 content">
                                  <p class="m-b-xs"><strong>Forward the scedule to registration office</strong></p>

                                  <p>After the talk with adviser then forward the new schedule to the registration offcie.Before their
                                  lunch time such that we get the schedule updated before the end of the day. </p>
                              </div>
                          </div>
                      </div>

                      <div class="timeline-item">
                          <div class="row">
                              <div class="col-xs-3 date">
                                  <i class="fa fa-phone"></i>
                                  6:30 pm
                                  <br/>
                                  <small class="text-navy"></small>
                              </div>
                              <div class="col-xs-7 content">
                                  <p class="m-b-xs"><strong>CS311 help session</strong></p>

                                  <p>
                                      Join the help session hold by Dr,Mcdaniel and talk with TAs about the bizzare bugs:(
                                  </p>
                              </div>
                          </div>
                      </div>
                      <div class="timeline-item">
                          <div class="row">
                              <div class="col-xs-3 date">
                                  <i class="fa fa-user-md"></i>
                                  08:00 pm
                                  <br/>
                                                     </div>
                              <div class="col-xs-7 content">
                                  <p class="m-b-xs"><strong>Submit the drawing homework </strong></p>

                                  <p>
                                      Finish the Drwing home work and submit hte draft on the course lab
                                  </p>
                              </div>
                          </div>
                      </div>
                      <div class="timeline-item">
                          <div class="row">
                              <div class="col-xs-3 date">
                                  <i class="fa fa-comments"></i>
                                  12:00 am
                                  <br/>
                              </div>
                              <div class="col-xs-7 content">
                                  <p class="m-b-xs"><strong>Submit the CS 465 homework</strong></p>

                                  <p>
                                      The new sorting algorithm still have to be edited, after the editing submit it to the course dropbox
                                  </p>
                              </div>
                          </div>
                      </div>

                  </div>
              </div>
          </div>
      </div>
      </div>
    </div>

  <div class="small-chat-box ng-small-chat fadeInRight animated">

      <div class="heading" draggable="true">
          <small class="chat-date pull-right">
              02.19.2015
          </small>
          Small chat
      </div>

      <div class="content chat-slim-scroll" >

          <div class="left">
              <div class="author-name">
                  Monica smith <small class="chat-date">
                  10:02 am
              </small>
              </div>
              <div class="chat-message active">
                  The class notes of CS311 this week is up, check it out if you miss anyof them.
              </div>

          </div>
          <div class="right">
              <div class="author-name">
                  Mick Smith
                  <small class="chat-date">
                      11:24 am
                  </small>
              </div>
              <div class="chat-message">
                  Thanks for note, it was pretty helpful
              </div>
          </div>
          <div class="left">
              <div class="author-name">
                  Alice Novak
                  <small class="chat-date">
                      08:45 pm
                  </small>
              </div>
              <div class="chat-message active">
                The math Home work is due on Wednesday , instructor extended the DL agian :)
               </div>
          </div>
          <div class="right">
              <div class="author-name">
                  Anna Lamson
                  <small class="chat-date">
                      11:24 am
                  </small>
              </div>
              <div class="chat-message">
                  The standard chunk of Lorem Ipsum
              </div>
          </div>
          <div class="left">
              <div class="author-name">
                  Mick Lane
                  <small class="chat-date">
                      08:45 pm
                  </small>
              </div>
              <div class="chat-message active">
                  I belive that. Lorem Ipsum is simply dummy text.
              </div>
          </div>


      </div>
      <div class="form-chat">
          <div class="input-group input-group-sm"><input type="text" class="form-control"> <span class="input-group-btn"> <button
                  class="btn btn-primary" type="button">Send
          </button> </span></div>
      </div>


  <div id="small-chat">
      <span class="badge badge-warning pull-right">5</span>
      <a class="open-small-chat">
          <i class="fa fa-comments"></i>
      </a>


  <div class="modal inmodal" id="uploadAvatar" tabindex="-1" role="dialog" aria-hidden="true"
       style="display: none;">
      <div class="modal-dialog">
          <div class="modal-content animated fadeIn">
              <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span
                          class="sr-only">Close</span></button>
                  <h4 class="modal-title">Course Syllabus</h4>
              </div>
              <div class="modal-body">

              </div>

              <div class="modal-footer">
              </div>
          </div>
      </div>
  </div>


</template>

<script>
    import * as cookie from '../utils/cookie'
    export default {
        name: 'Home',
        methods: {
            token() {
                return cookie.getCookie('token')
            },
            username() {
                return this.$store.getters.userFullName
            }
        }
    }

</script>
