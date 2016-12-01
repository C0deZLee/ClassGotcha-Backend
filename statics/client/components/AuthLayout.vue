<template>
  <div class="middle-box text-center loginscreen animated fadeInDown">
      <div>
          <div>
              <h1 class="logo-name">IN+</h1>
          </div>
          <router-view></router-view>
          <p class="m-t"> <small>Inspinia we app framework base on Bootstrap 3 &copy; 2014</small> </p>
      </div>
  </div>
</template>

<script>
import Login from '../views/Login'
import Register from '../views/Register'


export default {
  component:{
    'login': Login,
    'register' :Register
  }
}
$(document).ready(function () {
  $("body").addClass("gray-bg")
})
</script>
