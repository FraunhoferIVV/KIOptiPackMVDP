<script lang="ts">
import { defineComponent, defineEmits, ref, reactive} from 'vue';
import type { PropType} from 'vue';

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
    emits: ['changeTable'],
    components: {
        'EasyDataTable': Vue3EasyDataTable
    },
    created() { 
        this.loadTable()
    },
    watch: {
        table(newTable : TableType, oldTable : TableType) {

            this.loadTable()
        }
    },
    setup(props, { emit }) {
        // datastructure for the future emit
        // save only added/edited/deleted Items (rows)
        let changedItems: Item[] = [] 

        // reactive data
        let currentId = ref(0)
        const headers = ref([] as Header[])
        const items = ref([] as Item[])
        
        const editableHeaders = ref([] as Header[])
        // const itemsSelected = ref([] as Item[])
        const loading = ref(true)
        const isEditing = ref(false)
        const isAdding = ref(false)
        const editingItem = reactive({} as Item) // use header values as properties

        
        // methods
        const loadTable = () => {
            console.log("Loading table: drop index and all changes down")
            const table = props.table
            loading.value = true
            changedItems = []
            //
            headers.value = table.headers as Header[]
            editableHeaders.value = table.headers.map(header => Object.assign({}, header)) // make a copy of table headers
            if (editableHeaders.value.length == 0 || editableHeaders.value[editableHeaders.value.length - 1].text == "Operation") // remove operations only for editableItems
                editableHeaders.value.pop()
            if (headers.value.length == 0 || headers.value[headers.value.length - 1].text != "Operation")
                headers.value.push({text: "Operation", value: "operation"})
            //
            items.value = table.items as Item[]
            currentId.value = 0
            
            for (let i = 0; i < items.value.length; i++) {
                items.value[i].id = currentId.value++
            }
            //
            loading.value = false
        }

        const deleteItem = (row : Item) => {
            isEditing.value = false;
            items.value = items.value.filter((item) => item.id !== row.id)
            saveChange(row, "DELETE")
        }

        // todo: find a better interface for row editing
        const editItem = (row : Item) => {
            isAdding.value = false
            isEditing.value = true;
            Object.assign(editingItem, row)
        }

        const submitEdit = () => {
            isEditing.value = false;
            const item : Item = items.value.find((item) => item.id === editingItem.id) || editingItem // default value for typescript to calm down
            // Object.assign(item, editingItem)
            copyInput(item)
            saveChange(editingItem, "EDIT")
        }

        const copyInput = (to : Item) => {
            for (let key in editingItem) {
                if (!isNaN(+editingItem[key]))
                    to[key] = +editingItem[key]
                else
                    to[key] = editingItem[key]
            }
        }
        
        const addItem = () => {
            isAdding.value = true   
            Object.keys(editingItem).forEach(key => delete editingItem[key])
        }

        const submitAdd = () => {
            isAdding.value = false
            const newItem = {id: currentId.value++} as Item
            // Object.assign(newItem, editingItem)
            copyInput(newItem)
            items.value.push(newItem)
            saveChange(editingItem, "ADD")
        }

        const cancelEditAdd = () => {
            isEditing.value = isAdding.value = false;
        }

        const saveChange = (row : Item, changeType : String) => {
            // remove overhead from row and add changeType
            let resultRow = {changeType: changeType} as Item
            Object.assign(resultRow, row)
            delete resultRow.id
            delete resultRow.index
            delete resultRow.key
            changedItems.push(resultRow as Item)
        }
        
        const discardChanges = () => {
            // simply reload the original table (changes are deleted when loading)
            loadTable()
        }

        // todo: sum up all the changes with the same id
        const manageChanges = () => {

        }

        // todo
        const confirmChanges = () => {
            manageChanges()
            emit('changeTable', changedItems)
        }

        
        console.log('EditTable component: Setup completed')
        
        return {
            headers, items, 
            editableHeaders, currentId,
            loading, 
            isEditing, isAdding, editingItem,
            changedItems, emit,
            loadTable,
            editItem, submitEdit,
            addItem, submitAdd,
            cancelEditAdd, saveChange,
            deleteItem, 
            discardChanges, confirmChanges,
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
        <p> Editing row </p>
        <div v-for="(headerItem, index) in editableHeaders" :key="index">
            <p> {{ headerItem.text }} <input type="text" v-model="editingItem[headerItem.value]" /> </p>
        </div>
        <button @click="cancelEditAdd">Cancel</button>
        <button @click="submitEdit">OK</button>
    </div>
    

    <div class="edit-item" v-if="isAdding">
        <p> Adding row </p>
        <div v-for="(headerItem, index) in editableHeaders" :key="index">
            <p> {{ headerItem.text }} <input type="text" v-model="editingItem[headerItem.value]" /> </p>
        </div>
        <button @click="cancelEditAdd">Cancel</button>
        <button @click="submitAdd">OK</button>      
    </div>
    
    <div v-if="!isEditing && !isAdding">
        <button @click="addItem">Add row</button>
        <button @click="discardChanges">Discard changes</button>
        <button @click="confirmChanges">Confirm changes</button>
    </div>

</template>

<style scoped>
</style>