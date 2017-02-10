<template>
    <div>
    <div class="row wrapper border-bottom white-bg page-heading">
                <div class="col-lg-10">
                    <h2>{{currentPost.title}}</h2>
                    <ol class="breadcrumb">
                        <li>
                            <a href="#">Home</a>
                        </li>
                        <li>
                            <router-link :to="{name:'forum'}">Forum</router-link>
                        </li>
                        <li class="active">
                            <strong>Posts</strong>
                        </li>
                    </ol>
                </div>
                <div class="col-lg-2">

                </div>
            </div>
            <div class="wrapper wrapper-content  animated fadeInRight article">
            <div class="row">
                <div class="col-lg-10 col-lg-offset-1">
                    <div class="ibox">
                        <div class="ibox-content">
                            <div class="pull-right">
                                <span class="text-muted"><i class="fa fa-clock-o"></i> {{currentPost.created}}</span>
                            </div>
                            <div class="text-center article-title">
                                
                                <h1>
                                  {{currentPost.title}}
                                </h1>
                                <span class="text-muted">Posted by: {{currentPost.creator.full_name}}</span>
                                
                            </div>
                           {{currentPost.content}}
                            <hr>
                            <div class="row">
                                <div class="col-md-6">
                                        <h5>Tags:</h5>
                                        <button class="btn btn-primary btn-xs" type="button">Model</button>
                                        <button class="btn btn-white btn-xs" type="button">Publishing</button>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-lg-12">

                                    <h2>Comments:</h2>
                                    <div class="social-feed-box">
                                        <div class="social-avatar">
                                            <a href="" class="pull-left">
                                                <img alt="image" src="img/a1.jpg">
                                            </a>
                                            <div class="media-body">
                                                <a href="#">
                                                    Andrew Williams
                                                </a>
                                                <small class="text-muted">Today 4:21 pm - 12.06.2014</small>
                                            </div>
                                        </div>
                                        <div class="social-body">
                                            <p>
                                                Many desktop publishing packages and web page editors now use Lorem Ipsum as their
                                                default model text, and a search for 'lorem ipsum' will uncover many web sites still
                                                default model text.
                                            </p>
                                        </div>
                                    </div>
                                    <div class="social-feed-box">
                                        <div class="social-avatar">
                                            <a href="" class="pull-left">
                                                <img alt="image" src="img/a2.jpg">
                                            </a>
                                            <div class="media-body">
                                                <a href="#">
                                                    Michael Novek
                                                </a>
                                                <small class="text-muted">Today 4:21 pm - 12.06.2014</small>
                                            </div>
                                        </div>
                                        <div class="social-body">
                                            <p>
                                                Many desktop publishing packages and web page editors now use Lorem Ipsum as their
                                                default model text, and a search for 'lorem ipsum' will uncover many web sites still
                                                default model text, and a search for 'lorem ipsum' will uncover many web sites still
                                                in their infancy. Packages and web page editors now use Lorem Ipsum as their
                                                default model text.
                                            </p>
                                        </div>
                                    </div>
                                    <div class="social-feed-box">
                                        <div class="social-avatar">
                                            <a href="" class="pull-left">
                                                <img alt="image" src="img/a3.jpg">
                                            </a>
                                            <div class="media-body">
                                                <a href="#">
                                                    Alice Mediater
                                                </a>
                                                <small class="text-muted">Today 4:21 pm - 12.06.2014</small>
                                            </div>
                                        </div>
                                        <div class="social-body">
                                            <p>
                                                Many desktop publishing packages and web page editors now use Lorem Ipsum as their
                                                default model text, and a search for 'lorem ipsum' will uncover many web sites still
                                                in their infancy. Packages and web page editors now use Lorem Ipsum as their
                                                default model text.
                                            </p>
                                        </div>
                                    </div>
                                    <div class="social-feed-box">
                                        <div class="social-avatar">
                                            <a href="" class="pull-left">
                                                <img alt="image" src="img/a5.jpg">
                                            </a>
                                            <div class="media-body">
                                                <a href="#">
                                                    Monica Flex
                                                </a>
                                                <small class="text-muted">Today 4:21 pm - 12.06.2014</small>
                                            </div>
                                        </div>
                                        <div class="social-body">
                                            <p>
                                                Many desktop publishing packages and web page editors now use Lorem Ipsum as their
                                                default model text, and a search for 'lorem ipsum' will uncover many web sites still
                                                in their infancy. Packages and web page editors now use Lorem Ipsum as their
                                                default model text.
                                            </p>
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
    import Spinner from 'components/Spinner'
    export default {
        name: 'Post',
        components: {
            'spinner': Spinner
        },
        data() {
            return {
                loaded: false
            }
        },
        computed: {
            currentPost() {
                return this.$store.getters.currentPost
            }
        },
        created() {
            this.$store.dispatch('getPost', this.$route.params.post_id).then(() => {
                this.loaded = true
            })
        }
    }

</script>
