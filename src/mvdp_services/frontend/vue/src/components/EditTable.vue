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
        const editingItem = reactive({
            Sensor1: "",
            Sensor2: "",
            id: 0
        })
        
        // methods
        const deleteItem = (row : Item) => {
            isEditing.value = false;
            items.value = items.value.filter((item) => item.id !== row.id)
            saveChange(row, "DELETE")
        }

        // todo: find and edit directly the item in table
        const editItem = (row : Item) => {
            isEditing.value = true;
            const {Sensor1, Sensor2, id} = row
            editingItem.Sensor1 = Sensor1
            editingItem.Sensor2 = Sensor2
            editingItem.id = id
        }

        const submitEdit = () => {
            isEditing.value = false;
            const item = items.value.find((item) => item.ide === editingItem.id) as Item;
            item.Sensor1 = editingItem.Sensor1
            item.Sensor2 = editingItem.Sensor2
            saveChange(editingItem, "EDIT")
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
            console.log('changed[]: ', changedItems[0])
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
        console.log(props.table)
        
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
        Sensor1:<input type="text" v-model="editingItem.Sensor1" />
        <br />
        Sensor2:<input type="text" v-model="editingItem.Sensor2" />
        <br />
        <button @click="submitEdit">ok</button>
    </div>
    </template>

<style scoped>
</style>