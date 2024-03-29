<template>
    <div class="file-upload">
        <h2 class="file-upload__title">Upload XLSX- or CSV-File</h2>
        <div class="file-upload__wrapper">
            <div class="file-upload__item form-group">
                <input type="file" class="file-upload__input form-control" id="file-uploader" @change="readFile" />
            </div>
            <div class="file-upload__item radio-list">
                <div class="radio-list__item form-check" id="delimiter">
                    <p class="radio-list__item-name">Delimiter</p>
                    <div class="radio-field" v-for="(delim, ind) in fileDelimiters" :key="ind">
                        <input class="radio-field__input-circle form-check-input"
                            v-model="fileConfiguration.delimiterPick"
                            type="radio" name="delimiter"
                            :id="delim.id"
                            :value="delim.value">
                        <label class="radio-field__label form-check-label" :for="delim.id">{{ delim.name }}</label>
                    </div>
                </div>
                <div class="radio-list__item form-check" id="decimal">
                    <p class="radio-list__item-name">Decimal delimiter</p>
                    <div class="radio-field" v-for="(delim, ind) in decimalDelimiters" :key="ind">
                        <input class="radio-field__input-circle form-check-input"
                            v-model="fileConfiguration.decimalPick"
                            type="radio" name="decimal"
                            :id="delim.id"
                            :value="delim.value">
                        <label class="radio-field__label form-check-label" :for="delim.id">{{ delim.name }}</label>
                    </div>
                </div>
            </div>
            <div class="file-upload__item dropdown form-group">
                <label class="dropdown__description">Material_ID:
                    <div class="dropdown__body">
                        <input class="dropdown__input form-control" list="materialID" name="materialID" v-model="materialID"/>
                        <div class="dropdown__status">
                            <span v-if="displayOkMaterialId" class="dropdown__status--ok">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-bookmark-check" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M10.854 5.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                                <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
                                </svg>
                            </span>
                            <span v-if="!displayOkMaterialId" class="dropdown__status--wrong">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-bookmark-x" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M6.146 5.146a.5.5 0 0 1 .708 0L8 6.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 7l1.147 1.146a.5.5 0 0 1-.708.708L8 7.707 6.854 8.854a.5.5 0 1 1-.708-.708L7.293 7 6.146 5.854a.5.5 0 0 1 0-.708z"/>
                                <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
                                </svg>
                            </span>
                        </div>
                    </div>
                </label>
                <datalist id="materialID" v-if="!displayOkMaterialId">
                    <option v-for="(option, ind) in materialOptions" :key="ind" :value="option"></option>
                </datalist>
                
            </div>
            <div class="file-upload__item">
                <button class="file-upload__submit-button btn btn-primary btn-lg" @click="submitFile">Upload</button>
            </div>
            <div class="file-upload__item">
                <p class="file-upload__message" :class="uploadMessageClassObject">{{uploadMessage.content}}</p>
            </div>
        </div>
    </div>

</template>


<script lang="ts">
import axios from 'axios';
import {constants} from "@/constants";
import { defineComponent } from 'vue';

import EditTable from '@/components/EditTable.vue'

import type MessageType from '@/types/MessageType'



export default defineComponent({
    components: {
        EditTable
    },
    mounted() {
        this.loadUploadConfig()
        // this.loadMaterialOptions()
    },
    data() {           
        return {
            uploadForbidden: true,
            dataFile: {} as File,
            uploadMessage: {
                content: 'Upload file not chosen!',
                type: 'info' as MessageType
            },
            fileDelimiters: [{
                    name: 'Comma',
                    value: 'comma',
                    id: 'delimiters-comma'
                }, {
                    name: 'Semicolon',
                    value: 'semicolon',
                    id: 'delimiters-semicolon'
                }],
            decimalDelimiters: [{
                    name: 'Point',
                    value: 'point',
                    id: 'decimals-point'
                }, {
                    name: 'Comma',
                    value: 'comma',
                    id: 'decimals-comma'
                }],
            fileConfiguration: {
                delimiterPick: 'comma',
                decimalPick: 'point', 
            },
            materialOptions: [] as String[],
            materialID: ''
        }
    },
    computed: {
        displayOkMaterialId() {
            return this.materialOptions.includes(this.materialID)
        },
        uploadMessageClassObject() {
            return {
                'file-upload__message--error': this.uploadMessage.type == 'error',
                'file-upload__message--success': this.uploadMessage.type == 'success',
                'file-upload__message--warning': this.uploadMessage.type == 'warning',
            }
        }
    },
    methods: {
        readFile(event: Event) {
            try {
                const target = event.target as HTMLInputElement;
                this.dataFile = target.files![0]; // File Object
                this.uploadMessage.content = '';
                this.uploadMessage.type = 'info'
            } catch (err) {
                this.uploadMessage.content = 'File not accepted!';
                this.uploadMessage.type = 'warning'
            }
        },
        fileIsValid() {
            return (this.checkExtension() && this.checkConfiguration())
        },
        submitFile() { 
            if (this.fileIsValid()) {
                // build post data
                let formData = new FormData()
                // add dataFile
                formData.append('data_file', this.dataFile) 
                formData.append('file_type', this.getExtension())
                // add dataFile configuration
                formData.append('data_delimiter', this.fileConfiguration.delimiterPick)
                formData.append('decimal_delimiter', this.fileConfiguration.decimalPick)
                // add materialId if exists
                if (this.materialID)
                    formData.append('material_id', this.materialID)
                // log client message
                for (var pair of formData.entries()) {
                    console.log(pair[0]+ ', ' + pair[1]); 
                }
                // post formData
                const postUrl = constants.restBaseUrl + 'api/upload_data';
                axios.post(postUrl, formData, {headers: {
                    "Content-Type": "multipart/form-data"
                    }}
                    ).then((res) => {
                            console.log(res)
                            this.uploadMessage.content = 'File successfully uploaded'
                            this.uploadMessage.type = 'success'
                        }, (error) => {
                            console.log(error)
                            if (error.code == 'ERR_NETWORK') {
                                this.uploadMessage.content = 'Network error!\n\n' +
                                    'PosfileConfiguration. xlsx-file not valid (create file from your office software)'                  
                                this.uploadMessage.type = 'error';
                            } else if ('response' in error) {
                                this.uploadMessage.content = error.response.data.detail;
                                this.uploadMessage.type = 'error';
                            } else {
                                this.uploadMessage.content = 'Unknown Error!'
                                this.uploadMessage.type = 'error'
                            }
                        })
            }

        },
        getExtension() {
          let parts = this.dataFile.name.split('.')
          return parts[parts.length - 1].toLowerCase();
        },
        checkExtension() {
          let allowed_extensions = ['csv', 'xlsx', 'json']
            try {
                if (!this.dataFile || !this.dataFile.name) {
                    this.uploadMessage.content = 'No file!';
                    this.uploadMessage.type = 'warning';
                    return false;
                }
                if (allowed_extensions.indexOf(this.getExtension()) > -1) {
                    this.uploadMessage.content = 'Sending...';
                    this.uploadMessage.type = 'info';
                    return true;
                }
                this.uploadMessage.content = 'Wrong extension!';
                this.uploadMessage.type = 'warning';
                return false;
            } catch (err) {
                this.uploadMessage.content = 'Can not check extension'
                this.uploadMessage.type = 'error'
                return false;
            }
        },
        checkConfiguration() {
            if (this.getExtension() == 'csv' &&
                  this.fileConfiguration.decimalPick ==  this.fileConfiguration.delimiterPick) {
                this.uploadMessage.content = 'Delimiter configuration contains errors. Did you select the same type twice?!';
                this.uploadMessage.type = 'warning'
                return false;
            }
            return true;
        },
        loadUploadConfig: async function() {
            await axios({
                method: 'get',
                url: constants.restBaseUrl + 'api/config/upload_forbidden',
                timeout: 3000
            }).then((res) => {
                this.uploadForbidden = res.data;
                console.log('Upload config loaded');
                if (this.uploadForbidden) {
                    this.uploadMessage.content = 'Uploading forbidden by configuration!'
                    this.uploadMessage.type = 'warning'
                }  
            }, (error) => {
                console.log('Can not establish connection to server to get upload config')
                console.log(error)
            })
        },
        loadMaterialOptions() {
            
            const getUrl = constants.restBaseUrl + 'api/material_options';
            // await not needed: client doesn't have to wait for server response with current options
            /*
            axios.get(getUrl).
                then((res) => {
                    console.log(res)
                    this.materialOptions = res.data
                }, (error) => {
                    console.log(error)
                    this.uploadMessage.content = 'Can not load Material_ID hints!'
                    this.uploadMessage.type = 'warning'
                })
            */
        }
    }
})
</script>

<style scoped lang="scss">
    @import '../assets/styles/style.scss';

    .file-upload__editor {
        width: 100%;
        height: 100%
    }

    .file-upload__wrapper {
        display: flex;
        flex-direction: column;
        width: 640px;
        border: 1px solid #{$primary};
        border-radius: 5px;
        padding: 10px;
    }

    .file-upload__item {
        margin: 5px;
        padding: 5px;
        font-size: 18px;
    }

    .file-upload__input {
        width: 500px;
    }
    .file-upload__message {
        white-space: pre;
    }

    .file-upload__message--error {
        color: red;
    }

    .file-upload__message--success {
        color: #{$primary};
    }

    .file-upload__message--warning {
        color: #{$warning};
    }

    .file-upload__submit-button {
        width: 300px;
    }

    .radio-list {
        display: flex;
        flex-direction: row;

    }
    .radio-list__item {
        flex: 50%;
    }

    .radio-list__item-name {
        font-weight: bold;
    }

    .dropdown__description {
        font-weight: bold;
    }

    .dropdown__body {
        display: flex;
    }

    .dropdown__status {
        margin-left: 10px;
    }

    .dropdown__status svg {
        width: 30px;
        height: 30px;
    }

    .dropdown__status--ok {
        color: #{$primary};
    }

    .dropdown__status--wrong {
        color: red;
    }

</style>