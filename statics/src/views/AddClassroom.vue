<template>
    <div>
    <div class="row wrapper border-bottom white-bg page-heading">
                <div class="col-lg-10">
                    <h2>Add New</h2>
                    <ol class="breadcrumb">
                        <li>
                            <a href="index.html">Home</a>
                        </li>
                        <li>
                            <a>Classroom</a>
                        </li>
                        <li class="active">
                            <strong>Add New</strong>
                        </li>
                    </ol>
                </div>
                <div class="col-lg-2">

                </div>
            </div>
        <div class="wrapper wrapper-content  animated fadeInRight">
            <div class="row">
                <div class="col-sm-8">
                    <div class="ibox">
                        <div class="ibox-content">
                            
                            <h2>Search Your Class Here</h2>
                            <p>
                                All clients need to be verified before you can send email and set a project.
                            </p>
                            <div class="input-group">
                                <input type="text" placeholder="ex: 123456 or Math 141 or cmpsc121" @keydown.enter="classroomSearch($event)" v-model="search_token" class="input form-control">
                                <span class="input-group-btn">
                                        <button type="button" @click="classroomSearch($event)" class="btn btn btn-primary"> <i class="fa fa-search"></i> Search</button>
                                </span>
                            
                            </div>
                            <div class="clients-list">
                            
                            <ul class="nav nav-tabs">
                                  <div class="full-height-scroll">
                                        <div class="table-responsive">
                                            <table class="table table-striped table-hover">
                                                <tbody>
                                                    <tr v-if="resultLength===0">
                                                       <td class="text-center">No result</td>
                                                    </tr>
                                                    <tr v-for="classroom in searchResult">
                                                    <td><a data-toggle="tab" v-on:click="select_classroom(classroom)" class="client-link">{{classroom.class_code}}</a></td>
                                                    <td>{{classroom.class_short}}</td>
                                                    <td> Sec {{classroom.class_section}}</td>
                                                    
                                                    <td><i class="fa fa-group"></i> {{classroom.students_count}}</td>
                                                    <td class="client-status"><span class="label label-primary">Active</span></td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                            </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4">
                    <div class="ibox" v-show="selected_classroom">

                        <div class="ibox-content">
                            <div class="tab-content">
                                <div class="tab-pane active">
                                    <div  class="row m-b-lg">
                                        <div class="col-lg-4 text-center">
                                            <h2>{{selected_classroom.class_short}}</h2>
                                            <h5>Section {{selected_classroom.class_section}}</h5>
                                        </div>
                                        <div class="col-lg-8">
                                            <strong>
                                               Description
                                            </strong>

                                            <p>
                                               {{selected_classroom.description}}
                                            </p>
                                            <a v-on:click="classroomURL(selected_classroom)" class="btn btn-primary btn-sm btn-block"><i
                                                    class="fa fa-envelope"></i> Enter Classroom
                                            </a>
                                        </div>
                                    </div>
                                    <div class="client-detail">

                                    
                                        <strong>Last activity</strong>

                                        <ul class="list-group clear-list">
                                            <li class="list-group-item fist-item">
                                                <span class="pull-right"> 09:00 pm </span>
                                                Please contact me
                                            </li>
                                            <li class="list-group-item">
                                                <span class="pull-right"> 10:16 am </span>
                                                Sign a contract
                                            </li>
                                            <li class="list-group-item">
                                                <span class="pull-right"> 08:22 pm </span>
                                                Open new shop
                                            </li>
                                            <li class="list-group-item">
                                                <span class="pull-right"> 11:06 pm </span>
                                                Call back to Sylvia
                                            </li>
                                            <li class="list-group-item">
                                                <span class="pull-right"> 12:00 am </span>
                                                Write a letter to Sandra
                                            </li>
                                        </ul>
                                        <strong>Notes</strong>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                                            tempor incididunt ut labore et dolore magna aliqua.
                                        </p>
                                        <hr/>
                                        <strong>Timeline activity</strong>
                                        <div id="vertical-timeline" class="vertical-container dark-timeline">
                                            <div class="vertical-timeline-block">
                                                <div class="vertical-timeline-icon gray-bg">
                                                    <i class="fa fa-coffee"></i>
                                                </div>
                                                <div class="vertical-timeline-content">
                                                    <p>Conference on the sales results for the previous year.</p>
                                                    <span class="vertical-date small text-muted"> 2:10 pm - 12.06.2014 </span>
                                                </div>
                                            </div>
                                            <div class="vertical-timeline-block">
                                                <div class="vertical-timeline-icon gray-bg">
                                                    <i class="fa fa-briefcase"></i>
                                                </div>
                                                <div class="vertical-timeline-content">
                                                    <p>Many desktop publishing packages and web page editors now use Lorem.
                                                    </p>
                                                    <span class="vertical-date small text-muted"> 4:20 pm - 10.05.2014 </span>
                                                </div>
                                            </div>
                                            <div class="vertical-timeline-block">
                                                <div class="vertical-timeline-icon gray-bg">
                                                    <i class="fa fa-bolt"></i>
                                                </div>
                                                <div class="vertical-timeline-content">
                                                    <p>There are many variations of passages of Lorem Ipsum available.
                                                    </p>
                                                    <span class="vertical-date small text-muted"> 06:10 pm - 11.03.2014 </span>
                                                </div>
                                            </div>
                                            <div class="vertical-timeline-block">
                                                <div class="vertical-timeline-icon navy-bg">
                                                    <i class="fa fa-warning"></i>
                                                </div>
                                                <div class="vertical-timeline-content">
                                                    <p>The generated Lorem Ipsum is therefore.
                                                    </p>
                                                    <span class="vertical-date small text-muted"> 02:50 pm - 03.10.2014 </span>
                                                </div>
                                            </div>
                                            <div class="vertical-timeline-block">
                                                <div class="vertical-timeline-icon gray-bg">
                                                    <i class="fa fa-coffee"></i>
                                                </div>
                                                <div class="vertical-timeline-content">
                                                    <p>Conference on the sales results for the previous year.
                                                    </p>
                                                    <span class="vertical-date small text-muted"> 2:10 pm - 12.06.2014 </span>
                                                </div>
                                            </div>
                                            <div class="vertical-timeline-block">
                                                <div class="vertical-timeline-icon gray-bg">
                                                    <i class="fa fa-briefcase"></i>
                                                </div>
                                                <div class="vertical-timeline-content">
                                                    <p>Many desktop publishing packages and web page editors now use Lorem.
                                                    </p>
                                                    <span class="vertical-date small text-muted"> 4:20 pm - 10.05.2014 </span>
                                                </div>
                                            </div>
                                        </div>
                                    
                                    </div>

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
        name: 'AddClassroom',
        data: function() {
            return {
                search_token: '',
                selected_classroom: ''
            }
        },
        methods: {
            classroomSearch(e) {
                e.preventDefault()
                const formData = { search: this.search_token }
                this.$store.dispatch('classroomSearch', formData)
            },
            select_classroom(classroom) {
                this.selected_classroom = classroom
            },
            classroomURL(classroom) {
                const url = '/classroom/id/' + classroom.id
                this.$router.push(url)
            }

        },
        computed: {
            searchResult() {
                return this.$store.getters.classSearchResults
            },
            resultLength() {
                return this.$store.getters.classSearchResults.length
            }
        }
    }

</script>
