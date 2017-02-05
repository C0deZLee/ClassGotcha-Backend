<template>
    <div>
    <div class="row wrapper border-bottom white-bg page-heading">
                <div class="col-lg-9">
                    <h2>Notes</h2>
                    <ol class="breadcrumb">
                        <li>
                            <a href="#">Home</a>
                        </li>
                        <li>
                           <a :href="'/#/classroom/id/' + current_classroom.id">{{current_classroom.class_short}}</a>
                        </li>
                        <li class="active">
                            <strong>Notes</strong>
                        </li>
                    </ol>
                </div>
            </div>
            <div class="wrapper wrapper-content">
            <div class="row">
                <div class="col-lg-3">
                    <div class="ibox float-e-margins">
                        <div class="ibox-content">
                            <div class="file-manager">
                                
                                <button class="btn btn-primary btn-block" data-toggle="modal" data-target="#upload">Upload Files</button>
                                <upload id="upload"></upload>
                                  <div class="hr-line-dashed"></div>
                                
                                <h5>Folders</h5>
                                <ul class="folder-list" style="padding: 0">
                                             <li>
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}}"> 
                  <i class="fa fa-align-justify"></i> All Files
                </router-link>
              </li>
                <li v-show="showFolder('Note')">
                <router-link:to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Notes'}}"> 
                  <i class="fa fa-certificate"></i> Notes <span class="label label-warning pull-right">16</span> 
                </router-link>
              </li>
              <li v-show="showFolder('Lecture')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Lectures'}}"> 
                  <i class="fa fa-inbox"></i> Lectures
                </router-link>
              </li>
              <li v-show="showFolder('Lab')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Labs'}}"> 
                  <i class="fa fa-flask"></i> Labs
                </router-link>
              </li>
              <li v-show="showFolder('Homework')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Homeworks'}}"> 
                  <i class="fa fa-file-text-o"></i> Homeworks <span class="label label-danger pull-right">2</span>
                </router-link>
              </li>
              <li v-show="showFolder('Exam')">
                <router-link :to="{name:'classroom_files', params:{classroom_id: current_classroom.id}, query:{folder:'Exams'}}"> 
                  <i class="fa fa-bolt"></i> Exams
                </router-link>
              </li>  </ul>
                              
                                <div class="hr-line-dashed"></div>
                                <h5 class="tag-title">Tags</h5>
                                <ul class="tag-list" style="padding: 0">
                                    <li><a href="">Family</a></li>
                                    <li><a href="">Work</a></li>
                                    <li><a href="">Home</a></li>
                                    <li><a href="">Children</a></li>
                                    <li><a href="">Holidays</a></li>
                                    <li><a href="">Music</a></li>
                                    <li><a href="">Photography</a></li>
                                    <li><a href="">Film</a></li>
                                </ul>
                                <div class="clearfix"></div>
                                
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-9 animated fadeInRight">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="file-box" v-for="file in current_classroom_notes">
                                <div class="file">
                                    <a :href="file.file">
                                        <span class="corner"></span>

                                        <div class="icon">
                                            <i class="fa fa-file-pdf-o"></i>
                                        </div>
                                    </a>
                                     <div class="file-name">
                                           <a href="#"> {{file.title}}</a>
                                            <br>
                                          <small><a>{{file.creator.full_name}}</a></small>
                                            <br>
                                            <small>Added:{{file.created}}</small>
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
    import Upload from 'components/UploadFile'
    export default {
        name: 'Notes',
        components: {
            upload: Upload
        },
        methods: {
            showFolder(name) {
                for (let i in this.current_classroom.folders) {
                    if (this.current_classroom.folders[i].name === name)
                        return true
                }
                return false
            },
        },
        computed: {
            current_classroom() {
                return this.$store.getters.currentClassroom
            },
            current_classroom_notes() {
                return this.$store.getters.currentClassroomNotes
            }
        },
        created() {
            console.log('Notes created')
            // load current classroom's notes
            this.$store.dispatch('getClassroomNotes', this.$route.params.classroom_id)
            // if classroom not loaded or id doesn't match
            if (!this.$store.getters.currentClassroom.id || this.$route.params.classroom_id !== this.$store.getters.currentClassroom.id)
                // load current classroom
                this.$store.dispatch('getClassroom', this.$route.params.classroom_id)
        }
    }

</script>
