<template>
  <div>
  <div>
    <div class="row wrapper border-bottom white-bg page-heading">
      <div class="col-lg-10">
        <h2>{{chatroom.name}}</h2>
        <ol class="breadcrumb">
          <li>
            <a href="/#/">Home</a>
          </li>
          <li>
            <a>Chatrooms</a>
          </li>
          <li class="active">
            <strong>{{chatroom.name}}</strong>
          </li>
        </ol>
      </div>
      <div class="col-lg-2">
      </div>
    </div>
    <div class="wrapper wrapper-content animated fadeInRight">
      <div class="ibox chat-view">
        <div class="ibox-title">
          <small class="text-muted">Last message:  {{chatroom.latest_message.created}}</small>
          <p class="pull-right">{{chatroomUsers.length}} Users Online</p> 
        </div>
        <div class="ibox-content">
          <div class="row">
            <div class="col-md-10 ">
              <div class="chat-discussion" id="discussion" v-bottom>
                <div v-for="message in chatroomMessages">
                  <div class="chat-message" :class="myMessage(message)">
                    <img class="message-avatar" :src="getAvatar(message.send_from)"> 
                    <div class="message">
                      <a class="message-author" href=""> {{message.username}} </a>
                      <span class="message-date"> {{message.created}} </span>
                      <span class="message-content text-left">
                      {{message.message}}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-2">
              <div class="chat-users">
                <div class="users-list">
                  <div class="chat-user" v-for="user in chatroomUsers">
                    <img class="chat-avatar" :src="user.avatar.avatar1x" alt="">
                    <div class="chat-user-name">
                      <a>{{user.full_name}}</a>
                        <span class="label  label-warning">Level {{user.level}}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-12">
              <div class="panel-footer">
                     <div class="m-b">
                    <h3>
                      <i class="fa fa-file-image-o"></i><small>   (under development)</small>
                     </h3>
                </div>
                <div class="input-group">
                  <input  autofocus @keydown.enter="sendMessage($event)" v-model="message_text" type="text" class="form-control" placeholder="Type your message here...">
                  <span class="input-group-btn">
                  <button @click="sendMessage($event)" class="btn btn-primary">
                  Send</button>
                  </span>
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
    export default {
        name: 'Chat',
        data: function() {
            return {
                message_text: '',
                errorMsg: '',
                chatroom: {},
                chatroomUsers: {}
            }
        },
        methods: {
            myMessage(message) {
                return this.$store.getters.userID === message.send_from ? 'right' : 'left'
            },
            validateChatroom() {
                this.$store.dispatch('validateChatroom', this.$route.params.chatroom_id)
                // chat room doesn't exist or user doesn't belong to chat room, redirect
                if (this.$store.getters.validChatroom) {
                    this.$store.dispatch('getChatroom', this.$route.params.chatroom_id)
                    this.$store.dispatch('getChatroomUsers', this.$route.params.chatroom_id)
                    // after component is created
                    this.connectSocket()
                }
            },
            connectSocket() {
                this.$store.dispatch('connectSocket', this.$route.params.chatroom_id)
                this.reload()
            },
            reload() {
                this.chatroom = this.$store.getters.currentChatroom
                this.chatroomUsers = this.$store.getters.currentChatroomUsers
            },
            sendMessage(e) {
                e.preventDefault()
                if (this.message_text === '') {
                    return
                }
                const data = {
                    'message': {
                        'send_from': this.$store.getters.userID,
                        'username': this.$store.getters.userFullName,
                        'message': this.message_text,
                    },
                    pk: this.$route.params.chatroom_id
                }
                this.$store.dispatch('sendMessage', data)
                this.message_text = ''
            },
            getAvatar(user_id) {
                for (let i = 0; i < this.chatroomUsers.length; i++) {
                    if (this.chatroomUsers[i].pk === user_id)
                        return this.chatroomUsers[i].avatar.avatar1x
                }
            }
        },
        directives: {
            bottom: {
                update: (el) => {
                    el.scrollTop = el.scrollHeight
                },
                inserted: (el) => {
                    el.scrollTop = el.scrollHeight
                },
                bind: (el) => {
                    el.scrollTop = el.scrollHeight
                },
                componentUpdated: (el) => {
                    el.scrollTop = el.scrollHeight
                },
                unbind: (el) => {
                    el.scrollTop = el.scrollHeight
                },
            },
        },
        computed: {

            chatroomMessages() {
                return this.$store.getters.currentChatroomMessages
            },

        },
        created() {
            this.validateChatroom()
        },
        watch: {
            // execute getClassroomData if route changes
            '$route': 'validateChatroom'
        },

    }

</script>
