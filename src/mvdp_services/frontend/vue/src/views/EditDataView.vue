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
    this.loadEditConfig()
  },
  data() {
    return {
      tableReadonly: true,
      editMessage: {
        content: '',
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

        // reload the table from the child comonent
        (this.$refs.table as any).loadTable()
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

        console.log('here')
        // wait until all changes are applied on the database
        setTimeout(() => {
          this.fetchTable() // update table with current changes for child components
        }, 500)
      },
      loadEditConfig: async function () {
        await axios({
              method: 'get',
              url: constants.restBaseUrl + 'api/config/table_readonly',
              timeout: 3000
          }).then((res) => {
              this.tableReadonly = res.data;
              console.log('Upload config loaded');
              if (this.tableReadonly) {
                  this.editMessage.content = 'The table is read only!'
                  this.editMessage.type = 'warning'
              }  
          }, (error) => {
              console.log('Can not establish connection to server to get upload config')
              console.log(error)
          })
      }
  },
})
</script>

<template>
    <EditTable 
      ref="table"
      :table="table"
      :tableReadonly="tableReadonly"
      @changeTable="handleChanges"
    />
</template>

<style scoped>

</style>