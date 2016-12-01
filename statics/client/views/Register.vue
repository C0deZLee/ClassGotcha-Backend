<template>
    <form class="m-t" role="form" action="login.html">
      <p>Create account to see it in action.</p>
              <div class="form-group">
                  <input type="text" class="form-control" placeholder="Name" required="">
              </div>
              <div class="form-group">
                  <input type="email" class="form-control" placeholder="Email" required="">
              </div>
              <div class="form-group">
                  <input type="password" class="form-control" placeholder="Password" required="">
              </div>
              <div class="form-group">
                    <div class="checkbox i-checks"><label> <input type="checkbox"><i></i> Agree the terms and policy </label></div>
              </div>
              <button type="submit" class="btn btn-primary block full-width m-b">Register</button>

              <p class="text-muted text-center"><small>Already have an account?</small></p>
              <a class="btn btn-sm btn-white btn-block" href="login.html">Login</a>
        </form>
</template>

<style>
/* iCheck plugin Square skin, green
----------------------------------- */
.icheckbox_square-green,
.iradio_square-green {
    display: inline-block;
    *display: inline;
    vertical-align: middle;
    margin: 0;
    padding: 0;
    width: 22px;
    height: 22px;
    background: url(../css/patterns/icheck/green.png) no-repeat;
    border: none;
    cursor: pointer;
}

.icheckbox_square-green {
    background-position: 0 0;
}
.icheckbox_square-green.hover {
    background-position: -24px 0;
}
.icheckbox_square-green.checked {
    background-position: -48px 0;
}
.icheckbox_square-green.disabled {
    background-position: -72px 0;
    cursor: default;
}
.icheckbox_square-green.checked.disabled {
    background-position: -96px 0;
}

.iradio_square-green {
    background-position: -120px 0;
}
.iradio_square-green.hover {
    background-position: -144px 0;
}
.iradio_square-green.checked {
    background-position: -168px 0;
}
.iradio_square-green.disabled {
    background-position: -192px 0;
    cursor: default;
}
.iradio_square-green.checked.disabled {
    background-position: -216px 0;
}

/* HiDPI support */
@media (-o-min-device-pixel-ratio: 5/4), (-webkit-min-device-pixel-ratio: 1.25), (min-resolution: 120dpi) {
    .icheckbox_square-green,
    .iradio_square-green {
        background-image: url(../css/patterns/icheck/green@2x.png);
        -webkit-background-size: 240px 24px;
        background-size: 240px 24px;
    }
}
</style>

<script>
export default {
  name: 'login'
}

// UI
$(document).ready(function () {
  $("body").addClass("gray-bg")
})
var $script = require("scriptjs");
$script("https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/icheck.min.js", function() {
  $('.i-checks').iCheck({
      checkboxClass: 'icheckbox_square-green',
      radioClass: 'iradio_square-green',
  });
});
</script>
