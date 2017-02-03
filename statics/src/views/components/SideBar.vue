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
                             </span> <span class="text-muted text-xs block">@{{username}} <b class="caret"></b></span> </span> </a>
                        <ul class="dropdown-menu animated fadeInRight m-t-xs">
                            <li><a href="/#/profile/id/me">Profile</a></li>
                         
                            <li><a href="mailbox.html">Mailbox</a></li>
                            <li class="divider"></li>
                               <li> <a v-on:click="$store.dispatch('logout')"><i class="fa fa-sign-out"></i> Log out</a></li>
                        </ul>
                    </div>
                    <div class="logo-element">
                      <img alt="image" class="img-circle" :src="avatar" />
                    </div>
                </li>
                <li class="active">
                    <a href="/#/">
                        <i class="fa fa-th-large"></i>
                        <span class="nav-label">Index</span>
                    </a>
                </li>

                <li>
                    <a href="/#/classroom"><i class="fa fa-book"></i> <span class="nav-label">Classroom</span><span class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li><a href="/#/classroom/add">+ Add New</a></li>
                        <li v-for="classroom in classrooms">
                            <a :href="classroomUrl(classroom.id)">{{classroom.class_short}}</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="/#/me/">
                        <i class="fa fa-file-text"></i>
                        <span class="nav-label">My Notes</span>
                    </a>
                </li>
                   <li>
                    <a href="/#/me/">
                        <i class="fa fa-users"></i>
                        <span class="nav-label">My Groups</span>
                    </a>
                </li>   
                <li>
                    <a href="/#/profile/id/me/">
                        <i class="fa fa-user"></i>
                        <span class="nav-label">Profile</span>
                    </a>
                </li>
                <li>
                    <a href="/#/settings/">
                        <i class="fa fa-gear"></i>
                        <span class="nav-label">Settings</span>
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
                if (this.$store.getters.userAvatar)
                    return this.$store.getters.userAvatar.avatar1x
            },
            username() {
                if (this.$store.getters.me)
                    return this.$store.getters.me.username
            },
            classrooms() {
                if (this.$store.getters.userClassrooms)
                    return this.$store.getters.userClassrooms
            }
        }
    }

</script>
