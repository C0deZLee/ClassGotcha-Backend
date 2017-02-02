<template>
    <div  id="dropzone">
  <div v-show="!image">
      <div class="dropzone-area" drag-over="handleDragOver" @dragenter="hovering = true" @dragleave="hovering = false" :class="{'hovered': hovering}">
          <div class="dropzone-text ">
              <i class="fa fa-cloud-upload"> </i>
              <span>Drop image here or click to select</span>
              <!--<span class="dropzone-info" v-if="help">{{ help }}</span>-->
          </div>
          <input type="file" @change="onFileChange">
      </div>
  </div>
  <div class="dropzone-preview">
      <img :src="image" />
      <button class="form-control btn btn-white" @click="removeImage" v-show="image">Remove</button>
  </div>
  <!--{{ data | json }}-->
  </div>
</template>


<script>
    export default {

        template: '#dropzone',

        data() {
            return {
                image: '',
                hovering: false
            }
        },
        methods: {
            onFileChange(e) {
                // TODO: check if the file is image
                var files = e.target.files || e.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0])
            },
            createImage(file) {
                /* global FileReader:true */
                // var image = new Image()
                var reader = new FileReader()
                var vm = this

                reader.onload = (e) => {
                    vm.image = e.target.result
                    this.$store.dispatch('uploadFile', this.image)
                }
                reader.readAsDataURL(file)

            },
            removeImage(e) {
                this.image = ''
                this.$store.dispatch('clearFile')
            }
        }

    }

</script>

<style>
    /* Dropzone */
    /*.dropzone-area {
        min-height: 100px;
        border: 1px dashed #1ab394;
        background: white;
        padding: 20px 20px;
    }*/
    
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
