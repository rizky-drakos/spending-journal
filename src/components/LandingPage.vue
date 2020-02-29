<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <div id="google-signin-btn" class="g-signin2" data-onsuccess="onSignIn"></div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AutheticationStore from "../stores/AuthenticationStore";

export default {
  mounted() {
    const gapi_plugin = document.createElement("script");
    gapi_plugin.setAttribute("src", "https://apis.google.com/js/platform.js");
    gapi_plugin.async = true;
    gapi_plugin.defer = true;
    gapi_plugin.onload = () => {
      window.gapi.signin2.render("google-signin-btn", {
        onsuccess: this.onSignIn
      });
    };
    document.head.appendChild(gapi_plugin);
  },
  methods: {
    onSignIn() {
      AutheticationStore.data.isAuthenticated = true;
      this.$router.push("/journal");
    }
  }
};
</script>