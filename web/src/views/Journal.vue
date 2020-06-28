<!-- *****************************************************************************
     TEMPLATE
     *****************************************************************************  -->
<template>
  <v-data-table
    hide-default-header
    :headers="headers"
    :items="items"
    sort-by="record_date"
    :sort-desc="true"
    :mobile-breakpoint=0
  >
    <template v-slot:item.amount="{ item }">
      {{ Number(item.amount).toLocaleString('vi', {style : 'currency', currency : 'VND'}) }}
    </template>
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" width="800px" persistent>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" outlined>New Item</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span>Form</span>
              <v-spacer></v-spacer>
              <v-menu offset-y v-model="menu">
                <template v-slot:activator="{ on }">
                  <v-btn
                    v-on="on"
                    outlined
                    large
                  >{{ editedItem.record_date }}<v-icon right>mdi-calendar-blank</v-icon></v-btn>
                </template>
                <v-date-picker 
                  v-model="editedItem.record_date" 
                  no-title 
                  scrollable 
                  offset-y
                  :rules="[rules.required]"
                ></v-date-picker>
              </v-menu>
            </v-card-title>
            <v-card-text class="v-card__text">
              <v-form ref="form">
              <v-container>
                <v-row>
                  <v-col cols="12" md="8">
                    <v-text-field 
                      autofocus 
                      v-model="editedItem.name" 
                      label="Item" 
                      clearable 
                      append-icon="mdi-cart-outline" 
                      :rules="[rules.required]"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="4">
                    <v-select
                      v-model="editedItem.item_type" 
                      clearable
                      :items="item_types" 
                      :rules="[rules.required]"
                      item-text="name" 
                      return-object
                      append-icon="mdi-shape-outline" 
                      label="Type"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" md="3">
                    <v-text-field
                      class="text-right"
                      outlined
                      v-model="editedItem.amount" 
                      label="Amount" 
                      clearable
                      append-icon="mdi-cash"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="9">
                    <v-slider
                    v-model="editedItem.amount"
                    dense
                    thumb-label="always"
                    :thumb-size="48"
                    min="0"
                    max="100000"
                    ></v-slider>
                  </v-col>
                </v-row>
              </v-container>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="close">Cancel</v-btn>
              <v-btn text @click="save">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.action="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil-outline</v-icon>
      <v-icon small @click="deleteItem(item)">mdi-delete-outline</v-icon>
    </template>
  </v-data-table>
</template>
<!-- *****************************************************************************
     STYLE
     *****************************************************************************  -->
<style>
.v-dialog > .v-card > .v-card__text {
  padding-left: 0;
  padding-right: 0;
  padding-bottom: 0;
}
.v-slider--horizontal {
  padding-top: 60px;
}
</style>
<!-- *****************************************************************************
     SCRIPT
     *****************************************************************************  -->
<script>
import ApiService from '../services/api.service'

export default {
  data: () => ({
    headers: [
      { text: "Item", value: "name", align: "left", sortable: false },
      { text: "Type", value: "item_type.name", align: "left", sortable: false},
      { text: "Amount (Thousand VND)", value: "amount", align: "right", sortable: false},
      { text: "Date", value: "record_date", align: "left", sortable: false},
      { text: 'Actions', value: 'action', align: "right", sortable: false }
    ],
    item_types: [],
    items: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      item_type: "",
      amount: 12500,
      record_date: new Date().toISOString().substr(0,10)
    },
    defaultItem: {
      name: "",
      item_type: "",
      amount: 12500,
      record_date: new Date().toISOString().substr(0,10)
    },
    dialog: false,
    menu: false,
    rules: {
      required: value => !!value || "Required"
    }
  }),
  methods: {
    close () {
      this.dialog = false
      this.editedIndex = -1
      this.editedItem = Object.assign({}, this.defaultItem)
      this.$refs.form.resetValidation()
    },
    editItem (item) {
      this.editedIndex = this.items.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    // save() works for both editing and creating items
    // editedIndex=-1 which means we are creating a new
    // item because there was no item selected
    async save () {
      if (this.$refs.form.validate()) {
        const new_item = {
          name: this.editedItem.name.charAt(0).toUpperCase() + this.editedItem.name.slice(1),
          amount: this.editedItem.amount,
          record_date: this.editedItem.record_date, 
          item_type_id: this.editedItem.item_type.id
        }
        // this.editedIndex and this.editedItem will be reset 
        // to -1 and this.defaultItem when the form is closed
        const editedIndex = this.editedIndex
        const editedItem = this.editedItem
        if(this.editedIndex > -1) {
          const { status } = await ApiService.put('/items/'+this.editedItem.id, new_item)
          if (status===204) {
            // Object.assign(this.items[editedIndex], editedItem)
            this.items.splice(editedIndex, 1, editedItem)
          }
        } else {
          // the created item, which has an id,
          // should be pushed into items instead of the edited item
          const { status, data } = await ApiService.post("/items", new_item)
          if (status===201) {
            this.items.push(data)
          }
        }
        this.close()
      }
    },
    async deleteItem (item) {
      const index_to_delete = this.items.indexOf(item)
      const is_accepted = confirm('Are you sure you want to delete this item?')
      // splice() will also reindex the items array
      if (is_accepted) {
        const { status } = await ApiService.delete("/items/"+item.id)
        if (status===204) { 
          this.items.splice(index_to_delete, 1)
        }
      }
    }
  },
  async mounted() {
    const { data: items} = await ApiService.get('/items')
    this.items = items
    const { data: item_types } = await ApiService.get('/item-types')
    this.item_types = item_types
  },
  watch: {
    dialog (val) {
      // call close() when the dialog is closed.
      val || this.close()
    },
  },
}
</script>