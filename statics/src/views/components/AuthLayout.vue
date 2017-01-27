<template>
  <div class="middle-box text-center loginscreen animated fadeInDown">
      <div>
          <div>
              <h1 class="logo-name">IN+</h1>
          </div>
          <router-view></router-view>
          <p class="m-t"> <small>Chineserooms Studio</small> </p>
      </div>
  </div>
</template>

<script>
    export default {
        name: 'AuthLayout',

    }

</script>
