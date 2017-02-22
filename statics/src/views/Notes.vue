<template>
   <div>
      <div class="row wrapper border-bottom white-bg page-heading">
         <div class="col-lg-9">
            <h2>Notes</h2>
            <ol class="breadcrumb">
               <li>
                           <router-link  :to="{name:'home'}">Home</router-link>

               </li>
               <li>
                  <router-link :to="{name:'classroom', params:{classroom_id:current_classroom.id}}">{{current_classroom.class_short}}</router-link>
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
                              <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}}"> 
                                 <i class="fa fa-align-justify"></i> All Files
                              </router-link>
                           </li>
                           <li v-show="showFolder('Note')">
                              <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Note'}}"> 
                                 <i class="fa fa-certificate"></i> Notes <span class="label label-warning pull-right">16</span> 
                              </router-link>
                           </li>
                           <li v-show="showFolder('Lecture')">
                              <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Lecture'}}"> 
                                 <i class="fa fa-inbox"></i> Lectures
                              </router-link>
                           </li>
                           <li v-show="showFolder('Lab')">
                              <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Lab'}}"> 
                                 <i class="fa fa-flask"></i> Labs
                              </router-link>
                           </li>
                           <li v-show="showFolder('Homework')">
                              <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Homework'}}"> 
                                 <i class="fa fa-file-text-o"></i> Homeworks <span class="label label-danger pull-right">2</span>
                              </router-link>
                           </li>
                           <li v-show="showFolder('Exam')">
                              <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{folder:'Exam'}}"> 
                                 <i class="fa fa-bolt"></i> Exams
                              </router-link>
                           </li>
                        </ul>
                        <div class="hr-line-dashed"></div>
                        <h5 class="tag-title">Tags</h5>
                        <ul class="tag-list" style="padding: 0">
                           <li v-for="tag in tags">
                              <router-link :to="{name:'classroomNotes', params:{classroom_id: current_classroom.id}, query:{tag:tag}}">{{tag}}</router-link>
                           </li>
                        </ul>
                        <div class="clearfix"></div>
                     </div>
                  </div>
               </div>
            </div>
            <div class="col-lg-9 animated fadeInRight">
               <div class="row">
                  <div class="col-lg-12">
                     <div class="file-box" v-for="file in files">
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
                              <small>Added: {{formatTime(file.created)}}</small>
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
        data() {
            return {
                files: [],
            }
        },
        components: {
            upload: Upload
        },
        methods: {
            loadData() {
                // load current classroom's notes
                this.$store.dispatch('getClassroomNotes', this.$route.params.classroom_id).then(() => {
                    this.files = []
                    // filter by folder
                    if (this.$route.query.folder) {
                        // for every tag in every notes
                        for (let i in this.$store.getters.currentClassroomNotes) {
                            for (let j in this.$store.getters.currentClassroomNotes[i].tags) {
                                // if tag match current query's folder, add it to files
                                if (this.$store.getters.currentClassroomNotes[i].tags[j].name === this.$route.query.folder) {
                                    this.files.push(this.$store.getters.currentClassroomNotes[i])
                                }
                            }
                        }
                    }
                    // filter by tag
                    else if (this.$route.query.tag) {
                        // for every tag in every notes
                        for (let i in this.$store.getters.currentClassroomNotes) {
                            for (let j in this.$store.getters.currentClassroomNotes[i].tags) {
                                // if tag match current query's folder, add it to files
                                if (this.$store.getters.currentClassroomNotes[i].tags[j].name === this.$route.query.tag) {
                                    this.files.push(this.$store.getters.currentClassroomNotes[i])
                                }
                            }
                        }
                    }
                    // if no folder then get all files                    
                    else {
                        this.files = this.$store.getters.currentClassroomNotes
                    }
                })
                // if classroom not loaded or id doesn't match
                if (!this.$store.getters.currentClassroom.id || this.$route.params.classroom_id !== this.$store.getters.currentClassroom.id)
                    // load current classroom
                    this.$store.dispatch('getClassroom', this.$route.params.classroom_id)
            },
            showFolder(name) {
                for (let i in this.current_classroom.folders) {
                    if (this.current_classroom.folders[i].name === name)
                        return true
                }
                return false
            },
            formatTime(time) {
                /* global moment:true */
                return moment.utc(time).format('ll')
            },
        },
        computed: {
            current_classroom() {
                return this.$store.getters.currentClassroom
            },
            tags() {
                let tags = []
                // for every tag in every notes
                for (let i in this.$store.getters.currentClassroomNotes) {
                    for (let j in this.$store.getters.currentClassroomNotes[i].tags) {
                        // check if current tag is a folder
                        let is_folder = false
                        // for current classroom folders
                        for (let k in this.current_classroom.folders) {
                            // if current tag is in classroom folders
                            if ((this.current_classroom.folders[k].name === this.$store.getters.currentClassroomNotes[i].tags[j].name)) {
                                // is not a tag
                                is_folder = true
                            }
                        }
                        // if current tag is not folder
                        if (!is_folder) {
                            // if tag list not duplicate
                            if (!tags.includes(this.$store.getters.currentClassroomNotes[i].tags[j].name))
                                // push tag in
                                tags.push(this.$store.getters.currentClassroomNotes[i].tags[j].name)
                        }

                    }
                }
                return tags
            }
        },
        created() {
            this.loadData()
        },
        watch: {
            '$route': 'loadData'
        }
    }

</script>
