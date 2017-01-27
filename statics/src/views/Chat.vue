<template>
    <div class="wrapper wrapper-content">
        <div class="col-lg-12">

                <div class="ibox chat-view">

                    <div class="ibox-title">
                        <small class="pull-right text-muted">Last message:  Mon Jan 26 2015 - 18:39:23</small>
                         Chat room panel
                    </div>

                    <div class="ibox-content">

                        <div class="row">

                            <div class="col-md-10 ">
                                <div class="chat-discussion">
                                    <div v-for="message in chatroomMessages">
                                    <div  class="chat-message" :class="myMessage(message)">
                                        <img class="message-avatar" src="img/a1.jpg" alt="">
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
                                            <img class="chat-avatar" src="img/a4.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a>{{user.first_name}}</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="chat-message-form">
                                    <div class="form-group">
                                        <textarea @keydown.enter="sendMessage($event)" v-model="message_text" class="form-control message-input" name="message" placeholder="Enter message text"></textarea>
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
                errorMsg: ''
            }
        },
        methods: {
            myMessage: function(message) {
                return this.$store.getters.userID === message.send_from ? 'right' : 'left'
            },
            validateChatroom: function() {
                this.$store.dispatch('validateChatroom', this.$route.params.chatroom_id)
                // chat room doesn't exist or user doesn't belong to chat room, redirect
                if (this.$store.getters.validChatroom) {
                    console.log("connectSocket")
                    // after component is created, load data
                    this.connectSocket()
                }
            },
            connectSocket: function() {
                this.$store.dispatch('connectSocket', this.$route.params.chatroom_id)
                this.$store.dispatch('getChatroom', this.$route.params.chatroom_id)
                this.$store.dispatch('getChatroomUsers', this.$route.params.chatroom_id)

            },
            sendMessage: function(e) {
                e.preventDefault()
                if (this.message_text === '') {

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
            }
        },
        computed: {
            chatroomUsers() {
                return this.$store.getters.currentChatroomUsers
            },
            chatroomMessages() {
                return this.$store.getters.currentChatroomMessages
            }
        },
        created: function() {
            this.validateChatroom()
        },
        watch: {
            // execute getClassroomData if route changes
            '$route': 'validateChatroom'
        },
    }

</script>
