<script lang="ts">
import { defineComponent, defineEmits, ref, reactive} from 'vue';
import type { PropType} from 'vue';

import Vue3EasyDataTable from 'vue3-easy-data-table';
import type { Header, Item } from "vue3-easy-data-table";
import 'vue3-easy-data-table/dist/style.css';

import type TableType from '@/types/TableType';
import type ChangesDictionaryType from '@/types/ChangesDictionaryType';

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
    setup(props, { emit }) {
        // datastructure for the future emit
        // save only added/edited/deleted Items (rows)
        let changedItems: Item[] = [] 

        // reactive data
        let currentId = ref(0)
        const headers = ref([] as Header[])
        const items = ref([] as Item[])
        
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
            headers.value = table.headers.map(header => Object.assign({}, header)) // make a copy of table headers
            headers.value.unshift({text: "Operation", value: "operation"}) // operation overhead for headers
            // create id for each table item
            currentId.value = 0
            for (const item of table.items) {
                item.id = currentId.value++
            }
            //
            items.value = table.items.map(item => Object.assign({}, item)) // make a copy of table items
            
            //
            loading.value = false
        }

        const deleteItem = (itemId : number) => {
            let row = items.value.find((item) => item.id === itemId) as Item
            items.value = items.value.filter((item) => item.id !== itemId)
            console.log(row)
            saveChange(row, "DELETE")
            cancelEditAdd() // enable editingItem to be deleted
        }

        const editItem = (row : Item) => {
            cancelEditAdd()
            isEditing.value = true;
            Object.assign(editingItem, row)
        }

        const submitEdit = () => {
            isEditing.value = false;
            const item : Item = items.value.find((item) => item.id == editingItem.id) || editingItem // default value for typescript to calm down
            // Object.assign(item, editingItem)
            copyInput(item)
            saveChange(item, "EDIT")
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
            cancelEditAdd() 
            isAdding.value = true   
            editingItem.id = currentId.value++
            items.value.push(editingItem)
        }

        const submitAdd = () => {
            isAdding.value = false
            const newItem = {id: currentId.value++} as Item
            // Object.assign(newItem, editingItem)
            copyInput(newItem)
            items.value.pop()
            items.value.push(newItem)
            saveChange(newItem, "ADD")
        }

        const submit = () => {
            if (isEditing.value) {
                submitEdit()
            } else if (isAdding.value) {
                submitAdd()
            }
        }

        const cancelEditAdd = () => {
            if (isAdding.value) {
                items.value.pop()
            }
            isEditing.value = isAdding.value = false;
            Object.keys(editingItem).forEach(key => delete editingItem[key]) // important for adding
        }

        const saveChange = (row : Item, changeType : String) => {
            // remove overhead from row and add changeType
            // create resultRow with all empty fields and changeType
            let resultRow = {changeType: changeType} as Item
            for (const header of props.table.headers) {
                resultRow[header.text] = ''
            }
            // overwrite non empty fields
            Object.assign(resultRow, row)
            // delete overhead except of id
            delete resultRow.index
            delete resultRow.key
            // save resultRow as item ready for future managing
            changedItems.push(resultRow as Item)
        }
        
        const discardChanges = () => {
            // simply reload the original table (changes are deleted when loading)
            cancelEditAdd()
            loadTable()
        }

        // one change per id (also removes ids)
        const manageChanges = () => {
            let changesDictionary : ChangesDictionaryType = {} as ChangesDictionaryType
            for (const item of changedItems as Item[]) {
                const id = item.id as number
                delete item.id
                if (!changesDictionary.hasOwnProperty(id)) {
                    changesDictionary[id] = item
                    continue
                }
                // else: this item has already been changed before
                let savedItem = changesDictionary[id]
                // 1: ADD -> *
                if (savedItem.changeType == 'ADD') { 
                    if (item.changeType == 'ADD') {
                        throw new Error('id reused!')
                        return []
                    } else if (item.changeType == 'EDIT') {
                        item.ChangeType = 'ADD'
                        changesDictionary[id] = Object.assign({}, item)
                    } else if (item.changeType == 'DELETE') {
                        delete changesDictionary[id]
                    }
                }
                // 2: EDIT -> *
                if (savedItem.changeType == 'EDIT') { 
                    if (item.changeType == 'ADD') {
                        throw new Error('id reused!')
                        return []
                    } else if (item.changeType == 'EDIT') {
                        changesDictionary[id] = Object.assign({}, item)
                    } else if (item.changeType == 'DELETE') {
                        // delete original object
                        const originalItem = props.table.items.find((item) => item.id == id)
                        const copyItem = Object.assign({}, originalItem) as Item
                        delete copyItem.id
                        copyItem.changeType = 'DELETE'
                       changesDictionary[id] = copyItem
                    }
                }
                 // 3: DELETE -> *
                if (savedItem.changeType == 'DELETE') { 
                    throw new Error('id reused!')
                    return []
                }
                
            }
            // prepare changedItems for emit
            changedItems = []
            for (let id in changesDictionary) {
                changedItems.push(changesDictionary[id])
            }
            return changedItems
        }

        const confirmChanges = () => {
            cancelEditAdd()
            emit('changeTable', manageChanges())
            loading.value = true
        }

        const makeItemSlotName = (headerValue : string) => {
            return 'item-' + headerValue
        }

        const makeHeaderSlotName = (headerValue : string) => {
            return 'header-' + headerValue
        }

        const isEditingAddingId = (id: number) => {
            return ((isEditing.value || isAdding.value) && editingItem.id == id)
        }

        const isEditingId = (id: number) => {
            return (isEditing.value && editingItem.id == id)
        }

        const isAddingId = (id: number) => {
            return (isAdding.value && editingItem.id == id)
        }

        
        console.log('EditTable component: Setup completed')

        
        return {
            headers, items,
            currentId,
            loading, 
            isEditing, isAdding, editingItem,
            changedItems,
            loadTable,
            editItem, submitEdit,
            addItem, submitAdd,
            submit, cancelEditAdd,
            deleteItem, 
            discardChanges, confirmChanges,
            makeItemSlotName, makeHeaderSlotName,
            isEditingId, isAddingId, isEditingAddingId
        }
    }
})


</script>


<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <div class="container table">   
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
                <div class="operation__wrapper">
                    <div class="operation__icon" 
                        @click="deleteItem(item.id)">
                        <i class="fa fa-trash fa-2x fa-fw" aria-hidden="true"></i>
                    </div>
                    <div class="operation__icon" 
                        v-if="!isEditingAddingId(item.id)"
                        @click="editItem(item)">
                        <i class="fa-solid fa-pen-to-square fa-2x fa-fw"></i>
                    </div>
                    <div class="operation__icon" 
                        v-if="isEditingAddingId(item.id)"
                        @click="cancelEditAdd()">
                        <i class="fa-solid fa-xmark fa-2x fa-fw"></i>
                    </div>
                    <div class="operation__icon" 
                        v-if="isAddingId(item.id)"
                        @click="submitAdd">
                        <i class="fa-solid fa-check fa-2x fa-fw"></i>
                    </div>
                    <div class="operation__icon" 
                        v-if="isEditingId(item.id)"
                        @click="submitEdit">
                        <i class="fa-solid fa-check fa-2x fa-fw"></i>
                    </div>
                </div>

            </template>
            
            <template v-for="(headerItem, index) in table.headers"
                :key="index"
                #[makeItemSlotName(headerItem.value)]="item">
                <div class="item__wrapper"
                    @dblclick="editItem(item)">
                    <input class="form-control" type="text"
                        v-if="isEditingAddingId(item.id)"
                        v-model="editingItem[headerItem.value]"
                        @keydown.enter="submit()"
                        @keydown.esc="cancelEditAdd()"
                    />
                    <p class="" v-else>{{ item[headerItem.value] }}</p>       
                </div>
            </template>

            <template v-for="(headerItem, index) in headers"
                :key="index"
                #[makeHeaderSlotName(headerItem.value)]>
                <div class="header__wrapper">
                    <h3>{{ headerItem.value }}</h3>
                </div>
            </template>

        </EasyDataTable>    
    </div>
    <div class="control-panel">  
        <div class="control-panel__buttons-wrapper">
            <button @click="addItem" class="control-panel__button btn btn-secondary">Add row</button>
            <button @click="discardChanges" class="control-panel__button btn btn-danger">Discard changes</button>
            <button @click="confirmChanges" class="control-panel__button btn btn-primary">Confirm changes</button>
        </div>   
        <div class="operation__wrapper" 
            v-if="isAdding || isEditing">
            <div class="operation__icon"  
                @click="deleteItem(editingItem.id)">
                <i class="fa fa-trash fa-3x fa-fw" aria-hidden="true"></i>
            </div>
            <div class="operation__icon"  
                @click="cancelEditAdd()">
                <i class="fa-solid fa-xmark fa-3x fa-fw"></i>
            </div>
            <div class="operation__icon"  
                v-if="isAddingId(editingItem.id)"
                @click="submitAdd()">
                <i class="fa-solid fa-check fa-3x fa-fw"></i>
            </div>
            <div class="operation__icon" 
                v-if="isEditingId(editingItem.id)"
                @click="submitEdit">
                <i class="fa-solid fa-check fa-3x fa-fw"></i>
            </div>
        </div>
    </div>
    

</template>

<style scoped lang="scss">
    @import '../assets/styles/style.scss';

    .operation {

        &__wrapper {
            display: flex;
            flex-direction: row;
            justify-content: flex-start;
            height: 100%;
        }

        &__icon {
            margin: 10px;
        }
    }

    .item {

        &__wrapper {
            position: relative;
            width: 100%;
            height: 100%;
        }
    }

    .header {
        
        & h3 {
            font-weight: bold;
            font-size: 16px;
            color: #{$indigo}
        }
    }

    .control-panel {
        position: fixed;
        left: 0;
        right: 0;
        bottom: 67px;
        z-index: 1;
        background: white;
        border-top: 3px solid #{$primary};
        padding: 10px;
        display: flex;
        flex-direction: row-reverse;
        justify-content: space-between;

        &__buttons-wrapper {
            display: flex;
            flex-direction: row;
            justify-content: flex-end;
            height: 100%;
        }

        &__button {
            margin: 5px 30px;
            width: 150px
        }
    }

    .table {
        position: relative;
        padding-bottom: 70px;
    }

</style>