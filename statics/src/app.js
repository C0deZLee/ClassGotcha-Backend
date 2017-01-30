import Vue from 'vue'
import Resource from 'vue-resource'
import Router from 'vue-router'
import Mask from 'v-mask'
import { sync } from 'vuex-router-sync'

import router from './router'
import store from './store'

import App from 'views/components/App'
import * as cookie from './utils/cookie'

Vue.use(Router)
Vue.use(Resource)
Vue.use(Mask)

sync(store, router)

// set csrf token for django
Vue.http.headers.common['X-CSRFToken'] = cookie.getCookie('csrftoken')

export const app = new Vue({
    el: '#app',
    data: {},
    mounted: () => {
        const formData = { token: cookie.getCookie('token') }
        console.log('tokenVerify', formData)
        this.$store.dispatch('tokenVerify', formData)
        /* global $:true SmoothlyMenu:true */
        $(document).ready(function() {
            // Add body-small class if window less than 768px
            if ($(this).width() < 769) {
                $('body').addClass('body-small')
            } else {
                $('body').removeClass('body-small')
            }

            // MetsiMenu
            $('#side-menu').metisMenu()

            // Collapse ibox function
            $('.collapse-link').bind('click', function() {
                var ibox = $(this).closest('div.ibox')
                var button = $(this).find('i')
                var content = ibox.find('div.ibox-content')
                content.slideToggle(200)
                button.toggleClass('fa-chevron-up').toggleClass('fa-chevron-down')
                ibox.toggleClass('').toggleClass('border-bottom')
                setTimeout(function() {
                    ibox.resize()
                    ibox.find('[id^=map-]').resize()
                }, 50)
            })

            // Close ibox function
            $('.close-link').bind('click', function() {
                var content = $(this).closest('div.ibox')
                content.remove()
            })

            // Fullscreen ibox function
            $('.fullscreen-link').bind('click', function() {
                var ibox = $(this).closest('div.ibox')
                var button = $(this).find('i')
                $('body').toggleClass('fullscreen-ibox-mode')
                button.toggleClass('fa-expand').toggleClass('fa-compress')
                ibox.toggleClass('fullscreen')
                setTimeout(function() {
                    $(window).trigger('resize')
                }, 100)
            })

            // Close menu in canvas mode
            $('.close-canvas-menu').bind('click', function() {
                $("body").toggleClass("mini-navbar")
                SmoothlyMenu()
            })

            // Run menu of canvas
            $('body.canvas-menu .sidebar-collapse').slimScroll({
                height: '100%',
                railOpacity: 0.9
            })

            // Open close right sidebar
            $('.right-sidebar-toggle').bind('click', function() {
                $('#right-sidebar').toggleClass('sidebar-open')
            })

            // Initialize slimscroll for right sidebar
            $('.sidebar-container').slimScroll({
                height: '100%',
                railOpacity: 0.4,
                wheelStep: 10
            })

            // Open close small chat
            $('.open-small-chat').bind('click', function() {
                $(this).children().toggleClass('fa-comments').toggleClass('fa-remove')
                $('.small-chat-box').toggleClass('active')
            })

            // Initialize slimscroll for small chat
            $('.small-chat-box .content').slimScroll({
                height: '234px',
                railOpacity: 0.4
            })

            // Small todo handler
            $('.check-link').bind('click', function() {
                var button = $(this).find('i')
                var label = $(this).next('span')
                button.toggleClass('fa-check-square').toggleClass('fa-square-o')
                label.toggleClass('todo-completed')
                return false
            })

            // Minimalize menu
            $('.navbar-minimalize').bind('click', function() {
                $("body").toggleClass("mini-navbar")
                SmoothlyMenu()

            })

            // Tooltips demo
            $('.tooltip-demo').tooltip({
                selector: "[data-toggle=tooltip]",
                container: "body"
            })

            // Full height of sidebar
            function fix_height() {
                var heightWithoutNavbar = $("body > #wrapper").height() - 61
                $(".sidebard-panel").css("min-height", heightWithoutNavbar + "px")

                var navbarHeigh = $('nav.navbar-default').height()
                var wrapperHeigh = $('#page-wrapper').height()

                if (navbarHeigh > wrapperHeigh) {
                    $('#page-wrapper').css("min-height", navbarHeigh + "px")
                }

                if (navbarHeigh < wrapperHeigh) {
                    $('#page-wrapper').css("min-height", $(window).height() + "px")
                }

                if ($('body').hasClass('fixed-nav')) {
                    if (navbarHeigh > wrapperHeigh) {
                        $('#page-wrapper').css("min-height", navbarHeigh - 60 + "px")
                    } else {
                        $('#page-wrapper').css("min-height", $(window).height() - 60 + "px")
                    }
                }

            }

            fix_height()

            // Fixed Sidebar
            $(window).bind("load", function() {
                if ($("body").hasClass('fixed-sidebar')) {
                    $('.sidebar-collapse').slimScroll({
                        height: '100%',
                        railOpacity: 0.9
                    })
                }
            })

            // Move right sidebar top after scroll
            $(window).scroll(function() {
                if ($(window).scrollTop() > 0 && !$('body').hasClass('fixed-nav')) {
                    $('#right-sidebar').addClass('sidebar-top')
                } else {
                    $('#right-sidebar').removeClass('sidebar-top')
                }
            })

            $(window).bind("load resize scroll", function() {
                if (!$("body").hasClass('body-small')) {
                    fix_height()
                }
            })

            $("[data-toggle=popover]")
                .popover()

            // Add slimscroll to element
            $('.full-height-scroll').slimscroll({
                height: '100%'
            })
        })
    },
    router,
    store,
    render: h => h(App)
})

// export {
//     app,
//     router,
//     store
// }
