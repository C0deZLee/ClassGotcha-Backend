<template>
  <div class="loginColumns animated fadeInDown">

          <router-view></router-view>

            <div class="text-right text-white">
               <small>Chineseroom Studio © 2015-2017</small>
            </div>

  </div>

</template>

<script>
    export default {
        name: 'AuthLayout',
        beforeCreate() {
            // /* global $:true */
            // $(document.body).class('gray-bg')
        }
    }

</script>
