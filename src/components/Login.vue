<template>
  <a v-on:click="signOut">Sign out</a>
</template>

<script>
import AutheticationStore from "../stores/AuthenticationStore";

export default {
  methods: {
    signOut() {
      // window.gapi could be undefined if Login is
      // loaded after Home, because Home is also
      // responsible for window.gapi initialization
      var self = this;
      window.gapi.auth2
        .getAuthInstance()
        .signOut()
        .then(() => {
          console.log("User signed out.");
          AutheticationStore.data.isAuthenticated = false;
          self.$router.push("/");
        });
    }
  }
};
</script>