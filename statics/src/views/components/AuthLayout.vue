<template><div>
       <div class="text-center m-t">
              <h3 class="logo-name">ClassGotcha</h3>
          </div>
  <div class="middle-box text-center loginscreen">

          <router-view></router-view>
          <p class="m-t"> <small>2015-2017 @Chineserooms Studio</small> </p>
  </div>
  </div>
</template>

<script>
    export default {
        name: 'AuthLayout',

    }

</script>
