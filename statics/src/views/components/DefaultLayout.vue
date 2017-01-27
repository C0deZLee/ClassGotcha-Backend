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
        <right-side-bar></right-side-bar>
    <!-- Modal window -->
    <modal-window></modal-window>
    <!-- End wrapper-->
    </div>
</template>

<script>
    import SideBar from './SideBar'
    import TopBar from './TopBar'
    import RightSideBar from './RightSideBar'
    import ModalWindow from './ModalWindow'

    export default {
        name: 'DefaultLayout',
        components: {
            SideBar,
            TopBar,
            RightSideBar,
            ModalWindow
        }
    }

</script>
