<!-- *****************************************************************************
     TEMPLATE
     *****************************************************************************  -->
<template>
  <v-app>
    <v-navigation-drawer permanent app width="150">
      <!-- <v-list-item class="px-2">

        <v-list-item-avatar>
          User a colon to mark src as a dynamic attribute
          <v-img :src="user.picture_url"></v-img>
        </v-list-item-avatar>

        <v-list-item-title v-text="user.name"></v-list-item-title>
      </v-list-item>

      <v-divider></v-divider> -->
      <v-list dense>
        <v-list-item to="dashboard">
          <v-list-item-action>
            <v-icon>mdi-chart-bar</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>DASHBOARD</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item to="journal">
          <v-list-item-action>
            <v-icon>mdi-calendar-text-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>JOURNAL</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item to="item-types">
          <v-list-item-action>
            <v-icon>mdi-shape-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>ITEM TYPES</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link v-on:click="signOut">
          <v-list-item-action>
            <v-icon>mdi-logout-variant</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>LOG OUT</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-content app>
      <slot></slot>
    </v-content>
  </v-app>
</template>
<!-- *****************************************************************************
     TEMPLATE
     *****************************************************************************  -->
<style>
.v-list-item {
  padding-left: 10px;
  padding-right: 10px;
}
.v-application--is-ltr .v-list-item__action:first-child {
  margin-top: 0px;
  margin-bottom: 0px;
  margin-right: 5px;
}
.v-list--dense .v-list-item .v-list-item__content {
  padding: 8px 0;
}
</style>
<!-- *****************************************************************************
     SCRIPT
     *****************************************************************************  -->
<script>
import TokenService from '../services/token.service'
import ApiService from '../services/api.service'

export default {
  data: () => ({
    user: {
      name: "",
      picture_url: ""
    }
  }),
  async mounted() {
    const gapi_plugin = document.createElement("script")
    gapi_plugin.setAttribute("src", "https://apis.google.com/js/platform.js")
    gapi_plugin.async = true
    gapi_plugin.defer = true
    gapi_plugin.onload = () => {
      window.gapi.load('auth2', function() {
        window.gapi.auth2.init();
      })
    }
    document.head.appendChild(gapi_plugin)

    const { data: user } = await ApiService.get('/user')
    this.user = user
  },
  methods: {
    signOut() {
      var self = this;
      window.gapi.auth2
      .getAuthInstance()
      .signOut()
      .then(() => {
        TokenService.remove_token()
        self.$router.push("/")
        console.log("signed out")
      })
    },
  }
}
</script>