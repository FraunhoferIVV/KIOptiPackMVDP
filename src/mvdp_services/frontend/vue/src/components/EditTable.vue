<script lang="ts">
import { defineComponent, ref, reactive} from 'vue';
import type { PropType } from 'vue';

import Vue3EasyDataTable from 'vue3-easy-data-table';
import type { Header, Item } from "vue3-easy-data-table";
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
    components: {
        'EasyDataTable': Vue3EasyDataTable
    },
    setup(props) {
        // datastructure for the future emit
        // save only edited or deleted Items (rows)
        let changedItems: Item[] = [] 

        // reactive data
        const headers = ref(props.table.headers as Header[])
        const itemsSelected = ref([] as Item[])
        const items = ref([] as Item[])
        const loading = ref(true)
        const isEditing = ref(false)
        const editingItem = reactive({
            Sensor1: "",
            Sensor2: "",
            id: 0
        })
        // mini loading: useless feature
        setTimeout(() => {
            // making items reactive as soon as possible
            items.value = props.table.items as Item[]
            loading.value = false
        }, 300)
        
        // methods
        const deleteItem = (row : Item) => {
            items.value = items.value.filter((item) => item.id !== row.id)
            changedItems.push(row)
        }
        
        
        console.log('EditTable component: Setup completed')
        
        return {
            headers, items, loading,
            isEditing, editingItem,
            // editItem, submitEdit, deleteItem,
            changedItems
        }
    }
})


</script>


<template>
    <EasyDataTable
        :headers="headers"
        :items="items"
        :loading="loading"
        show-index
        fixed-index
        alternating
        border-cell
        buttons-pagination
    >
        <template #loading>
            <img src="@/assets/ivv-logo.png" alt="" style="float: right;">
        </template>
        <!--
        <template #item-operation="item">
            <div class="operation-wrapper">
                <img
                src="./images/delete.png"
                class="operation-icon"
                @click="deleteItem(item)"
                />
                <img
                src="./images/edit.png"
                class="operation-icon"
                @click="editItem(item)"
                />
            </div>
        </template>
        -->
        
    </EasyDataTable>

    <!--
    <div class="edit-ite/edit_data
        Sensor1:<input type="text" v-model="editingItem.height" />
        <br />
        Sensor2:<input type="text" v-model="editingItem.weight" />
        <br />
        <button @click="submitEdit">ok</button>
        
    </div>
    -->
</template>

<style scoped>
</style>