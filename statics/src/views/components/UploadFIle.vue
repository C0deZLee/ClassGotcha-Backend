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
          <div class="dropzone-preview" v-if="file&&(step2||step3)">
            <!--<img :src="image" />-->
            <p>Uploaded: <strong>{{file.name}} </strong>  <a class="m-l" @click="removeFile">Remove</a></p>
            <div v-if="step2">
              <p>Choose a category: </p>
              <a class="btn btn-primary" @click="chooseCategory('Note')"><i class="fa fa-tag"></i> Note</a>
              <a class="btn btn-white" @click="chooseCategory('Lecture')"><i class="fa fa-tag"></i> Lecture</a>
              <a class="btn btn-white" @click="chooseCategory('Homework')"><i class="fa fa-tag"></i> Homework</a>
              <a class="btn btn-white" @click="chooseCategory('Quiz')"><i class="fa fa-tag"></i> Quiz</a>
              <a class="btn btn-white" @click="chooseCategory('Exam')"><i class="fa fa-tag"></i> Exam</a>
              <a class="btn btn-white" @click="chooseCategory('Lab')"><i class="fa fa-tag"></i> Lab</a>
              <a class="btn btn-white" @click="chooseCategory('Syllabus')"><i class="fa fa-tag"></i> Syllabus</a>
              <a class="btn btn-white" @click="chooseCategory('Other')"><i class="fa fa-tag"></i> Other</a>
            </div>
            <div class="dropzone-preview" v-if="step3">
                <div v-show="choice!=='Note'">
              And this is for:
              <h3><strong>{{choice}}</strong> <input type="number" placeholder="Put a number here" v-model="count"></h3>
              </div>
              <div v-show="choice =='Note'">
              Choose a tag for this note:
              <h3><strong>Chapter</strong> <input type="number" placeholder="Put a number here" v-model="note_count1"></h3>
              <h3><strong>Lecture</strong> <input type="number" placeholder="Put a number here" v-model="note_count2"></h3>
              <h3><input type="checkbox" v-model="note_checked" id="check" name="check" required>
                 <label for="check"></label> 
                 <i class="m-r"></i>Cumulative</h3>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-white" @click="goBack">Back</button>
          <button type="button" class="btn btn-primary" v-show="step3" :disabled="!(count||note_count1||note_count2||note_checked)" >Upload</button>
          
        </div>
      </div>
    </div>
  </div>
</template>
<script>
    export default {
        data() {
            return {
                file: '',
                choice: '',
                count: '',
                note_count1: '',
                note_count2: '',
                note_checked: false,
                step1: true,
                step2: false,
                step3: false,
            }
        },
        methods: {
            onFileChange(e) {
                var files = e.target.files || e.dataTransfer.files
                if (!files.length) return
                console.log(files)
                this.file = files[0]
                this.$store.dispatch('uploadFile', files[0])
                // this.createFile(files[0])
                this.nextStep()
            },
            removeFile(e) {
                this.image = ''
                this.$store.dispatch('clearFile')
                this.step1 = true
                this.step2 = false
                this.step3 = false
            },
            chooseCategory(cate) {
                if (!cate) return
                this.choice = cate
                this.nextStep()
            },
            goBack() {
                if (this.step2) {
                    this.step1 = true
                    this.step2 = false
                } else if (this.step3) {
                    this.step2 = true
                    this.step3 = false
                    this.count = ''
                    this.note_count1 = ''
                    this.note_count2 = ''
                    this.note_checked = false
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
