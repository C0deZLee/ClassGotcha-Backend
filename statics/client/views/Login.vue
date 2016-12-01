<template>
  <form class="m-t" role="form" action="index.html">
    <p>Perfectly designed and precisely prepared admin theme with over 50 pages with extra new web app views.
        <!--Continually expanded and constantly improved Inspinia Admin Them (IN+)-->
    </p>
    <p>Login in. To see it in action.</p>
      <div class="form-group">
          <input type="email" class="form-control" placeholder="Username" required="">
      </div>
      <div class="form-group">
          <input type="password" class="form-control" placeholder="Password" required="">
      </div>
      <button type="submit" class="btn btn-primary block full-width m-b">Login</button>

      <a href="#"><small>Forgot password?</small></a>
      <p class="text-muted text-center"><small>Do not have an account?</small></p>
      <a class="btn btn-sm btn-white btn-block" href="register.html">Create an account</a>
  </form>
</template>

<script>
export default {
  name: 'login'
}
// UI
$(document).ready(function () {
  $("body").addClass("gray-bg")
})

</script>
