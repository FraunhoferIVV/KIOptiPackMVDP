<script lang="ts">
import {defineComponent} from 'vue';

import type {Header, Item} from "vue3-easy-data-table";

import EditTable from '@/components/EditTable.vue'
import type TableType from '@/types/TableType';
import type MessageType from '@/types/MessageType'
import axios from "axios";
import {constants} from "@/constants";


export default defineComponent({
  components: {
    EditTable
  },
  mounted() {
    this.fetchTable()
  },
  data() {
    return {
      editMessage: {
        content: 'table loaded',
        type: 'info' as MessageType
      },
      table: {headers: [] as Header[], items: [] as Item[]}
    }
  },

  methods: {
      fetchTable: async function () {
        // the true code for table fetching
        /* 
          await axios({
              method: 'get',
              url: constants.restBaseUrl + 'api/table/data',
              timeout: 5000
          }).then((res) => {
              const headers: Header[] = res.data.headers
              const items: Item[] = res.data.items
              this.table = {headers: headers, items: items}
              console.log(this.table);

          }, (error) => {
              console.log('Can not establish connection to server to update table')
              console.log(error)
          })
        */
          // the following code is just for testing of the edit-table component; remove that code soon!
        
            const headers : Header[] = [
                      { text: "Sensor1", value: 's1'},
                      { text: "Sensor2", value: 's2'}
                  ]
            const items : Item[] = [
                      { s1: 1, s2: 2},
                      { s1: 3, s2: 4}
                  ]
            this.table = {headers: headers, items: items}
            console.log('Test table: ')
            console.log(this.table)
         
      }
  }
})
</script>

<template>
    <EditTable :table="table"/>
</template>

<style scoped>

</style>