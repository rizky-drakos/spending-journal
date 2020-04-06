<template>
    <v-row justify="center">
          <v-col cols="5">
              <v-data-table
                hide-default-header
                :headers="headers"
                :items="cost_by_item_types"
                sort-by="name"
              >
                <template v-slot:top>
                  <h2>Total: {{ total }}</h2>
                </template>
              </v-data-table>
          </v-col>
          <v-col cols="3" text-align="center">
            <v-date-picker v-model="month_of_year" type="month"></v-date-picker>
          </v-col>
    </v-row>
</template>

<script>
import ApiService from '../services/api.service'

export default {
  mounted () {
    this.fetch_cost_by_item_types()
  },
  data: () => ({
    headers: [
      { text: "Item Type", value: "name", align: "left", sortable: false },
      { text: "Cost", value: "cost", align: "right", sortable: false }
    ],
    month_of_year: new Date().toISOString().substr(0, 7),
    year: new Date().toISOString().substr(0, 4),
    month: new Date().toISOString().substr(5, 2),
    cost_by_item_types: [],
    total: 0
  }),
  methods: {
    async fetch_cost_by_item_types () {
      const { data: cost_by_item_types } = await ApiService.post(
        "/cost-by-item-types",
        { year: this.year, month: this.month }
      )
      this.cost_by_item_types = cost_by_item_types.map(
        item => ({...item, cost: item["cost"].toLocaleString('vi', {style : 'currency', currency : 'VND'})})
      )
      this.total = cost_by_item_types.map(item => item["cost"]).reduce((current, next) => current + next).toLocaleString('vi', {style : 'currency', currency : 'VND'})
    }
  },
  watch: {
    month_of_year (value) {
      this.year = value.substr(0, 4)
      this.month = value.substr(5, 2)
      this.fetch_cost_by_item_types()
    }
  }
}

</script>