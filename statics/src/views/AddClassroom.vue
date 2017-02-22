<template>
   <div>
      <div class="row wrapper border-bottom white-bg page-heading">
         <div class="col-lg-10">
            <h2>Add New</h2>
            <ol class="breadcrumb">
               <li>
                <router-link :to="{name:'home'}">Home</router-link>
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
                     <p>Just simply type class name 'MATH 140' or class code '23365'</p>
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
                                    <thead>
                                       <tr v-if="resultLength!==0">
                                          <th>Class code</th>
                                          <th>Class name</th>
                                          <th>Class section</th>
                                          <th>Classmates</th>
                                          <th></th>
                                       </tr>
                                    </thead>
                                    <tbody>
                                       <tr v-if="resultLength===0">
                                          <td class="text-center">No result</td>
                                       </tr>
                                       <tr v-for="classroom in searchResult">
                                          <td><a data-toggle="tab" v-on:click="select_classroom(classroom)" class="client-link">{{classroom.class_code}}</a></td>
                                          <td>{{classroom.class_short}}</td>
                                          <td> Sec {{classroom.class_section}}</td>
                                          <td><i class="fa fa-group"></i> {{classroom.students_count}}</td>
                                          <td class="client-status"><span class="label label-primary"><a data-toggle="tab" v-on:click="select_classroom(classroom)" class="client-link">Show Detail</a></span></td>
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
               <div class="ibox" v-show="selected_classroom.id !== 0">
                  <div class="ibox-content">
                     <div class="tab-content">
                        <div class="tab-pane active">
                           <div  class="row m-b-lg">
                              <div class="col-lg-4 text-center">
                                 <h2>{{selected_classroom.class_short}}</h2>
                                 <h5>Section {{selected_classroom.class_section}}</h5>
                              </div>
                              <div class="col-lg-8">
                                 <strong>Description</strong>
                                 <p>{{selected_classroom.description}}</p>
                                 <a v-on:click="classroomURL(selected_classroom)" class="btn btn-primary btn-sm btn-block">
                                 <i class="fa fa-chevron-up"></i> Enter Classroom
                                 </a>
                              </div>
                           </div>
                           <div class="client-detail">
                              <strong>Detail</strong>
                              <ul class="list-group clear-list">
                                 <li class="list-group-item fist-item" v-for="prof in selected_classroom.professors">
                                    Professor
                                    <router-link :to="{name:'professor', params:{professor_id: prof.id}}"><strong class="pull-right">{{prof.full_name}}</strong></router-link>
                                 </li>
                                 <li class="list-group-item">
                                    Class Time                                            
                                    <strong class="pull-right">{{formatClassTime}}</strong>
                                 </li>
                                 <li class="list-group-item">
                                    Location                                           
                                    <strong class="pull-right">{{classLocation}}</strong>
                                 </li>
                              </ul>
                              <strong>Latest Activities</strong>
                              <strong>Class Files</strong>
                              <ul class="folder-list m-t" style="padding: 0">
                                 <li>
                                    <router-link :to="{name:'classroomNotes', params:{classroom_id: selected_classroom.id}}"> 
                                       <i class="fa fa-align-justify"></i> All Files
                                    </router-link>
                                 </li>
                                 <li v-show="showFolder('Note')">
                                    <router-link :to="{name:'classroomNotes', params:{classroom_id: selected_classroom.id}, query:{folder:'Note'}}"> 
                                       <i class="fa fa-certificate"></i> Notes <span class="label label-warning pull-right">16</span> 
                                    </router-link>
                                 </li>
                                 <li v-show="showFolder('Lecture')">
                                    <router-link :to="{name:'classroomNotes', params:{classroom_id: selected_classroom.id}, query:{folder:'Lecture'}}"> 
                                       <i class="fa fa-inbox"></i> Lectures
                                    </router-link>
                                 </li>
                                 <li v-show="showFolder('Lab')">
                                    <router-link :to="{name:'classroomNotes', params:{classroom_id: selected_classroom.id}, query:{folder:'Lab'}}"> 
                                       <i class="fa fa-flask"></i> Labs
                                    </router-link>
                                 </li>
                                 <li v-show="showFolder('Homework')">
                                    <router-link :to="{name:'classroomNotes', params:{classroom_id: selected_classroom.id}, query:{folder:'Homework'}}"> 
                                       <i class="fa fa-file-text-o"></i> Homeworks <span class="label label-danger pull-right">2</span>
                                    </router-link>
                                 </li>
                                 <li v-show="showFolder('Exam')">
                                    <router-link :to="{name:'classroomNotes', params:{classroom_id: selected_classroom.id}, query:{folder:'Exam'}}"> 
                                       <i class="fa fa-bolt"></i> Exams
                                    </router-link>
                                 </li>
                              </ul>
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
                selected_classroom: {
                    id: 0,
                    class_time: { location: 0 }
                }
            }
        },
        methods: {
            classroomSearch(e) {
                e.preventDefault()
                this.$store.dispatch('classroomSearch', { search: this.search_token })
                    .then(() => {
                        this.selected_classroom = this.searchResult[0]
                    })
            },
            select_classroom(classroom) {
                this.selected_classroom = classroom
            },
            classroomURL(classroom) {
                const url = '/classroom/id/' + classroom.id
                this.$router.push(url)
            },
            showFolder(name) {
                for (let i in this.selected_classroom.folders) {
                    if (this.selected_classroom.folders[i].name === name)
                        return true
                }
                return false
            },
        },
        computed: {
            searchResult() {
                return this.$store.getters.classSearchResults
            },
            resultLength() {
                return this.$store.getters.classSearchResults.length
            },
            formatClassTime() {
                if (this.selected_classroom) {
                    if (this.selected_classroom.class_time.repeat) {
                        /* global moment:true */
                        return this.selected_classroom.class_time.repeat + ' ' +
                            moment(this.selected_classroom.class_time.formatted_start_time, 'HH:mm:ss').format('LT') +
                            '-' +
                            moment(this.selected_classroom.class_time.formatted_end_time, 'HH:mm:ss').format('LT')
                    } else return 'WEB'
                } else return ''
            },
            classLocation() {
                if (this.selected_classroom) {
                    return this.selected_classroom.class_time.location
                } else return ''
            }
        }
    }

</script>
