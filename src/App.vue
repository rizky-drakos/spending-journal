<template>
  <v-app id="inspire">

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Spending Journal</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list>

        <v-list-item link to="/">
          <v-list-item-action>
            <v-icon>mdi-calendar-text-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>JOURNAL</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="dashboard">
          <v-list-item-action>
            <v-icon>mdi-chart-bar</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>DASHBOARD</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="item-types">
          <v-list-item-action>
            <v-icon>mdi-shape-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>ITEM TYPES</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <v-content>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-content>

  </v-app>
</template>

<script>
  export default {
    data: () => ({
      drawer: true,

    })
  }
</script>