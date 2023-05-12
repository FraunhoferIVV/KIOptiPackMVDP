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

</script>

<script setup lang="ts">

</script>

<template>
    <EasyDataTable
        :headers="table.headers"
        :items="table.items"
    />
</template>

<style scoped>
</style>