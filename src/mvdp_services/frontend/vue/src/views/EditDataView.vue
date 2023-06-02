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
      table: {headers: [] as Header[], items: [] as Item[]},
    }
  },

  methods: {
      fetchTable: async function () {
        // the true code for table fetching
         
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
        });

        (this.$refs.table as any).blockTable();
        await (this.$refs.table as any).checkUpdate(this.table).then((res : boolean) => {
          (this.$refs.table as any).loadTable()
        })
        
      },
      handleChanges: async function (changedItems : Item[]) {
        let formData = new FormData()
        formData.append('changed_items', JSON.stringify(changedItems))
        await axios({
              method: 'put',
              url: constants.restBaseUrl + 'api/change_data',
              data: formData,
              timeout: 5000
          }).then((res) => {
              console.log('Changes accomplished');
          }, (error) => {
              console.log('Can not establish connection to server to update data with changes')
              console.log(error)
          })

        this.fetchTable() // update table with current changes for child components
      }
  },
})
</script>

<template>
    <EditTable 
      ref="table"
      :table="table"
      @changeTable="handleChanges"
    />
</template>

<style scoped>

</style>