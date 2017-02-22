<template>
    <div id="page-top">
        <div class="navbar-wrapper" >
                <nav class="navbar navbar-default navbar-fixed-top navbar-scroll" role="navigation">
                    <div class="container">
                        <div class="navbar-header page-scroll">
                            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>
                            <a class="navbar-brand">ClassGotcha <span class="label label-primary">Beta</span></a>
                        </div>
                        <div id="navbar" class="navbar-collapse collapse">
                            <ul class="nav navbar-nav navbar-right">
                                <li><a class="page-scroll" href="#page-top">Home</a></li>
                                <li><a class="page-scroll" href="#features">Features</a></li>
                                <li><a class="page-scroll" href="#team">Team</a></li>
                                <li><a class="page-scroll" href="#pricing">Pricing</a></li>
                                <li><a class="page-scroll" href="#contact">Contact</a></li>
                                <li><router-link class="page-scroll btn-primary" :to="{name:'register'}">SIGN UP</router-link></li>
                            </ul>
                        </div>
                    </div>
                </nav>
        </div>
        <div id="inSlider" class="carousel carousel-fade" data-ride="carousel">
            <div class="carousel-inner" role="listbox">
                <div class="item active">
                    <div class="container">
                        <div class="carousel-caption">
                            <h1>save college student<br/>
                                from<br/>
                                homeworks, quizzes, exams<br/>
                                </h1>
                            <p>Currently under developement.</p>
                            <p>
                                <router-link  class="btn btn-lg btn-primary" :to="{name:'register'}">SIGN UP</router-link>
                                <router-link class="caption-link" :to="{name:'login'}">LOG IN</router-link>
                            </p>
                        </div>
                    </div>
                    <div class="header-back one"></div>
                </div>
            </div>

        </div>

        <section id="features" class="container services">
            <div class="row">
                <div class="col-sm-3">
                    <h2>Full responsive</h2>
                    <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
                <div class="col-sm-3">
                    <h2>LESS/SASS Files</h2>
                    <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
                <div class="col-sm-3">
                    <h2>6 Charts Library</h2>
                    <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
                <div class="col-sm-3">
                    <h2>Advanced Forms</h2>
                    <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
            </div>
        </section>

        <section  class="container features">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <div class="navy-line"></div>
                    <h1>Over 40+ unique view<br/> <span class="navy"> with many custom components</span> </h1>
                    <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. </p>
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 text-center wow fadeInLeft">
                    <div>
                        <i class="fa fa-mobile features-icon"></i>
                        <h2>Full responsive</h2>
                        <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    </div>
                    <div class="m-t-lg">
                        <i class="fa fa-bar-chart features-icon"></i>
                        <h2>6 Charts Library</h2>
                        <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    </div>
                </div>
                <div class="col-md-6 text-center  wow zoomIn">
                    <img src="img/landing/perspective.png" alt="dashboard" class="img-responsive">
                </div>
                <div class="col-md-3 text-center wow fadeInRight">
                    <div>
                        <i class="fa fa-envelope features-icon"></i>
                        <h2>Mail pages</h2>
                        <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    </div>
                    <div class="m-t-lg">
                        <i class="fa fa-google features-icon"></i>
                        <h2>AngularJS version</h2>
                        <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus.</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12 text-center">
                    <div class="navy-line"></div>
                    <h1>Discover great feautres</h1>
                    <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. </p>
                </div>
            </div>
            <div class="row features-block">
                <div class="col-lg-6 features-text wow fadeInLeft">
                    <small>INSPINIA</small>
                    <h2>Perfectly designed </h2>
                    <p>INSPINIA Admin Theme is a premium admin dashboard template with flat design concept. It is fully responsive admin dashboard template built with Bootstrap 3+ Framework, HTML5 and CSS3, Media query. It has a huge collection of reusable UI components and integrated with latest jQuery plugins.</p>
                    <a href="" class="btn btn-primary">Learn more</a>
                </div>
                <div class="col-lg-6 text-right wow fadeInRight">
                    <img src="img/landing/dashboard.png" alt="dashboard" class="img-responsive pull-right">
                </div>
            </div>
        </section>

        <section id="team" class="gray-section team">
            <div class="container">
                <div class="row m-b-lg">
                    <div class="col-lg-12 text-center">
                        <div class="navy-line"></div>
                        <h1>Our Team</h1>
                        <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod.</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-4 wow fadeInLeft">
                        <div class="team-member">
                            <img src="img/landing/avatar3.jpg" class="img-responsive img-circle img-small" alt="">
                            <h4><span class="navy">Amelia</span> Smith</h4>
                            <p>Lorem ipsum dolor sit amet, illum fastidii dissentias quo ne. Sea ne sint animal iisque, nam an soluta sensibus. </p>
                            <ul class="list-inline social-icon">
                                <li><a href="#"><i class="fa fa-twitter"></i></a>
                                </li>
                                <li><a href="#"><i class="fa fa-facebook"></i></a>
                                </li>
                                <li><a href="#"><i class="fa fa-linkedin"></i></a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-sm-4">
                        <div class="team-member wow zoomIn">
                            <img src="img/landing/avatar1.jpg" class="img-responsive img-circle" alt="">
                            <h4><span class="navy">John</span> Novak</h4>
                            <p>Lorem ipsum dolor sit amet, illum fastidii dissentias quo ne. Sea ne sint animal iisque, nam an soluta sensibus.</p>
                            <ul class="list-inline social-icon">
                                <li><a href="#"><i class="fa fa-twitter"></i></a>
                                </li>
                                <li><a href="#"><i class="fa fa-facebook"></i></a>
                                </li>
                                <li><a href="#"><i class="fa fa-linkedin"></i></a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-sm-4 wow fadeInRight">
                        <div class="team-member">
                            <img src="img/landing/avatar2.jpg" class="img-responsive img-circle img-small" alt="">
                            <h4><span class="navy">Peter</span> Johnson</h4>
                            <p>Lorem ipsum dolor sit amet, illum fastidii dissentias quo ne. Sea ne sint animal iisque, nam an soluta sensibus.</p>
                            <ul class="list-inline social-icon">
                                <li><a href="#"><i class="fa fa-twitter"></i></a>
                                </li>
                                <li><a href="#"><i class="fa fa-facebook"></i></a>
                                </li>
                                <li><a href="#"><i class="fa fa-linkedin"></i></a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-8 col-lg-offset-2 text-center m-t-lg m-b-lg">
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut eaque, laboriosam veritatis, quos non quis ad perspiciatis, totam corporis ea, alias ut unde.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="pricing" class="pricing">
            <div class="container">
                <div class="row m-b-lg">
                    <div class="col-lg-12 text-center">
                        <div class="navy-line"></div>
                        <h1>Pricing</h1>
                        <p>Everything is free under beta test.</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-12 wow zoomIn">
                        <ul class="pricing-plan list-unstyled">
                            <li class="pricing-title">
                                Free 
                            </li>
                            <li class="pricing-desc">
                                Lorem ipsum dolor sit amet, illum fastidii dissentias quo ne. Sea ne sint animal iisque, nam an soluta sensibus.
                            </li>
                            <li class="pricing-price">
                                <span>$0</span> / month
                            </li>
                            <li>
                                Personalized schedule 
                            </li>
                            <li>
                                Class Notes
                            </li>
                            <li>
                                Event orgnization
                            </li>
                            <li>
                                Online Chating
                            </li>
                            <li>
                                Other
                            </li>
                        </ul>
                    </div>

                    <!--<div class="col-lg-6 wow zoomIn">
                        <ul class="pricing-plan list-unstyled">
                            <li class="pricing-title">
                                Premium
                            </li>
                            <li class="pricing-desc">
                                Lorem ipsum dolor sit amet, illum fastidii dissentias quo ne. Sea ne sint animal iisque, nam an soluta sensibus.
                            </li>
                            <li class="pricing-price">
                                <span>$0</span> / month
                            </li>
                            <li>
                                Dashboards
                            </li>
                            <li>
                                Projects view
                            </li>
                            <li>
                                Contacts
                            </li>
                            <li>
                                Calendar
                            </li>
                            <li>
                                AngularJs
                            </li>
                        </ul>
                    </div>-->
                </div>
                <div class="row m-t-lg">
                    <div class="col-lg-8 col-lg-offset-2 text-center m-t-lg">
                        <p>*Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. <span class="navy">Various versions</span>  have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
                    </div>
                </div>
            </div>

        </section>

        <section id="contact" class="gray-section contact">
            <div class="container">
                <div class="row m-b-lg">
                    <div class="col-lg-12 text-center">
                        <div class="navy-line"></div>
                        <h1>Contact Us</h1>
                        <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod.</p>
                    </div>
                </div>
                <div class="row m-b-lg">
                    <div class="col-lg-3 col-lg-offset-3">
                        <address>
                            <strong><span class="navy">Chineseroom Studio</span></strong><br/>
                            Launch Box 108<br/>
                            State College, PA 16803<br/>
                            <abbr title="Email"><i class="fa fa-envelope"></i></abbr>  team@classgotcha.com
                        </address>
                    </div>
                    <div class="col-lg-4">
                        <p class="text-color">
                            Consectetur adipisicing elit. Aut eaque, totam corporis laboriosam veritatis quis ad perspiciatis, totam corporis laboriosam veritatis, consectetur adipisicing elit quos non quis ad perspiciatis, totam corporis ea,
                        </p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-12 text-center">
                        <a href="mailto:test@email.com" class="btn btn-primary">Send us mail</a>
                        <p class="m-t-sm">
                            Or follow us on social platform
                        </p>
                        <ul class="list-inline social-icon">
                            <li><a href="#"><i class="fa fa-twitter"></i></a>
                            </li>
                            <li><a href="#"><i class="fa fa-facebook"></i></a>
                            </li>
                            <li><a href="#"><i class="fa fa-linkedin"></i></a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-8 col-lg-offset-2 text-center m-t-lg m-b-lg">
                        <p><strong>&copy; 2017 Chineseroom</strong><br/> 
                        All rights reserved.</p>
                    </div>
                </div>
            </div>
        </section>
</div>
</template>
<script>
    export default {
        name: 'LandingPage',
        mounted() {
            document.getElementsByTagName("body")[0].style['background-color'] = "#fff"
            /* global $:true */

            $(document).ready(function() {

                $('body').scrollspy({
                    target: '.navbar-fixed-top',
                    offset: 80
                })

                // Page scrolling feature
                $('a.page-scroll').bind('click', function(event) {
                    var link = $(this)
                    $('html, body').stop().animate({
                        scrollTop: $(link.attr('href')).offset().top - 50
                    }, 500)
                    event.preventDefault()
                    $("#navbar").collapse('hide')
                })
            })


            const docElem = document.documentElement
            const header = document.querySelector('.navbar-default')
            let didScroll = false
            const changeHeaderOn = 200

            function init() {
                window.addEventListener('scroll', function(event) {
                    if (!didScroll) {
                        didScroll = true
                        setTimeout(scrollPage, 250)
                    }
                }, false)
            }

            function scrollPage() {
                var sy = scrollY()
                if (sy >= changeHeaderOn) {
                    $(header).addClass('navbar-scroll')
                } else {
                    $(header).removeClass('navbar-scroll')
                }
                didScroll = false
            }

            function scrollY() {
                return window.pageYOffset || docElem.scrollTop
            }

            init()

        }
    }

</script>
<style scoped>
    span.navy {
        color: #1ab394;
    }
    
    p.text-color {
        color: #676a6c;
    }
    
    a.navy-link {
        color: #1ab394;
        text-decoration: none;
    }
    
    a.navy-link:hover {
        color: #179d82;
    }
    
    section p {
        color: #aeaeae;
        font-size: 13px;
    }
    
    address {
        font-size: 13px;
    }
    
    h1 {
        margin-top: 10px;
        font-size: 30px;
        font-weight: 200;
    }
    
    .navy-line {
        width: 60px;
        height: 1px;
        margin: 60px auto 0;
        border-bottom: 2px solid #1ab394;
    }
    
    .navbar-wrapper {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        z-index: 200;
    }
    
    .navbar-wrapper>.container {
        padding-right: 0;
        padding-left: 0;
    }
    
    .navbar-wrapper .navbar {
        padding-right: 15px;
        padding-left: 15px;
    }
    
    .navbar-default.navbar-scroll {
        background-color: #fff;
        border-color: #fff;
        padding: 15px 0;
    }
    
    .navbar-default {
        background-color: transparent;
        border-color: transparent;
        transition: all 0.3s ease-in-out 0s;
    }
    
    .navbar-default .nav li a {
        color: #fff;
        font-family: 'Open Sans', helvetica, arial, sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 14px;
    }
    
    .navbar-nav>li>a {
        padding-top: 25px;
        border-top: 6px solid transparent;
    }
    
    .navbar-default .navbar-nav>.active>a,
    .navbar-default .navbar-nav>.active>a:hover {
        background: transparent;
        color: #fff;
        border-top: 6px solid #1ab394;
    }
    
    .navbar-default .navbar-nav>li>a:hover,
    .navbar-default .navbar-nav>li>a:focus {
        color: #1ab394;
        background: inherit;
    }
    
    .navbar-default .navbar-nav>.active>a:focus {
        background: transparent;
        color: #fff;
    }
    
    .navbar-default .navbar-nav>.active>a:focus {
        background: transparent;
        color: #ffffff;
    }
    
    .navbar-default.navbar-scroll .navbar-nav>.active>a:focus {
        background: transparent;
        color: inherit;
    }
    
    .navbar-scroll.navbar-default .nav li a {
        color: #676a6c;
    }
    
    .navbar-scroll.navbar-default .nav li a:hover {
        color: #1ab394;
    }
    
    .navbar-wrapper .navbar.navbar-scroll {
        padding-top: 0;
        padding-bottom: 0;
        border-bottom: 1px solid #e7eaec;
        border-radius: 0;
    }
    
    .nav>li.active {
        border: none;
        background: inherit;
    }
    
    .nav>li>a {
        padding: 25px 10px 15px 10px;
    }
    
    .navbar-scroll .navbar-nav>li>a {
        padding: 20px 10px;
    }
    
    .navbar-default .navbar-nav>.active>a,
    .navbar-default .navbar-nav>.active>a:hover {
        border-top: 6px solid #1ab394;
    }
    
    .navbar-fixed-top {
        border: none !important;
    }
    
    .navbar-fixed-top.navbar-scroll {
        border-bottom: 1px solid #e7eaec !important;
    }
    
    .navbar-default .navbar-brand {
        font-size: 20px;
        color: #e7eaec;
        display: block;
        border-radius: 0 0 5px 5px;
        font-weight: 700;
        transition: all 0.3s ease-in-out 0s;
    }
    
    .navbar.navbar-scroll .navbar-brand {
        margin-top: 15px;
        border-radius: 5px;
        font-size: 20px;
        padding: 10px;
        height: auto;
        color: #1ab394;
        display: block;
        border-radius: 0 0 5px 5px;
        font-weight: 700;
        transition: all 0.3s ease-in-out 0s;
    }
    
    .header-back {
        height: 470px;
        width: 100%;
    }
    
    .header-back.one {
        background: url('../../static/img/landing/header_one.jpg') 50% 0 no-repeat;
    }
    
    .header-back.two {
        background: url('../../static/img/landing/header_two.jpg') 50% 0 no-repeat;
    }
    
    .carousel {
        height: 470px;
    }
    
    .carousel-caption {
        z-index: 10;
    }
    
    .carousel .item {
        height: 470px;
        background-color: #777;
    }
    
    .carousel-inner>.item>img {
        position: absolute;
        top: 0;
        left: 0;
        min-width: 100%;
        height: 470px;
    }
    
    .carousel-fade .carousel-inner .item {
        opacity: 0;
        -webkit-transition-property: opacity;
        transition-property: opacity;
    }
    
    .carousel-fade .carousel-inner .active {
        opacity: 1;
    }
    
    .carousel-fade .carousel-inner .active.left,
    .carousel-fade .carousel-inner .active.right {
        left: 0;
        opacity: 0;
        z-index: 1;
    }
    
    .carousel-fade .carousel-inner .next.left,
    .carousel-fade .carousel-inner .prev.right {
        opacity: 1;
    }
    
    .carousel-fade .carousel-control {
        z-index: 2;
    }
    
    .carousel-control.left,
    .carousel-control.right {
        background: none;
    }
    
    .carousel-control {
        width: 6%;
    }
    
    .carousel-inner .container {
        position: relative;
    }
    
    .carousel-inner {
        overflow: visible;
    }
    
    .carousel-caption {
        position: absolute;
        top: 100px;
        left: 0;
        bottom: auto;
        right: auto;
        text-align: left;
    }
    
    .carousel-caption {
        position: absolute;
        top: 100px;
        left: 0;
        bottom: auto;
        right: auto;
        text-align: left;
    }
    
    .carousel-caption.blank {
        top: 140px;
    }
    
    .carousel-image {
        position: absolute;
        right: 10px;
        top: 150px;
    }
    
    .carousel-indicators {
        padding-right: 60px;
    }
    
    .carousel-caption h1 {
        font-weight: 700;
        font-size: 38px;
        text-transform: uppercase;
        text-shadow: none;
        letter-spacing: -1.5px;
    }
    
    .carousel-caption p {
        font-weight: 700;
        text-transform: uppercase;
        text-shadow: none;
    }
    
    .caption-link {
        color: #fff;
        margin-left: 10px;
        text-transform: capitalize;
        font-weight: 400;
    }
    
    .caption-link:hover {
        text-decoration: none;
        color: inherit;
    }
    
    .services {
        padding-top: 60px;
    }
    
    .services h2 {
        font-size: 20px;
        letter-spacing: -1px;
        font-weight: 600;
        text-transform: uppercase;
    }
    
    .features-block {
        margin-top: 40px;
    }
    
    .features-text {
        margin-top: 40px;
    }
    
    .features small {
        color: #1ab394;
    }
    
    .features h2 {
        font-size: 18px;
        margin-top: 5px;
    }
    
    .features-text-alone {
        margin: 40px 0;
    }
    
    .features-text-alone h1 {
        font-weight: 200;
    }
    
    .features-icon {
        color: #1ab394;
        font-size: 40px;
    }
    
    .navy-section {
        margin-top: 60px;
        background: #1ab394;
        color: #fff;
        padding: 20px 0;
    }
    
    .gray-section {
        background: #f4f4f4;
        margin-top: 60px;
    }
    
    .team-member {
        text-align: center;
    }
    
    .team-member img {
        margin: auto;
    }
    
    .social-icon a {
        background: #1ab394;
        color: #fff;
        padding: 4px 8px;
        height: 28px;
        width: 28px;
        display: block;
        border-radius: 50px;
    }
    
    .social-icon a:hover {
        background: #179d82;
    }
    
    .img-small {
        height: 88px;
        width: 88px;
    }
    
    .pricing-plan {
        margin: 20px 30px 0 30px;
        border-radius: 4px;
    }
    
    .pricing-plan.selected {
        transform: scale(1.1);
        background: #f4f4f4;
    }
    
    .pricing-plan li {
        padding: 10px 16px;
        border-top: 1px solid #e7eaec;
        text-align: center;
        color: #aeaeae;
    }
    
    .pricing-plan .pricing-price span {
        font-weight: 700;
        color: #1ab394;
    }
    
    li.pricing-desc {
        font-size: 13px;
        border-top: none;
        padding: 20px 16px;
    }
    
    li.pricing-title {
        background: #1ab394;
        color: #fff;
        padding: 10px;
        border-radius: 4px 4px 0 0;
        font-size: 22px;
        font-weight: 600;
    }
    
    .testimonials {
        padding-top: 80px;
        padding-bottom: 90px;
        background-color: #1ab394;
        background-image: url('../../static/img/landing/avatar_all.png');
    }
    
    .big-icon {
        font-size: 56px !important;
    }
    
    .features .big-icon {
        color: #1ab394 !important;
    }
    
    .contact {
        background-image: url('../../static/img/landing/word_map.png');
        background-position: 50% 50%;
        background-repeat: no-repeat;
        margin-top: 60px;
    }
    
    section.timeline {
        padding-bottom: 30px;
    }
    
    section.comments {
        padding-bottom: 80px;
    }
    
    .comments-avatar {
        margin-top: 25px;
        margin-left: 22px;
        margin-bottom: 25px;
    }
    
    .comments-avatar .commens-name {
        font-weight: 600;
        font-size: 14px;
    }
    
    .comments-avatar img {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        margin-right: 10px;
    }
    
    .bubble {
        position: relative;
        height: 120px;
        padding: 20px;
        background: #FFFFFF;
        -webkit-border-radius: 10px;
        -moz-border-radius: 10px;
        border-radius: 10px;
        font-style: italic;
        font-size: 14px;
    }
    
    .bubble:after {
        content: '';
        position: absolute;
        border-style: solid;
        border-width: 15px 14px 0;
        border-color: #FFFFFF transparent;
        display: block;
        width: 0;
        z-index: 1;
        bottom: -15px;
        left: 30px;
    }
    
    .btn-primary.btn-outline:hover,
    .btn-success.btn-outline:hover,
    .btn-info.btn-outline:hover,
    .btn-warning.btn-outline:hover,
    .btn-danger.btn-outline:hover {
        color: #fff;
    }
    
    .btn-primary {
        background-color: #1ab394;
        border-color: #1ab394;
        color: #FFFFFF;
        font-size: 14px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .btn-primary:hover,
    .btn-primary:focus,
    .btn-primary:active,
    .btn-primary.active,
    .open .dropdown-toggle.btn-primary {
        background-color: #179d82;
        border-color: #179d82;
        color: #FFFFFF;
    }
    
    .btn-primary:active,
    .btn-primary.active,
    .open .dropdown-toggle.btn-primary {
        background-image: none;
    }
    
    .btn-primary.disabled,
    .btn-primary.disabled:hover,
    .btn-primary.disabled:focus,
    .btn-primary.disabled:active,
    .btn-primary.disabled.active,
    .btn-primary[disabled],
    .btn-primary[disabled]:hover,
    .btn-primary[disabled]:focus,
    .btn-primary[disabled]:active,
    .btn-primary.active[disabled],
    fieldset[disabled] .btn-primary,
    fieldset[disabled] .btn-primary:hover,
    fieldset[disabled] .btn-primary:focus,
    fieldset[disabled] .btn-primary:active,
    fieldset[disabled] .btn-primary.active {
        background-color: #1dc5a3;
        border-color: #1dc5a3;
    }
    
    @media (min-width: 768px) {
        {
            /* Navbar positioning foo */
            /* The navbar becomes detached from the top, so we round the corners */
            /* Bump up size of carousel content */
        }
        .navbar-wrapper {
            margin-top: 20px;
        }
        .navbar-wrapper .container {
            padding-right: 15px;
            padding-left: 15px;
        }
        .navbar-wrapper .navbar {
            padding-right: 0;
            padding-left: 0;
        }
        .navbar-wrapper .navbar {
            border-radius: 4px;
        }
        .carousel-caption p {
            margin-bottom: 20px;
            font-size: 14px;
            line-height: 1.4;
        }
        .featurette-heading {
            font-size: 50px;
        }
    }
    
    @media (max-width: 992px) {
        .carousel-image {
            display: none;
        }
    }
    
    @media (max-width: 768px) {
        .carousel-caption,
        .carousel-caption.blank {
            left: 5%;
            top: 80px;
        }
        .carousel-caption h1 {
            font-size: 28px;
        }
        .navbar.navbar-scroll .navbar-brand {
            margin-top: 6px;
        }
        .navbar-default {
            background-color: #fff;
            border-color: #fff;
            padding: 15px 0;
        }
        .navbar-default .navbar-nav>.active>a:focus {
            background: transparent;
            color: inherit;
        }
        .navbar-default .nav li a {
            color: #676a6c;
        }
        .navbar-default .nav li a:hover {
            color: #1ab394;
        }
        .navbar-wrapper .navbar {
            padding-top: 0;
            padding-bottom: 5px;
            border-bottom: 1px solid #e7eaec;
            border-radius: 0;
        }
        .nav>li>a {
            padding: 25px 10px 15px 10px;
        }
        .navbar-nav>li>a {
            padding: 20px 10px;
        }
        .navbar .navbar-brand {
            margin-top: 6px;
            border-radius: 5px;
            font-size: 12px;
            padding: 10px;
            height: auto;
        }
        .navbar-wrapper .navbar {
            padding-left: 15px;
            padding-right: 5px;
        }
        .navbar-default .navbar-nav>.active>a,
        .navbar-default .navbar-nav>.active>a:hover {
            color: inherit;
        }
        .carousel-control {
            display: none;
        }
    }
    
    @media (min-width: 992px) {
        .featurette-heading {
            margin-top: 120px;
        }
    }
    
    @media (max-width: 768px) {
        .navbar .navbar-header {
            display: block;
            float: none;
        }
        .navbar .navbar-header .navbar-toggle {
            background-color: #ffffff;
            padding: 9px 10px;
            border: none;
        }
    }

</style>
