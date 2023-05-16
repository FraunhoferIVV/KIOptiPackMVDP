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
        table: {headers: [], items: []}
    }
  },

  methods: {
      fetchTable: async function () {
          axios({
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
      }
  }
})
</script>

<template>
    <EditTable :table="table"/>
</template>

<style scoped>

</style>