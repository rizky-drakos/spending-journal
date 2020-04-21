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
        url: "http://192.168.1.6:5000/access-token",
        data: {
          "id_token": user.getAuthResponse().id_token
        }
      })
      const access_token = data["access_token"]
      TokenService.save_token(access_token)
      ApiService.set_access_token()
      this.$router.push("/journal")
    }
  }
}
</script>