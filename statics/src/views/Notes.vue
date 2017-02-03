<template>
    <div>
    <div class="row wrapper border-bottom white-bg page-heading">
                <div class="col-lg-9">
                    <h2>File Manager</h2>
                    <ol class="breadcrumb">
                        <li>
                            <a href="index.html">Home</a>
                        </li>
                        <li>
                            App Views
                        </li>
                        <li class="active">
                            <strong>File Manager</strong>
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
                                    <li><a href=""><i class="fa fa-folder"></i> Notes</a></li>
                                    <li><a href=""><i class="fa fa-folder"></i> Lectures</a></li>
                                    <li><a href=""><i class="fa fa-folder"></i> Homeworks</a></li>
                                    <li><a href=""><i class="fa fa-folder"></i> Exams</a></li>
                                    <li><a href=""><i class="fa fa-folder"></i> Labs</a></li>
                                    <li><a href=""><i class="fa fa-folder"></i> Others</a></li>
                                </ul>
                              
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
                            <div class="file-box">
                                <div class="file">
                                    <a href="#">
                                        <span class="corner"></span>

                                        <div class="icon">
                                            <i class="fa fa-file-pdf-o"></i>
                                        </div>
                                    </a>
                                     <div class="file-name">
                                           <a href="#"> Document_2014.doc</a>
                                            <br>
                                          <small><a>Test User</a></small>
                                            <br>
                                            <small>Added: Jan 11, 2014</small>
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
        components: {
            upload: Upload
        }
    }

</script>
