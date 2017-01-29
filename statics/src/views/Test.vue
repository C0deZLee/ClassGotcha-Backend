<template>
    <div class="ibox">
            <div class="ibox-content">
<upload-avatar></upload-avatar>
</div>
</div>
</template>
<script>
    import UploadAvatar from 'components/UploadAvatar'

    export default {
        name: 'Test',
        components: {
            'upload-avatar': UploadAvatar
        }
    }

</script>
