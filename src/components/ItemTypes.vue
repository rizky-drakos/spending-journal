<template>
      <v-data-table
        hide-default-header
        :headers="headers"
        :items="item_types"
        hide-default-footer>
      </v-data-table>
</template>

<script>
import axios from 'axios'
import { TokenService } from '../services/token.service'

  export default {
    data: () => ({
      headers: [
        { text: "Item Type", value: "name", align: "left", sortable: false },      
      ],
      item_types: [],
    }),
    mounted() {
      axios.get('http://192.168.1.100:5000/item-types', {
        headers: {
          "Authorization": `Bearer ${TokenService.get_token()}`
        }
      })
      .then(response => {
        this.item_types = response.data;
      })
    }
  }
</script>