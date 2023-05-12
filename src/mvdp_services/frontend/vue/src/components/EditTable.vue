<script lang="ts">
import { defineComponent} from 'vue';
import type { PropType } from 'vue';
import Vue3EasyDataTable from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';

import type TableType from '@/types/TableType';

// using vue3-easy-data-table
export default defineComponent({
    props: {
        table: {
            required: true,
            type: Object as PropType<TableType>
        }
    },
    mounted() {
        console.log(this.table)
    },
    components: {
        'EasyDataTable': Vue3EasyDataTable
    },
    data() {
        return {
            
        }
    },
    computed: {
    },
    methods: {
    }
})

/* 
table example
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
            return table
*/

</script>


<template>
    <EasyDataTable
        :headers="table.headers"
        :items="table.items"
        show-index
        alternating
        border-cell
        buttons-pagination
    />
</template>

<style scoped>
</style>