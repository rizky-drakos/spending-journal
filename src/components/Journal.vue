<template>
      <v-data-table
          :headers="headers"
          :items="items"
          sort-by="record_date"
          :sort-desc="true">

      </v-data-table>
</template>

<script>
import axios from 'axios';

  export default {
    data: () => ({
      headers: [
        { text: "Item", value: "name", align: "left", sortable: false },
        { text: "Type", value: "item_type_id", align: "center", sortable: false},
        { text: "Date", value: "record_date", align: "center", sortable: false},
        { text: "Amount (in thousand VND)", value: "amount", align: "center", sortable: false}        
      ],
      items: [],
    }),
    mounted() {
      axios.get('http://localhost:5000/items')
      .then(response => {
        this.items = response.data;
      })
    }
  }
</script>