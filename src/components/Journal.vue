<template>
      <v-data-table
          hide-default-header
          :headers="headers"
          :items="items"
          sort-by="record_date"
          :sort-desc="true">
          <template v-slot:top>
            <v-toolbar flat color="white">
              <v-spacer></v-spacer>
              <v-dialog v-model="dialog" width="800px">
                <template v-slot:activator="{ on }">
                  <v-btn v-on="on" outlined>New Item</v-btn>
                </template>
                <v-card >
                  <v-card-title>
                    <span>Form</span>
                  </v-card-title>
                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12" md="3">
                          <v-text-field autofocus v-model="editedItem.name" label="Item" clearable outlined append-icon="mdi-cart-outline" dense></v-text-field>
                        </v-col>
                        <v-col cols="12" md="3">
                          <v-select
                            v-model="editedItem.item_type"
                            dense
                            :items="item_types"
                            outlined
                            item-text="name"
                            return-object
                            append-icon="mdi-shape-outline"
                            label="Type">
                          </v-select>
                        </v-col>
                        <v-col cols="12" md="3">
                            <v-menu offset-y v-model="menu">
                              <template v-slot:activator="{ on }">
                                <v-text-field 
                                  v-on="on" 
                                  v-model="editedItem.record_date" 
                                  label="Date" 
                                  readonly
                                  append-icon="mdi-calendar-today"
                                  outlined dense>
                                </v-text-field>
                              </template>
                              <v-date-picker 
                                v-model="editedItem.record_date" 
                                no-title scrollable offset-y>
                              </v-date-picker>
                            </v-menu>
                        </v-col>
                        <v-col cols="12" md="3">
                          <v-text-field type="number" v-model="editedItem.amount" label="Amount" clearable outlined append-icon="mdi-currency-usd" dense></v-text-field>
                        </v-col>
                      </v-row>
                    </v-container>
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
            <v-icon
              small
              class="mr-2"
              @click="editItem(item)"
            >
              mdi-pencil-outline
            </v-icon>
            <v-icon
              small
              @click="deleteItem(item)"
            >
              mdi-delete-outline
            </v-icon>
        </template>
      </v-data-table>
</template>

<script>
import axios from 'axios';

  export default {
    data: () => ({
      headers: [
        { text: "Item", value: "name", align: "left", sortable: false },
        { text: "Type", value: "item_type.name", align: "left", sortable: false},
        { text: "Amount (Thousand VND)", value: "amount", align: "left", sortable: false},
        { text: "Date", value: "record_date", align: "left", sortable: false},
        { text: 'Actions', value: 'action', align: "right", sortable: false }
      ],
      item_types: [],
      items: [],
      editedIndex: -1,
      editedItem: {
        name: "",
        item_type: {},
        amount: "",
        record_date: ""
      },
      defaultItem: {
        name: "",
        item_type: "",
        amount: "",
        record_date: ""
      },
      dialog: false,
      menu: false,
    }),
    methods: {
      close () {
        this.dialog = false
        this.editedIndex = -1
        this.editedItem = Object.assign({}, this.defaultItem)
      },
      editItem (item) {
        this.editedIndex = this.items.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },
      // save() works for both editing and creating items
      // editedIndex=-1 which means we are creating a new
      // item because there was no item selected
      save () {
        const new_item = {
          name: this.editedItem.name,
          amount: this.editedItem.amount,
          record_date: this.editedItem.record_date, 
          item_type_id: this.editedItem.item_type.id
        }
        // this.editedIndex and this.editedItem will be reset 
        // to -1 and this.defaultItem when the form is closed
        const editedIndex = this.editedIndex
        const editedItem = this.editedItem
        if(this.editedIndex > -1) {
          axios.put('http://192.168.1.105:5000/items/'+this.editedItem.id, new_item).then(() => {
            Object.assign(this.items[editedIndex], editedItem)
          })
          Object.assign(this.items[editedIndex], this.editedItem)
        } else {
          axios.post('http://192.168.1.105:5000/items', new_item).then(({ data }) => {
            // should push the created item which has an id,
            // instead of edited item, into items
            this.items.push(data)
          })
        }
        this.close()
      },
      deleteItem (item) {
        const index_to_delete = this.items.indexOf(item)
        confirm('Are you sure you want to delete this item?') && 
        // splice() will also reindex the items array
        axios.delete("http://192.168.1.105:5000/items/"+item.id).then(() => {
          this.items.splice(index_to_delete, 1)
        })
      }
    },
    mounted() {
      axios.get('http://192.168.1.105:5000/items')
      .then(response => {
        this.items = response.data
      }), 
      axios.get('http://192.168.1.105:5000/item-types')
      .then(response => {
        this.item_types = response.data;
      })
    },
    watch: {
      dialog (val) {
        // call close() when the dialog is closed.
        val || this.close()
      }
    },
  }
</script>