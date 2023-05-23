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
    watch: {
        table(newTable : TableType, oldTable : TableType) {
            this.headers = newTable.headers as Header[]
            if (this.headers.length == 0 || this.headers[this.headers.length - 1].text != "Operation")
                this.headers.push({text: "Operation", value: "operation"})
            //
            this.items = newTable.items as Item[]
            for (let i = 0; i < this.items.length; i++) {
                this.items[i].id = i
            }
            //
            this.loading = false
            console.log(this.table)
        }
    },
    setup(props) {
        // datastructure for the future emit
        // save only edited or deleted Items (rows)
        let changedItems: Item[] = [] 

        // reactive data
        const headers = props.table.headers as Header[]  
        if (headers.length == 0 || headers[headers.length - 1].text != "Operation")
                headers.push({text: "Operation", value: "operation"})

        const items = ref(props.table.items as Item[])
        for (let i = 0; i < items.value.length; i++) {
        }

        const itemsSelected = ref([] as Item[])
        const loading = ref(items.value.length == 0)
        const isEditing = ref(false)
        const editingItem = reactive({} as Item) // use header values as properties
        
        // methods
        const deleteItem = (row : Item) => {
            isEditing.value = false;
            items.value = items.value.filter((item) => item.id !== row.id)
            saveChange(row, "DELETE")
        }

        // todo: find a better interface for row editing
        const editItem = (row : Item) => {
            isEditing.value = true;
            editingItem.s1 = row.s1
            editingItem.s2 = row.s2
            editingItem.id = row.id
        }

        const submitEdit = () => {
            isEditing.value = false;
            const item : Item = items.value.find((item) => item.id === editingItem.id) || editingItem // default value for typescript to calm down
            console.log(item)
            item.s1 = editingItem.s1
            item.s2 = editingItem.s2
            saveChange(editingItem, "EDIT")
            console.log(item)
        }
        
        // todo
        const addItem = () => {

        }

        // todo
        const submitAdding = () => {

        }

        const saveChange = (row : Item, changeType : String) => {
            // remove overhead from row and add changeType
            delete row.id
            delete row.index
            delete row.key
            row.changeType = changeType
            changedItems.push(row as Item)
        }
        

        // todo
        const discardChanges = () => {
            // request to load the original table again (almost the same as reload)

        }

        // todo
        const confirmChanges = () => {
            // emit changedItems
            // changes overview ?

        }

        
        console.log('EditTable component: Setup completed')
        
        return {
            headers, items, loading,
            isEditing, editingItem,
            editItem, submitEdit, deleteItem, saveChange,
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
        alternating
        border-cell
        buttons-pagination
    >
        <template #loading>
            <img src="@/assets/ivv-logo.png" alt="" style="float: right;">
        </template>
        
        <template #item-operation="item">
            <div class="operation-wrapper">
                <img
                src="@/assets/delete.png"
                class="operation-icon"
                @click="deleteItem(item)"
                />
                <img
                src="@/assets/edit.png"
                class="operation-icon"
                @click="editItem(item)"
                />
            </div>
        </template>
                
    </EasyDataTable>

    
    <div class="edit-item" v-if="isEditing">
        Sensor1:<input type="text" v-model="editingItem.s1" />
        <br />
        Sensor2:<input type="text" v-model="editingItem.s2" />
        <br />
        <button @click="submitEdit">ok</button>
    </div>
    </template>

<style scoped>
</style>