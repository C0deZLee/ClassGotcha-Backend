<template>
   <div id="right-sidebar" class="animated">
      <div class="sidebar-container">
         <ul class="nav nav-tabs navs-2">
            <li class="active"><a data-toggle="tab" href="#tab-1">
               Chats
               </a>
            </li>
            <li><a data-toggle="tab" href="#tab-2">
               Friends
               </a>
            </li>
         </ul>
         <div class="tab-content">
            <div id="tab-1" class="tab-pane active">
               <div class="sidebar-title">
                  <h3> <i class="fa fa-comments-o"></i> Recent Chats</h3>
                  <small><i class="fa fa-tim"></i> You have 0 new message.</small>
               </div>
               <div>
                  <div v-for="chatroom in chatrooms" class="sidebar-message" >
                     <a :href="chatroomUrl(chatroom)">
                        <div class="pull-left text-center">
                           <img  class="img-circle message-avatar" >
                           <div class="m-t-xs">
                              <i class="fa fa-star text-warning"></i>
                              <i class="fa fa-star text-warning"></i>
                           </div>
                        </div>
                        <div class="media-body">
                           {{chatroom.name}}
                           <br>
                           <div v-if="chatroom.latest_message">
                              <strong>{{chatroom.latest_message.full_name}}</strong>: {{chatroom.latest_message.message}}
                              <br>
                              <br>
                              <small class="text-muted">{{chatroom.latest_message.created}}</small>
                           </div>
                        </div>
                     </a>
                  </div>
               </div>
            </div>
            <div id="tab-2" class="tab-pane">
               <div class="sidebar-title">
                  <h3> <i class="fa fa-cube"></i> Latest projects</h3>
                  <small><i class="fa fa-tim"></i> You have 14 projects. 10 not completed.</small>
               </div>
               <ul class="sidebar-list">
                  <li>
                     <a href="#">
                        <div class="small pull-right m-t-xs">9 hours ago</div>
                        <h4>Business valuation</h4>
                        It is a long established fact that a reader will be distracted.
                        <div class="small">Completion with: 22%</div>
                        <div class="progress progress-mini">
                           <div style="width: 22%;" class="progress-bar progress-bar-warning"></div>
                        </div>
                        <div class="small text-muted m-t-xs">Project end: 4:00 pm - 12.06.2014</div>
                     </a>
                  </li>
                  <li>
                     <a href="#">
                        <div class="small pull-right m-t-xs">9 hours ago</div>
                        <h4>Contract with Company </h4>
                        Many desktop publishing packages and web page editors.
                        <div class="small">Completion with: 48%</div>
                        <div class="progress progress-mini">
                           <div style="width: 48%;" class="progress-bar"></div>
                        </div>
                     </a>
                  </li>
                  <li>
                     <a href="#">
                        <div class="small pull-right m-t-xs">9 hours ago</div>
                        <h4>Meeting</h4>
                        By the readable content of a page when looking at its layout.
                        <div class="small">Completion with: 14%</div>
                        <div class="progress progress-mini">
                           <div style="width: 14%;" class="progress-bar progress-bar-info"></div>
                        </div>
                     </a>
                  </li>
                  <li>
                     <a href="#">
                        <span class="label label-primary pull-right">NEW</span>
                        <h4>The generated</h4>
                        There are many variations of passages of Lorem Ipsum available.
                        <div class="small">Completion with: 22%</div>
                        <div class="small text-muted m-t-xs">Project end: 4:00 pm - 12.06.2014</div>
                     </a>
                  </li>
                  <li>
                     <a href="#">
                        <div class="small pull-right m-t-xs">9 hours ago</div>
                        <h4>Business valuation</h4>
                        It is a long established fact that a reader will be distracted.
                        <div class="small">Completion with: 22%</div>
                        <div class="progress progress-mini">
                           <div style="width: 22%;" class="progress-bar progress-bar-warning"></div>
                        </div>
                        <div class="small text-muted m-t-xs">Project end: 4:00 pm - 12.06.2014</div>
                     </a>
                  </li>
                  <li>
                     <a href="#">
                        <div class="small pull-right m-t-xs">9 hours ago</div>
                        <h4>Contract with Company </h4>
                        Many desktop publishing packages and web page editors.
                        <div class="small">Completion with: 48%</div>
                        <div class="progress progress-mini">
                           <div style="width: 48%;" class="progress-bar"></div>
                        </div>
                     </a>
                  </li>
                  <li>
                     <a href="#">
                        <div class="small pull-right m-t-xs">9 hours ago</div>
                        <h4>Meeting</h4>
                        By the readable content of a page when looking at its layout.
                        <div class="small">Completion with: 14%</div>
                        <div class="progress progress-mini">
                           <div style="width: 14%;" class="progress-bar progress-bar-info"></div>
                        </div>
                     </a>
                  </li>
                  <li>
                     <a href="#">
                        <span class="label label-primary pull-right">NEW</span>
                        <h4>The generated</h4>
                        <!--<div class="small pull-right m-t-xs">9 hours ago</div>-->
                        There are many variations of passages of Lorem Ipsum available.
                        <div class="small">Completion with: 22%</div>
                        <div class="small text-muted m-t-xs">Project end: 4:00 pm - 12.06.2014</div>
                     </a>
                  </li>
               </ul>
            </div>
         </div>
      </div>
   </div>
</template>
<script>
    export default {
        name: 'RightSideBar',
        data: function() {
            return {}
        },
        computed: {
            chatrooms() {
                return this.$store.getters.userChatrooms
            },
            friends() {
                return this.$store.getters.userFriends
            }
        },
        methods: {
            chatroomUrl: function(chatroom) { if (chatroom) return '/#/chatroom/id/' + chatroom.id }
        }
    }

</script>
