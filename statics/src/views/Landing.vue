<template>
    <div id="page-top">
        <div class="navbar-wrapper" >
                <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
                    <div class="container">
                        <div class="navbar-header">
                            <!--<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>-->
                            <a class="navbar-brand"> ClassGotcha <span class="label label-primary">Beta</span></a>
                        </div>
                           
                               <ul class="m-l nav navbar-nav navbar-right">
                                <li><router-link class="btn-primary" style=" color: #ffffff;" :to="{name:'register'}" >SIGN UP</router-link></li>
                                <li><router-link  :to="{name:'login'}">LOG IN</router-link></li>
                            </ul> 
                        <div id="navbar" class="navbar-collapse collapse">
                            <ul class="nav navbar-nav navbar-right">
                                <li><a class="page-scroll" href="#page-top">Home</a></li>
                                <li><a class="page-scroll" href="#features">Features</a></li>
                                <li><a class="page-scroll" href="#team">Team</a></li>
                                <li><a class="page-scroll" href="#pricing">Pricing</a></li>
                                <li><a class="page-scroll" href="#contact">Contact</a></li>
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
                            <h1>
                                Save you from <br>
                                college</h1>
                            <p>Your personal assistant for courses organizing.</p>
                            <p>
                                <router-link  class="btn btn-lg btn-primary" :to="{name:'register'}">Join Now</router-link>
                            </p>
                        </div>
                    </div>
                    <div class="header-back one"></div>
                </div>
            </div>

        </div>

<section id="features" class="features">
    <div class="container">
        <div class="row">
            <div class="col-lg-12 text-center">
                <div class="navy-line"></div>
                <h1>Our Great Feautres</h1>
                <p>YOUR PERSONAL ASSISTANT FOR COURSES ORGANIZING.</p>
            </div>
        </div>
        <br>
        <div class="row">
                <div class="col-sm-3">
                    <h2>INTERACTIVE CALENDAR</h2>
                    <p>Courses deadlines and shared activities are automatically pushed onto your tasks list. With simple drag and drop, you can arrange them on your calendar without conflicts with personal events.</p>
             <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
                <div class="col-sm-3">
                    <h2>COMMUNICATION</h2>
                    <p>To create an environment closed to your daily online social experience, the Q&A system use the form of facebook activities feeds. The instant messaging chatroom can help you find and chat with your classmates at one click.</p>
              <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
                <div class="col-sm-3">
                    <h2>NOTES SHARING</h2>
                    <p>To create an environment closed to your daily online social experience, the Q&A system use the form of facebook activities feeds. The instant messaging chatroom can help you find and chat with your classmates at one click.</p>
                <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
                <div class="col-sm-3">
                    <h2>LEARNING ANALYTIC</h2>
                    <p>A powerful learning analytic backend can provide a personalized learning profile. It analyzes all your online footprints and provide you a thorough report to inform you where you are in the semester. </p>
              <p><a class="navy-link" href="#" role="button">Details &raquo;</a></p>
                </div>
            </div>
    </div>

</section>
                <div class="gray-line"></div>

        <section  class="container features">
        <div class="row features-block">

        <div class="col-lg-5  features-text">
                <small>CLASSGOTCHA</small>
                <h1>Interactive Calendar</h1>
                <i class="fa fa fa-calendar-check-o big-icon pull-left"></i>
                <p>Courses deadlines and shared activities are automatically pushed onto your tasks list. With simple drag and drop, you can arrange them on your calendar without conflicts with personal events.</p>
        </div>
        <div class="col-lg-7 text-right wow fadeInRight animated">
           <img  src="~img/landing/homepage.png" alt="dashboard" class="img-responsive shadow pull-right">
        </div>
    </div>
                <div class="gray-line"></div>
    
            <div class="row features-block">
  <div class="col-lg-7 text-right wow fadeInLeft animated">
           <img  src="~img/landing/classroom.png" alt="dashboard" class="img-responsive shadow">
        </div>
        
        <div class="col-lg-5  features-text">
                <small>CLASSGOTCHA</small>
                <h1>Communication</h1>
                <i class="fa fa fa-users big-icon pull-right"></i>
                <p>To create an environment closed to your daily online social experience, the Q&A system use the form of facebook activities feeds. The instant messaging chatroom can help you find and chat with your classmates at one click.</p>
                </div>
      
    </div>     
                <div class="gray-line"></div>
    
       <div class="row features-block">

        <div class="col-lg-5  features-text">
                <small>CLASSGOTCHA</small>
                <h1>Notes Sharing</h1>
                <i class="fa fa fa-file-text big-icon pull-left"></i>
                <p>To create an environment closed to your daily online social experience, the Q&A system use the form of facebook activities feeds. The instant messaging chatroom can help you find and chat with your classmates at one click.</p>
        </div>
        <div class="col-lg-7 text-right wow fadeInRight animated">
           <img  src="~img/landing/notes.png" alt="dashboard" class="img-responsive shadow pull-right">
        </div>
    </div>
          <!--  <div class="row">
                <div class="col-lg-12 text-center">
                    <div class="navy-line"></div>
                    <h1>Greatly Designed User Interface</h1>
                    <p>YOUR PERSONAL ASSISTANT FOR COURSES ORGANIZING.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 text-center wow fadeInLeft">
                    <div>
                        <i class="fa fa-calendar-check-o features-icon"></i>
                        <h2>Calendar</h2>
                        <p>Courses deadlines and shared activities are automatically pushed onto your tasks list. With simple drag and drop, you can arrange them on your calendar without conflicts with personal events. </p>
                    </div>
                    <div class="m-t-lg">
                        <i class="fa fa-bar-chart features-icon"></i>
                        <h2>Learning Analytics</h2>
                        <p>A powerful learning analytics backend can provide a personalized learning profile. It analyzes all your online footprints and provide you a thorough report to inform you where you are in the semester. </p>
                    </div>
                </div>
                <div class="col-md-6 text-center wow zoomIn">
                    <img  src="~img/landing/homepage.png" alt="dashboard" class="img-responsive shadow">
                </div>
                <div class="col-md-3 text-center wow fadeInRight">
                    <div>
                        <i class="fa fa-file-text-o features-icon"></i>
                        <h2>Notes sharing</h2>
                        <p>You can view and share course notes with all classmates. Shared notes are automatically tagged for easy Notes with high quality can get rewards.</p>
                    </div>
                     <div class="m-t-lg">
                        <i class="fa fa-comments-o features-icon"></i>
                        <h2>Communication</h2>
                        <p>To create an environment closed to your daily online social experience, the Q&A system use the form of facebook activities feeds. The instant messaging chatroom can help you find and chat with your classmates at one click.</p>
                    </div>
                </div>
            </div>
            <!--<div class="row">
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
            </div>-->
        </section>

        <section id="team" class="gray-section team">
            <div class="container">
                <div class="row m-b-lg">
                    <div class="col-lg-12 text-center">
                        <div class="navy-line"></div>
                        <h1>Our Team</h1>
                        <p>YOUR PERSONAL ASSISTANT FOR COURSES ORGANIZING.</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-4">
                         <div class="team-member">
                            <img src="~img/landing/simowu.png" class="img-responsive img-circle" alt="">
                            <h4><span class="navy">Simo</span> Wu</h4>
                            <p>Expert in data mining. <br>  Help you understand your learning activities better. </p>
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
                        <div class="team-member">
                            <img src="~img/landing/xiangli.png" class="img-responsive img-circle" alt="">
                            <h4><span class="navy">Xiang</span> Li</h4>
                            <p>Developing expert. <br> Provide perfect experience in organizing your learning activities.</p>
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
                        <div class="team-member">
                            <img src="~img/landing/qiyuanli.png" class="img-responsive img-circle" alt="">
                            <h4><span class="navy">Qiyuan</span> Li</h4>
                            <p>Educational Designer. <br> Create sustained learning community for you.</p>
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
                <!--<div class="row">
                    <div class="col-lg-8 col-lg-offset-2 text-center m-t-lg m-b-lg">
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut eaque, laboriosam veritatis, quos non quis ad perspiciatis, totam corporis ea, alias ut unde.</p>
                    </div>
                </div>
            </div>-->
        </section>

        <section id="pricing" class="pricing">
            <div class="container">
                <div class="row m-b-lg">
                    <div class="col-lg-12 text-center">
                        <div class="navy-line"></div>
                        <h1>Pricing</h1>
                        <!--<p>Everything is free under beta test.</p>-->
                    </div>
                </div>
                <div class="row">
                    <div class=" col-md-offset-4 col-md-4 wow zoomIn">
                        <ul class="pricing-plan list-unstyled">
                            <li class="pricing-title">
                                Free 
                            </li>
                            <li class="pricing-desc">
                                Everything is free under beta test.
                            </li>
                            <li class="pricing-price">
                                <span>$0</span> / month
                            </li>
                            <li>
                                Personalized schedule 
                            </li>
                            <li>
                                Class notes sharing
                            </li>
                            <li>
                                Event orgnization
                            </li>
                            <li>
                                Online chating
                            </li>
                            <li>
                               All Other services
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
                <!--<div class="row m-t-lg">
                    <div class="col-lg-8 col-lg-offset-2 text-center m-t-lg">
                        <p>*Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. <span class="navy">Various versions</span>  have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
                    </div>
                </div>-->
            </div>

        </section>

        <section id="contact" class="gray-section contact">
            <div class="container">
                <div class="row m-b-lg">
                    <div class="col-lg-12 text-center">
                        <div class="navy-line"></div>
                        <h1>Contact Us</h1>
                        <p>Have questions? Just let us know.</p>
                    </div>
                </div>
                <div class="row m-b-lg">
                    <div class="col-lg-3 col-lg-offset-3">
                        <address>
                            <h3><span class="navy">ClassGotcha</span></h3>
                            Launch Box<br/>
                            State College, PA 16803<br/>
                            <!--<abbr title="Email"><i class="fa fa-envelope"></i></abbr>  team@classgotcha.com-->
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
                        <a href="mailto:team@classgotcha.com" class="btn btn-primary">Send us mail</a>
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
                        <p><strong>&copy; 2017 ClassGotcha Team</strong><br/> 
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
                    target: '.page-scroll',
                    offset: 80
                })

                // Page scrolling feature
                setTimeout($('a.page-scroll').bind('click', function(event) {
                    var link = $(this)
                    $('html, body').stop().animate({
                        scrollTop: $(link.attr('href')).offset().top - 50
                    }, 500)
                    event.preventDefault()
                    $("#navbar").collapse('hide')
                }), 250)

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
    
    .gray-line {
        width: 60px;
        height: 1px;
        margin: 60px auto 0;
        border-bottom: 2px solid #aeaeae;
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
    
    .nav>li.active {
        border: none;
        background: inherit;
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
    
    .shadow {
        -webkit-box-shadow: 10px 10px 55px -1px rgba(0, 0, 0, 0.69);
        -moz-box-shadow: 10px 10px 55px -1px rgba(0, 0, 0, 0.69);
        box-shadow: 10px 10px 55px -1px rgba(0, 0, 0, 0.69);
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
