<template>
    <div>
            <div class="row wrapper border-bottom white-bg page-heading">
                <div class="col-lg-9">
                    <h2>Students</h2>
                    <ol class="breadcrumb">
                        <li>
                           <router-link  :to="{name:'home'}">Home</router-link>
                        </li>
                        <li>
                           Classrooms
                        </li>
                         <li>
                           <router-link :to="{name:'classroom', params:{classroom_id:currentClassroom.id}}"> {{currentClassroom.class_short}}</router-link>
                        </li>
                        <li class="active">
                            <strong>Classmates</strong>
                        </li>
                    </ol>
                </div>
            </div>
        <div class="wrapper wrapper-content animated fadeInRight">
        <div class="row">
            <div class="col-lg-3 col-md-6 col-sm-12" v-for="student in currentClassroom.students">
                <div class="contact-box">
                    <router-link :to="{name:'userDetail', params:{user_id:student.id}}">
                    
                    <div class="col-sm-4">
                        <div class="text-center">
                           <img v-if="student.avatar" class="img-circle m-t-xs img-responsive" :src="student.avatar.avatar2x">
                           <avatar v-else class="img-circle m-t-xs img-responsive" :size="86" :username="student.full_name"></avatar>
                           <div class="m-t-xs font-bold hidden-xs">@{{student.username}}</div>
                           
                        </div>
                     </div>
                        </router-link>
                     
                   <div class="col-sm-8 ">
                        <h3><strong>{{student.full_name}}</strong> 
                        
                           <span class="label label-warning">Level {{student.level}}</span>
                        </h3>
                        <address>
                           <strong>Major:</strong> <br>
                           <strong>Class:</strong> {{student.school_year}}<br>
                           <strong>About Me</strong><br>
                           {{student.about_me}}
                        </address>
                        <div class="m-t-xs btn-group">
                            <a @click="addFriend(student.id)" class="btn btn-xs btn-primary"><i class="fa fa-user-plus"></i> + Add Friend</a>
                            <router-link :to="{name:'userDetail', params:{user_id:student.id}}" class="btn btn-xs btn-white"><i class="fa fa-user"></i> Profile </router-link>                            
                        </div>
                        
                     </div>
                     
                    <div class="clearfix"></div>
                </div>
            </div>
</div>

        </div>
        </div>
</template>

<script>
    import Avatar from 'vue-avatar'

    export default {
        name: 'ClassroomStudent',
        components: {
            'avatar': Avatar.Avatar
        },
        methods: {
            addFriend(pk) {
                this.$store.dispatch('addFriend', pk)
            }
        },
        computed: {
            currentClassroom() {
                return this.$store.getters.currentClassroom
            }
        }
    }

</script>
