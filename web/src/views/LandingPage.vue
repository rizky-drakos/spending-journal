<!-- *****************************************************************************
     TEMPLATE
     *****************************************************************************  -->
<template>
  <div class="landing-page">
    <div id="google-signin-btn" class="g-signin2" data-onsuccess="onSignIn"></div>
    <span>or</span>
    <v-btn outlined color="indigo" @click="logInAsGuest">Try</v-btn>
  </div>
</template>
<!--  *****************************************************************************
      STYLE
      *****************************************************************************  -->
<style>
/*  Vertically and horizontally center the elements inside 
    Reference: https://stackoverflow.com/questions/19026884/flexbox-center-horizontally-and-vertically
*/
.landing-page {
  display: flex;           /* establish flex container */
  flex-direction: column;  /* make main axis vertical */
  justify-content: center; /* center items vertically, in this case */
  align-items: center;     /* center items horizontally, in this case */
  height: 500px;
}
</style>
<!--  ****************************************************************************
      SCRIPT
      ****************************************************************************  -->
<script>
import TokenService from "../services/token.service"
import ApiService from "../services/api.service"


export default {
  mounted() {
    const gapi_plugin = document.createElement("script")
    gapi_plugin.setAttribute("src", "https://apis.google.com/js/platform.js")
    gapi_plugin.async = true
    gapi_plugin.defer = true
    gapi_plugin.onload = () => {
      window.gapi.signin2.render("google-signin-btn", {
        width: 240,
        height: 50,
        longtitle: true,
        theme: 'dark',
        onsuccess: this.onSignIn
      })
    }
    document.head.appendChild(gapi_plugin)
    console.log("From Landing page")
  },
  methods: {
    async onSignIn(user) {
      const { data } = await ApiService.make_custom_request({
        method: "post",
        url: "http://spending-journal.herokuapp.com/api/access-token",
        data: {
          "id_token": user.getAuthResponse().id_token
        }
      })
      const access_token = data["access_token"]
      TokenService.save_token(access_token)
      ApiService.set_access_token()
      this.$router.push("/journal")
    },
    async logInAsGuest() {
      const { data } = await ApiService.get('/guest-token')
      const access_token = data["access_token"]
      TokenService.save_token(access_token)
      ApiService.set_access_token()
      this.$router.push("/journal")
    }
  },
}
</script>