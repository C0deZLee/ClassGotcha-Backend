<template>
  <div class="modal inmodal fade" id="upload" tabindex="-1" role="dialog"  aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
          <h3 class="modal-title">Upload Your File</h3>
        </div>
        <div class="modal-body">
          <div v-if="step1">
            <div class="dropzone-area">
              <div class="dropzone-text ">
                <i class="fa fa-cloud-upload"> </i>
                <span>Drop file here or click to select</span>
              </div>
              <input type="file" @change="onFileChange">
            </div>
          </div>
          <div class="dropzone-preview" v-show="file&&(step2||step3)">
            <!--<img :src="image" />-->
            <p>Uploaded: <strong>{{file.name}} </strong>  <a class="m-l" @click="removeFile">Remove</a></p>
            <div v-if="step2">
              <p>Choose a category for your file </p>
              <a class="btn btn-primary" @click="chooseCategory('Note')"><i class="fa fa-tag"></i> Note</a>
              <a class="btn btn-white" @click="chooseCategory('Lecture')"><i class="fa fa-tag"></i> Lecture</a>
              <a class="btn btn-white" @click="chooseCategory('Homework')"><i class="fa fa-tag"></i> Homework</a>
              <a class="btn btn-white" @click="chooseCategory('Quiz')"><i class="fa fa-tag"></i> Quiz</a>
              <a class="btn btn-white" @click="chooseCategory('Exam')"><i class="fa fa-tag"></i> Exam</a>
              <a class="btn btn-white" @click="chooseCategory('Lab')"><i class="fa fa-tag"></i> Lab</a>
              <a class="btn btn-white" @click="chooseCategory('Syllabus')"><i class="fa fa-tag"></i> Syllabus</a>
              <a class="btn btn-white" @click="chooseCategory('Other')"><i class="fa fa-tag"></i> Other</a>
            </div>
            <div v-show="step3">
              <p class="m-t">Tell your classmates more about your <strong>{{choice[0]}}</strong>!</p>
                <div class="form-group">
                  <input v-model="file_title" type="text" class="form-control m-b" :placeholder="file.name">
             
                  <textarea v-model="file_dscr" type="text" class="form-control m-b" placeholder="Describe it in detail (optional)"></textarea>
                  <input-tag :tags="tags" :on-change="tagManager"></input-tag>
              </div>
            </div>
          </div>
          <div v-show="step4">
            
            <h1 class="text-navy text-center"><i class="fa fa-check-circle-o"></i>
            Upload Successful!</h1>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-white" @click="goBack" v-show="!step1&&!step4">Back</button>
          <button type="button" class="btn btn-primary" v-show="step3" @click="uploadFile()" :disabled="!(step3)" >Upload</button>
          <button type="button" class="btn btn-white" v-show="step4" @click="step1=true;step4=false" data-dismiss="modal">Close</button>
          
        </div>
      </div>
    </div>
  </div>
</template>
<script>
    import InputTag from 'vue-input-tag'
    export default {
        components: { 'input-tag': InputTag },
        data() {
            return {
                // file
                file: '',
                file_title: '',
                file_dscr: '',
                choice: '',
                tags: [],
                // step
                step1: true,
                step2: false,
                step3: false,
                step4: false
            }
        },
        methods: {
            onFileChange(e) {
                var files = e.target.files || e.dataTransfer.files
                if (!files.length) return
                console.log(files)
                this.file = files[0]
                this.$store.dispatch('uploadFile', files[0])
                this.file_title = this.file.name.split('.')[0]
                this.nextStep()
            },
            removeFile(e) {
                this.$store.dispatch('clearFile')
                this.step1 = true
                this.step2 = false
                this.step3 = false
            },
            uploadFile() {
                if (this.step3 && this.file && this.file_title) {
                    /* global FormData:true */
                    let formData = new FormData()
                    formData.append('file', this.file)
                    formData.append('description', this.file_dscr)
                    formData.append('title', this.file_title)
                    formData.append('tags', JSON.stringify(this.tags))

                    const data = {
                        pk: this.$route.params.classroom_id,
                        formData: formData
                    }
                    console.log('UploadFile.uploadFile', data)
                    this.$store.dispatch('postClassroomNote', data)
                        .then(() => {
                            this.step1 = false
                            this.step2 = false
                            this.step3 = false
                            this.step4 = true
                            this.file = ''
                            this.file_title = ''
                            this.file_dscr = ''
                            this.choice = ''
                            this.tags = []
                            this.$store.dispatch('clearFile')

                        })
                }
            },
            chooseCategory(category) {
                if (!category) return
                this.choice = category
                this.tags.push(category)
                this.nextStep()
            },
            tagManager() {
                if (this.tags.length === 0)
                    this.tags.push(this.choice)
            },
            goBack() {
                if (this.step2) {
                    this.step1 = true
                    this.step2 = false
                } else if (this.step3) {
                    this.step2 = true
                    this.step3 = false
                }
            },
            nextStep() {
                if (this.step1) {
                    this.step2 = true
                    this.step1 = false
                } else if (this.step2) {
                    this.step3 = true
                    this.step2 = false
                }
            }
        },
        computed: {
            current_classroom() {
                return this.$store.getters.currentClassroom
            },
            current_classroom_id() {
                return this.$route.params.classroom_id
            }
        }
    }

</script>
<style scoped>
    .dropzone-area {
        width: 100%;
        height: 200px;
        position: relative;
        border: 2px dashed #CBCBCB;
    }
    
    .dropzone-area.hovered {
        border: 2px dashed #1ab394;
    }
    
    .dropzone-area.hovered .dropzone-title {
        color: #1ab394;
    }
    
    .dropzone-area input {
        position: absolute;
        cursor: pointer;
        top: 0px;
        right: 0;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0;
    }
    
    .dropzone-text {
        position: absolute;
        top: 50%;
        text-align: center;
        transform: translate(0, -50%);
        width: 100%;
    }
    
    .dropzone-text span {
        display: block;
        font-family: Arial, Helvetica;
        line-height: 1.9;
    }
    
    .dropzone-title {
        font-size: 13px;
        color: #787878;
        letter-spacing: 0.4px;
    }
    
    .dropzone-info {
        font-size: 13px;
        font-size: 0.8125rem;
        color: #A8A8A8;
        letter-spacing: 0.4px;
    }
    
    .dropzone-button {
        position: absolute;
        top: 10px;
        right: 10px;
        display: none;
    }
    
    .dropzone-preview {
        width: 100%;
        position: relative;
    }
    
    .dropzone-preview:hover .dropzone-button {
        display: block;
    }
    
    .dropzone-preview img {
        display: block;
        height: auto;
        max-width: 100%;
    }

</style>
