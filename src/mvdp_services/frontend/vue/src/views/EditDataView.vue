<script lang="ts">
import { defineComponent } from 'vue';

import type { Header, Item } from "vue3-easy-data-table";

import EditTable from '@/components/EditTable.vue'
import type TableType from '@/types/TableType';
import type MessageType from '@/types/MessageType'



    export default defineComponent({
        components: {
            EditTable
        },
        data() {
            return {
                editMessage: {
                    content: 'talbe loaded',
                    type: 'info' as MessageType
                }
            }
        },
        methods: {
            fetchTable() {
                // fetch table from server

                // just an example
                const headers : Header[] = [
                    { text: "Sensor1", value: 's1'},
                    { text: "Sensor2", value: 's2'}
                ]
                const items : Item[] = [
                    { s1: 1, s2: 2},
                    { s1: 3, s2: 4}
                ]
                const table = {
                    headers: headers,
                    items: items,
                }
                // example end
                return table
            }
        }
    })
</script>

<template>
    <EditTable :table="fetchTable()"/>
</template>

<style scoped>

</style>