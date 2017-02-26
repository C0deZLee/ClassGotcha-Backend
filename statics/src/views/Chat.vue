<template>
  <div v-if='loaded && chatroom_name && chatroom'>
    <div class="row wrapper border-bottom white-bg page-heading">
      <div class="col-lg-10">
        <h2>{{$store.getters.currentChatroom.name}}</h2>
        <ol class="breadcrumb">
          <li>
         <router-link :to="{name:'home'}" >Home</router-link>
          </li>
          <li>
            <a>Chatrooms</a>
          </li>
          <li class="active">
            <strong>{{$store.getters.currentChatroom.name}}</strong>
          </li>
        </ol>
      </div>
      <div class="col-lg-2">
      </div>
    </div>
    <div class="wrapper wrapper-content animated fadeInRight">
      <div class="ibox chat-view">
        <div class="ibox-title">
          <small v-if="chatroom.latest_message" class="text-muted">Last message: {{chatroom.latest_message.created}}</small>
          <small v-else class="text-muted">Last message:  </small>
          <p class="pull-right">{{chatroom.accounts.length}} Users In Chatroom</p> 
        </div>
        <div class="ibox-content">
          <div class="row">
            <div class="col-md-10 col-sm-12">
              <div class="chat-discussion" id="discussion" v-bottom>
                <div v-for="message in chatroom_messages">
                  <div class="chat-message" :class="myMessage(message)">
                      
                    <img v-if="messageAvatar(message.send_from)" class="message-avatar" :src="messageAvatar(message.send_from)"> 
                    <avatar v-else class="message-avatar" :size="42" :username="message.username"></avatar>
                    <div class="message">
                      <a class="message-author"> {{message.username}} </a>
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
              <div class="chat-users hidden-sm hidden-xs">
                <div class="users-list  " >
                  <div class="chat-user" v-for="user in chatroom.accounts">
                     
                    <img v-if="user.avatar" class="chat-avatar" :src="user.avatar.avatar1x">
                    <avatar v-if="user&&!user.avatar"  class="chat-avatar" :size="42" :username="user.full_name"></avatar>
                    
                    <div class="chat-user-name">
                      <a>{{user.full_name}}</a>
                        <span class="m-l label label-warning">Level {{user.level}}</span>
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
<spinner v-else></spinner>
  
</template>
<script>
    import Avatar from 'vue-avatar'
    import Spinner from 'components/Spinner'
    import { mapGetters } from 'vuex'

    // import Debugger from 'utils/debugger'

    export default {
        name: 'Chat',
        components: {
            'avatar': Avatar.Avatar,
            'spinner': Spinner
        },
        data() {
            return {
                loaded: false,
                message_text: '',
                errorMsg: '',
            }
        },
        methods: {
            myMessage(message) {
                return this.$store.getters.userID === message.send_from ? 'right' : 'left'
            },
            messageAvatar(send_from) {
                for (let i in this.chatroom.accounts) {
                    if (this.chatroom.accounts[i].pk === send_from && this.chatroom.accounts[i].avatar)
                        return this.chatroom.accounts[i].avatar.avatar1x
                }
                return false

            },
            validateChatroom() {
                this.$store.dispatch('getChatroom', this.$route.params.chatroom_id)
                    .then(() => {
                        this.$store.dispatch('validateChatroom', parseInt(this.$route.params.chatroom_id))
                            .then(() => {
                                this.loaded = true
                            })
                            .catch((error) => {
                                this.$router.push({ name: 'home' })
                                throw error
                            })
                    })
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
            formatTime(time) {
                /* global moment:true */
                return moment.utc(time)
            }
        },
        computed: mapGetters({
            chatroom_messages: "currentChatroomMessages",
            chatroom: "currentChatroom",
            chatroom_name: "currentChatroomName"
        }),
        directives: {
            bottom: {
                inserted: (el) => {
                    el.scrollTop = el.scrollHeight
                },
                componentUpdated: (el) => {
                    el.scrollTop = el.scrollHeight
                },
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
