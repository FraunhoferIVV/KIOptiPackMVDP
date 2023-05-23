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
    methods: {
        loadTable(table : TableType) {
            this.loading = true
            this.changedItems = []
            //
            this.headers = table.headers as Header[]
            this.editableHeaders = table.headers.map(header => Object.assign({}, header)) // copy original table headers
            if (this.headers.length == 0 || this.headers[this.headers.length - 1].text != "Operation")
                this.headers.push({text: "Operation", value: "operation"})
            //
            this.items = table.items as Item[]
            this.currentId = 0
            for (let i = 0; i < this.items.length; i++) {
                this.items[i].id = this.currentId++
            }
            //
            this.loading = false
        }
    },
    mounted() { 
        this.loadTable(this.table)
    },
    watch: {
        table(newTable : TableType, oldTable : TableType) {
            this.loadTable(newTable)
        }
    },
    setup(props) {
        // datastructure for the future emit
        // save only added/edited/deleted Items (rows)
        let changedItems: Item[] = [] 

        // reactive data
        let currentId = 0
        const headers = ref([] as Header[])
        const items = ref([] as Item[])
        
        const editableHeaders = ref([] as Header[])
        // const itemsSelected = ref([] as Item[])
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
            Object.assign(editingItem, row)
        }

        const submitEdit = () => {
            isEditing.value = false;
            const item : Item = items.value.find((item) => item.id === editingItem.id) || editingItem // default value for typescript to calm down
            Object.assign(item, editingItem)
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
            console.log(changedItems)
        }
        

        // todo
        const discardChanges = () => {
            // request to load the original table again (almost the same as reload)

        }

        // todo: sum up all the changes with the same id
        const manageChanges = () => {

        }

        // todo
        const confirmChanges = () => {
            manageChanges()
            // emit changedItems
            // changes overview ?

        }

        
        console.log('EditTable component: Setup completed')
        
        return {
            headers, items, 
            editableHeaders, currentId,
            loading, 
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
        <div v-for="(header, index) in editableHeaders" :key="index">
            <p> {{ header.text }} <input type="text" v-model="editingItem[header.value]" /> </p>
        </div>
        <button @click="submitEdit">ok</button>
    </div>


</template>

<style scoped>
</style>