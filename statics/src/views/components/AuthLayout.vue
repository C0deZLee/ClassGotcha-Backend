<template>
  <div class="loginColumns animated fadeInDown">
        <router-view></router-view>
        <div class="text-right text-white">
            <small>Classgotcha © 2015-2017</small>
        </div>
  </div>

</template>

<script>
    export default {
        name: 'AuthLayout',
        mounted() {
            document.getElementsByTagName("Body")[0].style['background-color'] = "#2f4050"

        }
    }

</script>
