<template>
    <div>
            <div class="row wrapper border-bottom white-bg page-heading">
                <div class="col-lg-9">
                    <h2>Students</h2>
                    <ol class="breadcrumb">
                        <li>
                            <a href="#">Home</a>
                        </li>
                        <li>
                           Clssrooms
                        </li>
                         <li>
                           {{currentClassroom.class_short}}
                        </li>
                        <li class="active">
                            <strong>Classmates</strong>
                        </li>
                    </ol>
                </div>
            </div>
        <div class="wrapper wrapper-content animated fadeInRight">
        <div class="row">
            <div class="col-lg-3 col-sm-3" v-for="student in currentClassroom.students">
                <div class="contact-box center-version">

                    <a :href="profileUrl(student)">
                        <img alt="image" class="img-circle" :src="student.avatar.avatar2x">
                        <h3 class="m-b-xs"><strong>{{student.full_name}}</strong></h3>

                        <div class="font-bold">@{{student.username}}</div>
                        <address class="m-t-md">
                            <strong>About</strong><br>
                          {{student.about_me}}
                        </address>

                    </a>
                    <div class="contact-box-footer">
                            <a class="btn btn-xm btn-primary"><i class="fa fa-user-plus"></i> Send Firend Request</a>
                    </div>

                </div>
            </div>
</div>

        </div>
        </div>
</template>

<script>
    export default {
        name: 'ClassroomStudent',
        methods: {
            profileUrl(student) {
                return '/#/profile/id/' + student.pk
            }
        },
        computed: {
            currentClassroom() {
                return this.$store.getters.currentClassroom
            }
        }
    }

</script>
