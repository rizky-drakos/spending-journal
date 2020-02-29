<template>
  <v-app id="inspire">

    <v-navigation-drawer
      expand-on-hover
      permanent
      app
      v-if="this.$route.path !== '/login' && this.$route.path !== '/'"
    >
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/40.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title>John Leider</v-list-item-title>
      </v-list-item>

      <v-divider></v-divider>
      <v-list>

        <v-list-item to="journal">
          <v-list-item-action>
            <v-icon>mdi-calendar-text-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>JOURNAL</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item to="dashboard">
          <v-list-item-action>
            <v-icon>mdi-chart-bar</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>DASHBOARD</v-list-item-title>
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
            <v-list-item-title>SIGN OUT</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <v-content app>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-content>

  </v-app>
</template>

<script>
import AutheticationStore from './stores/AuthenticationStore'

  export default {
    methods: {
      signOut() {
        // window.gapi could be undefined if Login is
        // loaded after Home, because Home is also
        // responsible for window.gapi initialization
        var self = this
        window.gapi.auth2.getAuthInstance().signOut().then(() => {
          AutheticationStore.data.isAuthenticated = false
          self.$router.push("/")
        });
      }
    }
  }
</script>