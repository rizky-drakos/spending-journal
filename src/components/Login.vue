<template>
    <a v-on:click="signOut">Sign out</a>
</template>

<script>
    export default {
        methods: {
            signOut() {
                var self = this
                window.gapi.auth2.getAuthInstance().signOut().then(() => {
                    console.log('User signed out.');
                    self.$router.push("/")
                });
            }
        }
    }
</script>