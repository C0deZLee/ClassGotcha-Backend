<template>
    <nav class="navbar-default navbar-static-side" role="navigation">
        <div class="sidebar-collapse">
            <ul side-navigation class="nav metismenu" id="side-menu">
                <li class="nav-header">
                    <div class="dropdown profile-element"> <span>
                             <img alt="image" class="img-circle" :src="avatar" />
                             </span>
                        <a data-toggle="dropdown" class="dropdown-toggle">
                            <span class="clear"> <span class="block m-t-xs"> <strong class="font-bold">{{fullName}}</strong>
                             </span> <span class="text-muted text-xs block">Art Director <b class="caret"></b></span> </span> </a>
                        <ul class="dropdown-menu animated fadeInRight m-t-xs">
                            <li><a href="profile.html">Profile</a></li>
                            <li><a href="contacts.html">Contacts</a></li>
                            <li><a href="mailbox.html">Mailbox</a></li>
                            <li class="divider"></li>
                            <li><a href="login.html">Logout</a></li>
                        </ul>
                    </div>
                    <div class="logo-element">
                        CG
                    </div>
                </li>
                <li class="active">
                    <a href="/#/">
                        <i class="fa fa-th-large"></i>
                        <span class="nav-label">Index</span>
                    </a>
                </li>

                <li>
                    <a href="/#/classroom"><i class="fa fa-laptop"></i> <span class="nav-label">Classroom</span><span class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li><a href="/#/classroom/add">+ Add New</a></li>
                        <li v-for="classroom in classrooms">
                            <a :href="classroomUrl(classroom.id)">{{classroom.class_short}}</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="/#/chatroom/id/1">
                        <i class="fa fa-laptop"></i>
                        <span class="nav-label">Chat</span>
                    </a>
                </li>
                <li>
                    <a href="/#/upload/">
                        <i class="fa fa-laptop"></i>
                        <span class="nav-label">Upload</span>
                    </a>
                </li>
            </ul>   
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'sidebar',
        methods: {
            classroomUrl(id) {
                return '/#/classroom/id/' + id
            }
        },
        computed: {
            fullName() {
                return this.$store.getters.userFullName
            },
            avatar() {
                return this.$store.getters.userAvatar.avatar1x
            },
            classrooms() {
                return this.$store.getters.userClassrooms
            }
        }
    }

</script>
