<template>
    <div id="wrapper">
        <!-- Navigation -->
        <side-bar></side-bar>
        <!-- Page wraper -->
        <div id="page-wrapper" class="gray-bg">
            <!-- Page wrapper -->
            <top-bar></top-bar>
            <!-- Router view -->
            <router-view></router-view>
          <!-- End page wrapper-->
        </div>
    <!-- Modal window -->
    <modal-window></modal-window>
    <!-- End wrapper-->
    </div>
</template>

<script>
import SideBar from './SideBar'
import TopBar from './TopBar'

export default {
  components: {
    SideBar,
    TopBar
  }
}

// UI
$(document).ready(function () {
  $("body").removeClass("gray-bg")
})

</script>
