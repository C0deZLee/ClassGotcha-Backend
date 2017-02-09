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
                  <h3> <i class="fa fa-users"></i> Friend List</h3>
               </div>
                            <div>
                  <div v-for="friend in friends" class="sidebar-message" >
                     <!--<router-link>-->
                         <a>
                        <div class="pull-left text-center">
                           <img  class="img-circle message-avatar" >
                           <div class="m-t-xs">
                              <i class="fa fa-star text-warning"></i>
                              <i class="fa fa-star text-warning"></i>
                           </div>
                        </div>
                        <div class="media-body">
                           {{friend.full_name}}
                           <br>
                           <!--<div v-if="chatroom.latest_message">
                              <strong>{{chatroom.latest_message.full_name}}</strong>: {{chatroom.latest_message.message}}
                              <br>
                              <br>
                              <small class="text-muted">{{chatroom.latest_message.created}}</small>
                           </div>-->
                        </div>
                        </a>
                     <!--</router-link>-->
                  </div>
               </div>
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
