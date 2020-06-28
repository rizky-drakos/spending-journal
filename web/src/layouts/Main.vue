<!-- *****************************************************************************
     TEMPLATE
     *****************************************************************************  -->
<template>
  <v-app>
    <v-app-bar
      app
      color="deep-purple"
      dark
      clipped-left
      prominent
      shrink-on-scroll
      scroll-threshold="5"
      src="https://i.picsum.photos/id/882/1920/1080.jpg?hmac=FCDToSVP5kHJLp0mnIaRatU0lH3ivaZ2GaSCuOzz2uU"
    >
      <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Spending Journal</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-avatar>
          <v-img :src="user.picture_url"></v-img>
        </v-avatar>
      </v-btn>
      <!-- debt -->
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
        ></v-img>
      </template>
    </v-app-bar>
    <v-navigation-drawer clipped app width="130" v-model="drawer">
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
      picture_url: "",
    },
    drawer: true
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