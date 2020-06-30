<template>
  <v-row justify="center">
    <v-col>
      <v-data-table
        hide-default-header
        hide-default-footer
        :headers="headers"
        :items="item_types"
        sort-by="name"
        :mobile-breakpoint=0
      >
        <template v-slot:top>
          <v-toolbar flat color="white">
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" width="400px">
              <template v-slot:activator="{ on }">
                <v-btn v-on="on" outlined>New Item</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span>Form</span>
                </v-card-title>
                <v-card-text>
                  <v-form ref="form">
                  <v-container>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field autofocus label="Item Type" 
                        v-model="editedItemType.name" clearable 
                        outlined append-icon="mdi-shape-outline" 
                        dense :rules="[rules.required]"></v-text-field>
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
    </v-col>
  </v-row>
</template>

<script>
import ApiService from '../services/api.service'

export default {
  data: () => ({
    headers: [
      { text: "Item Type", value: "name", align: "left", sortable: false },
      { text: 'Actions', value: 'action', align: "right", sortable: false }      
    ],
    item_types: [],
    dialog: false,
    editedIndex: -1,
    editedItemType: {
      name: ""
    },
    defaultItemType: {
      name: ""
    },
    rules: {
      required: value => !!value || "Required"
    }
  }),
  async mounted() {
    const { data: item_types } = await ApiService.get("/item-types")
    this.item_types = item_types
  },
  methods: {
    close () {
      this.dialog = false
      this.editedIndex = -1
      this.editedItemType = Object.assign({}, this.defaultItemType)
      this.$refs.form.resetValidation()
    },
    async save () {
      if (this.$refs.form.validate()) {
        const new_item_type = {
          name: this.editedItemType.name.toUpperCase(),
        }
        const editedIndex = this.editedIndex
        const editedItemType = this.editedItemType
        if (this.editedIndex > -1) {
          const { status } = await ApiService.put("/item-types/"+this.editedItemType.id, new_item_type)
          if (status===204) {
            Object.assign(this.item_types[editedIndex], editedItemType)
          }
        } else {
          const { status, data } = await ApiService.post("/item-types", new_item_type)
          if (status===201) {
            this.item_types.push(data)
          }
        }
        this.close()
      }
    },
    editItem (item_type) {
      this.editedIndex = this.item_types.indexOf(item_type)
      this.editedItemType = Object.assign({}, item_type)
      this.dialog = true
    },
    async deleteItem (item_type) {
      const index_to_delete = this.item_types.indexOf(item_type)
      const is_accepted = confirm('Are you sure you want to delete this item type?')
      // splice() will also reindex the item typess array
      if (is_accepted) {
        const { status } = await ApiService.delete("/item-types/"+item_type.id)
        if (status===204) {
          this.item_types.splice(index_to_delete, 1)
        }
      }
    }
  }
}
</script>