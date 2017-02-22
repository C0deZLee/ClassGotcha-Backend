<template>
    <div class="middle-box text-center animated fadeInDown">
        <h1>403</h1>
        <h3 class="font-bold">Forbidden</h3>

        <div class="error-desc">
            Sorry, but you are not allowed to visit this page, try to login to continue.
            <form class="form-inline m-t" role="form">
                <div class="form-group">
                    <router-link :to="{name:'login'}" placeholder="login" class="btn btn-primary">Login</router-link>
                </div>
                
            </form>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'Page403'
    }

</script>
