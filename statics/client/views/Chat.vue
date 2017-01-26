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

                            <div class="col-md-9 ">
                                <div class="chat-discussion">

                                    <div class="chat-message left">
                                        <img class="message-avatar" src="img/a1.jpg" alt="">
                                        <div class="message">
                                            <a class="message-author" href="#"> Michael Smith </a>
											<span class="message-date"> Mon Jan 26 2015 - 18:39:23 </span>
                                            <span class="message-content">
											Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
                                            </span>
                                        </div>
                                    </div>
                                    <div class="chat-message right">
                                        <img class="message-avatar" src="img/a4.jpg" alt="">
                                        <div class="message">
                                            <a class="message-author" href="#"> Karl Jordan </a>
                                            <span class="message-date">  Fri Jan 25 2015 - 11:12:36 </span>
                                            <span class="message-content">
											Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover.
                                            </span>
                                        </div>
                                    </div>
                                    <div class="chat-message right">
                                        <img class="message-avatar" src="img/a2.jpg" alt="">
                                        <div class="message">
                                            <a class="message-author" href="#"> Michael Smith </a>
                                            <span class="message-date">  Fri Jan 25 2015 - 11:12:36 </span>
                                            <span class="message-content">
											There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration.
                                            </span>
                                        </div>
                                    </div>
                                    <div class="chat-message left">
                                        <img class="message-avatar" src="img/a5.jpg" alt="">
                                        <div class="message">
                                            <a class="message-author" href="#"> Alice Jordan </a>
                                            <span class="message-date">  Fri Jan 25 2015 - 11:12:36 </span>
                                            <span class="message-content">
											All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.
                                                It uses a dictionary of over 200 Latin words.
                                            </span>
                                        </div>
                                    </div>
                                    <div class="chat-message right">
                                        <img class="message-avatar" src="img/a6.jpg" alt="">
                                        <div class="message">
                                            <a class="message-author" href="#"> Mark Smith </a>
                                            <span class="message-date">  Fri Jan 25 2015 - 11:12:36 </span>
                                            <span class="message-content">
											All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.
                                                It uses a dictionary of over 200 Latin words.
                                            </span>
                                        </div>
                                    </div>

                                </div>

                            </div>
                            <div class="col-md-3">
                                <div class="chat-users">


                                    <div class="users-list">
                                        <div class="chat-user">
                                            <img class="chat-avatar" src="img/a4.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Karl Jordan</a>
                                            </div>
                                        </div>
                                        <div class="chat-user">
                                            <img class="chat-avatar" src="img/a1.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Monica Smith</a>
                                            </div>
                                        </div>
                                        <div class="chat-user">
                                            <span class="pull-right label label-primary">Online</span>
                                            <img class="chat-avatar" src="img/a2.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Michael Smith</a>
                                            </div>
                                        </div>
                                        <div class="chat-user">
                                            <span class="pull-right label label-primary">Online</span>
                                            <img class="chat-avatar" src="img/a3.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Janet Smith</a>
                                            </div>
                                        </div>
                                        <div class="chat-user">
                                            <img class="chat-avatar" src="img/a5.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Alice Smith</a>
                                            </div>
                                        </div>
                                        <div class="chat-user">
                                            <img class="chat-avatar" src="img/a6.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Monica Cale</a>
                                            </div>
                                        </div>
                                        <div class="chat-user">
                                            <img class="chat-avatar" src="img/a2.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Mark Jordan</a>
                                            </div>
                                        </div>
                                        <div class="chat-user">
                                            <span class="pull-right label label-primary">Online</span>
                                            <img class="chat-avatar" src="img/a3.jpg" alt="">
                                            <div class="chat-user-name">
                                                <a href="#">Janet Smith</a>
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
    import { WS_ROOT } from '../config.js'
    export default {
        name: 'Chat',
        data: function() {
            return {
                message_list: [],
                message_text: ''
            }
        },
        methods: {
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
                e.preventDefault();
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
                //this.chatsock.send(JSON.stringify(_message));
                // this.chatsock.send(_message);
                // $("#message").val('').focus();

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
