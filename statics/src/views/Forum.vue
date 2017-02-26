<template>
   <spinner v-if="!loaded"></spinner>
   <div v-else>
      <div class="row wrapper border-bottom white-bg page-heading">
         <div class="col-sm-4">
            <h2>User Forum</h2>
            <ol class="breadcrumb">
               <li>
         <router-link :to="{name:'home'}">Home</router-link>

               </li>
               <li class="active">
                  <strong>User Forum</strong>
               </li>
            </ol>
         </div>
      </div>
      <div class="row">
         <div class="col-lg-12">
            <div class="wrapper wrapper-content animated fadeInRight">
               <div class="ibox-content m-b-sm border-bottom">
                  <div class="text-center p-lg">
                     <h2>Welcome to User Forum of ClassGotcha <span class="label label-primary">Beta</span></h2>
                     <span>Here you can report bugs, give us suggestions or contribute new ideas</span>
                     <br>
                     <button type="button" data-toggle="modal" data-target="#newpost" class="btn btn-primary btn-sm m-t">
                     <i class="fa fa-plus"></i> <span class="bold">Add Post</span>
                     </button>
                     <div class="modal inmodal" id="newpost" name="newpost" tabindex="-1" role="dialog" aria-hidden="true">
                        <div class="modal-dialog">
                           <div class="modal-content animated fadeInDown">
                              <div class="modal-header">
                                 <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                                 <h4 class="modal-title">New Post</h4>
                                 <small class="font-bold">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</small>
                              </div>
                              <div class="modal-body">
                <div class="form-group">
                  <input v-model="post_title" class="form-control m-b" placeholder="Title">
             
                  <textarea v-model="post_content"  class="form-control m-b" placeholder="Content"></textarea>
                  <!--<input-tag :tags="tags" :on-change="tagManager"></input-tag>-->
                              </div>
                              </div>
                              <div class="modal-footer">
                                 <button type="button" class="btn btn-white" data-dismiss="modal">Close</button>
                                 <button type="button" @click="postNewPost()" class="btn btn-primary">Save changes</button>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
               </div>
               <div class="faq-item" v-for="post in posts">
                  <div class="row">
                     <div class="vote-actions m-l">
                        <a @click="upVote(post.id)">
                        <i class="fa fa-chevron-up"> </i>
                        </a>
                        <div>{{post.vote}}</div>
                        <a @click="downVote(post.id)">
                        <i class="fa fa-chevron-down"> </i>
                        </a>
                     </div>
                     <div class="col-md-7">
                        <router-link :to="{name:'post', params:{post_id:post.id}}" class="faq-question">{{post.title}}</router-link>
                        <small>Added by <strong>{{post.creator.full_name}}</strong> <i class="fa fa-clock-o"></i>{{post.created}}</small>
                     </div>
                     <div class="col-md-3">
                        <span class="small font-bold">Tags</span>
                        <div class="tag-list">
                           <span class="tag-item">General</span>
                           <span class="tag-item">License</span>
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
    import Spinner from 'components/Spinner'
    export default {
        name: 'posts',
        components: {
            'spinner': Spinner
        },
        data() {
            return {
                loaded: false,
                post_title: '',
                post_content: '',
                post_tags: []
            }
        },
        methods: {
            postNewPost() {
                this.$store.dispatch('postPost', {
                    title: this.post_title,
                    content: this.post_content
                })
            },
            upVote(id) {
                const data = {
                    id: id,
                    formData: {
                        vote: 1
                    }
                }
                this.$store.dispatch('addPostVote', data)
            },
            downVote(id) {
                const data = {
                    id: id,
                    formData: {
                        vote: -1
                    }
                }
                this.$store.dispatch('addPostVote', data)
            }
        },
        computed: {
            posts() {
                return this.$store.getters.posts
            }
        },
        created() {
            this.$store.dispatch('getPosts').then(() => {
                this.loaded = true
            })
        }
    }

</script>
