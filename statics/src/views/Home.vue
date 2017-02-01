<template>
<div>
          <div class="row  border-bottom white-bg dashboard-header">
            <div class="col-sm-3">
                <h2>Welcome back! {{username()}}! </h2><br>
                <p>Here are tasks we recommand you to do today!</p>
              
        <div class="ibox-content">
                    <div id='external-events'>
                        <p>Drag a event and drop into callendar.</p>
                        <div class='external-event navy-bg'>Go to shop and buy some products.</div>
                        <div class='external-event navy-bg'>Check the new CI from Corporation.</div>
                        <div class='external-event navy-bg'>Send documents to John.</div>
                        <div class='external-event navy-bg'>Phone to Sandra.</div>
                        <div class='external-event navy-bg'>Chat with Michael.</div>
                    </div>
                </div>
                    <br>
                <p>Here are your tasks today!</p>
                    
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
                <button class="btn btn-primary pull-right">See detail</button>
            </div>
            <div class="col-sm-9">
                <full-calendar :events="events"></full-calendar>
            </div>
          </div>


  <div class="row">
    <div class="col-lg-12">
      <div class="wrapper wrapper-content">
        <div class="row">
          <div class="col-lg-4">
              <div class="ibox float-e-margins">
                    <div class="ibox-title">
                        <h5>Small todo list</h5>
                        <div class="ibox-tools">
                            <a class="collapse-link">
                                <i class="fa fa-chevron-up"></i>
                            </a>
                            <a class="close-link">
                                <i class="fa fa-times"></i>
                            </a>
                        </div>
                    </div>
                    <div class="ibox-content">
                        <ul class="todo-list m-t small-list">
                            <li>
                                <a href="#" class="check-link"><i class="fa fa-check-square"></i> </a>
                                <span class="m-l-xs todo-completed">Buy a milk</span>

                            </li>
                            <li>
                                <a href="#" class="check-link"><i class="fa fa-check-square"></i> </a>
                                <span class="m-l-xs todo-completed">Go to shop and find some products.</span>

                            </li>
                            <li>
                                <a href="#" class="check-link"><i class="fa fa-square-o"></i> </a>
                                <span class="m-l-xs">Send documents to Mike</span>
                                <small class="label label-primary"><i class="fa fa-clock-o"></i> 1 mins</small>
                            </li>
                            <li>
                                <a href="#" class="check-link"><i class="fa fa-square-o"></i> </a>
                                <span class="m-l-xs">Go to the doctor dr Smith</span>
                            </li>
                            <li>
                                <a href="#" class="check-link"><i class="fa fa-square-o"></i> </a>
                                <span class="m-l-xs">Plan vacation</span>
                            </li>
                            <li>
                                <a href="#" class="check-link"><i class="fa fa-square-o"></i> </a>
                                <span class="m-l-xs">Create new stuff</span>
                            </li>
                            <li>
                                <a href="#" class="check-link"><i class="fa fa-square-o"></i> </a>
                                <span class="m-l-xs">Call to Anna for dinner</span>
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

  </div>
           <div class="small-chat-box fadeInRight animated">

            <div class="heading" draggable="true">
                <small class="chat-date pull-right">
                    02.19.2015
                </small>
                Small chat
            </div>

            <div class="content">

                <div class="left">
                    <div class="author-name">
                        Monica Jackson <small class="chat-date">
                        10:02 am
                    </small>
                    </div>
                    <div class="chat-message active">
                        Lorem Ipsum is simply dummy text input.
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
                        Lorem Ipsum is simpl.
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
                        Check this stock char.
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
                <div class="input-group input-group-sm">
                    <input type="text" class="form-control">
                    <span class="input-group-btn"> <button
                        class="btn btn-primary" type="button">Send
                </button> </span></div>
            </div>

        </div>
  <div id="small-chat">
      <span class="badge badge-warning pull-right">5</span>
      <a class="open-small-chat">
          <i class="fa fa-comments"></i>
      </a>

  </div>
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
  </div>


</template>

<script>
    import Calendar from 'components/Calendar'

    import * as cookie from '../utils/cookie'
    export default {
        name: 'Home',
        data() {
            return {
                events: []
            }
        },
        components: {
            'full-calendar': Calendar
        },
        methods: {
            token() {
                return cookie.getCookie('token')
            },
            username() {
                return this.$store.getters.userFullName
            }
        },
        created() {
            let event_list = []
            for (let counter in this.$store.getters.userClassrooms) {
                const classroom = this.$store.getters.userClassrooms[counter]
                console.log(classroom)
                // classes
                event_list.push({
                    currentTimezone: 'UTC',
                    title: classroom.class_time.task_name + '\n' + classroom.class_time.location,

                    start: classroom.class_time.formatted_start_time,
                    end: classroom.class_time.formatted_end_time,
                    dow: classroom.class_time.repeat_list,
                    repeat: [{
                        start: classroom.semester.formatted_start_date,
                        end: classroom.semester.formatted_end_date
                    }]
                })

            }
            this.events = event_list
        },
        mounted() {
            /* global $:true */
            $('#external-events div.external-event').each(function() {

                // store data so the calendar knows to render an event upon drop
                $(this).data('event', {
                    title: $.trim($(this).text()), // use the element's text as the event title
                    stick: false // maintain when user navigates (see docs on the renderEvent method)
                })

                // make the event draggable using jQuery UI
                $(this).draggable({
                    zIndex: 10,
                    revert: true, // will cause the event to go back to its
                    revertDuration: 0 //  original position after the drag
                })

            })
        }
    }

</script>
