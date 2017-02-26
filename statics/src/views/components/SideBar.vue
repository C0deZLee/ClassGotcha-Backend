<template>
    <nav class="navbar-default navbar-static-side" role="navigation">
        <div class="sidebar-collapse">
            <ul side-navigation class="nav metismenu" id="side-menu">
                <li class="nav-header">
                    <div class="dropdown profile-element"> <span>
                    <img v-if="avatar" alt="image" class="img-circle" :src="avatar" />
                    <avatar v-else class="img-circle" :size="42" :username="fullName"></avatar>
                             </span>
                        <a data-toggle="dropdown" class="dropdown-toggle">
                            <span class="clear"> <span class="block m-t-xs"> <strong class="font-bold">{{fullName}}</strong>
                             </span> <span class="text-muted text-xs block">@{{username}} <b class="caret"></b></span> </span> </a>
                        <ul class="dropdown-menu animated fadeInRight m-t-xs">
                            <li><a href="/#/profile/me">Profile</a></li>
                        
                            <li class="divider"></li>
                               <li> <a v-on:click="$store.dispatch('logout')"><i class="fa fa-sign-out"></i> Log out</a></li>
                        </ul>
                    </div>
                    <div class="logo-element">
                    <img v-if="avatar" class="img-circle" :src="avatar"/>
                    <avatar v-else class="m-l" :size="42" :username="fullName"></avatar>
                    </div>
                </li>
                <li>
                    <router-link :to="{name: 'home'}">
                        <i class="fa fa-th-large"></i>
                        <span class="nav-label">Home</span>
                    </router-link>
                </li>

                <li>
                    <a><i class="fa fa-book"></i> <span class="nav-label">Classroom</span><span class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li><router-link :to="{name:'addClassroom'}">+ Add New</router-link></li>
                        <li v-for="classroom in classrooms">
                            <router-link :to="{name: 'classroom', params:{classroom_id:classroom.id}}">{{classroom.class_short}}</router-link>
                        </li>
                    </ul>
                </li>
                <!--<li>
                    <router-link :to="{name: 'myNotes'}">
                        <i class="fa fa-file-text"></i>
                        <span class="nav-label">My Notes</span>
                    </router-link>
                </li>-->
                   <li>
                    <router-link :to="{name:'myGroups'}">
                        <i class="fa fa-users"></i>
                        <span class="nav-label">My Groups</span>
                    </router-link>
                </li>   
                <li>
                    <router-link :to="{name:'profile'}">
                        <i class="fa fa-user"></i>
                        <span class="nav-label">Profile</span>
                    </router-link>
                </li>
                <li>
                    <router-link :to="{name:'forum'}">
                        <i class="fa fa-question-circle"></i>
                        <span class="nav-label">User Forum</span>
                    </router-link>
                </li>
            </ul>   
        </div>
    </nav>
</template>

<script>
    import Avatar from 'vue-avatar'
    import { mapGetters } from 'vuex'

    export default {
        name: 'sidebar',
        components: {
            'avatar': Avatar.Avatar
        },
        methods: {
            classroomUrl(id) {
                return '/#/classroom/id/' + id
            }
        },
        computed: mapGetters({
            fullName: "userFullName",
            avatar: "userAvatar1x",
            username: "username",
            classrooms: "userClassrooms"
        })
    }

</script>
