<template>
    <div class="file-upload">
        <h1 class="file-upload__title">Upload XLSX- or CSV-File</h1>
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
                <span class="file-upload__message" :class="uploadMessageClassObject">{{uploadMessage.content}}</span>
            </div>
        </div>
    </div>
</template>


<script lang="ts">
import axios from 'axios';

export default {
    mounted() {
        this.loadMaterialOptions()
    },
    data() {
        return {
            dataFile: {} as File,
            fileType: '',
            messageTypes: {
                    info: 'info',
                    error: 'error',
                    warning: 'warning',
                    success: 'success'
                },
            uploadMessage: {
                content: 'Upload file not chosen!',
                type: 'info'
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
                'file-upload__message--error': this.uploadMessage.type === this.messageTypes.error,
                'file-upload__message--success': this.uploadMessage.type === this.messageTypes.success,
                'file-upload__message--warning': this.uploadMessage.type === this.messageTypes.warning,
            }
        }
    },
    methods: {
        readFile(event: Event) {
            try {
                const target = event.target as HTMLInputElement;
                this.dataFile = target.files![0]; // File Object
                this.uploadMessage.content = '';
                this.uploadMessage.type = this.messageTypes.info
            } catch (err) {
                this.uploadMessage.content = 'File not accepted!';
                this.uploadMessage.type = this.messageTypes.warning
            }
        },
        submitFile() { 
            if (this.checkExtension() && this.checkConfiguration()) {
                // build post data
                let formData = new FormData()
                // add dataFile
                formData.append('data_file', this.dataFile) 
                formData.append('file_type', this.fileType)
                // add dataFile configuration
                formData.append('data_delimiter', this.fileConfiguration.delimiterPick)
                formData.append('decimal_delimiter', this.fileConfiguration.decimalPick)
                // add materialId if exists
                if (this.materialID)
                    formData.append('material_id', this.materialID)
                else
                    formData.append('material_id', 'no')
                // log client message
                for (var pair of formData.entries()) {
                    console.log(pair[0]+ ', ' + pair[1]); 
                }
                // post formData
                const postUrl = 'http://localhost:5478/api/post_some_data';
                axios.post(postUrl, formData, {headers: {
                    "Content-Type": "multipart/form-data"
                    }}
                    ).then((res) => {
                            console.log(res)
                            this.uploadMessage.content = 'File successfully uploaded'
                            this.uploadMessage.type = this.messageTypes.success
                        }, (error) => {
                            console.log(error)
                            if (error.code === 'ERR_NETWORK') {
                                this.uploadMessage.content = 'Network error!'
                                this.uploadMessage.type = this.messageTypes.error;
                            } else if (error.code === 'ERR_BAD_REQUEST') {
                                this.uploadMessage.content = 'Unprocessable message!'
                                this.uploadMessage.type = this.messageTypes.error;
                            } else if ('response' in error) {
                                this.uploadMessage.content = error.response.data.detail;
                                this.uploadMessage.type = this.messageTypes.error;
                            } else {
                                this.uploadMessage.content = 'Unknown Error!'
                                this.uploadMessage.type = this.messageTypes.error
                            }
                        })
            }

        },
        checkExtension() {
            try {
                if (!this.dataFile || !this.dataFile.name) {
                    this.uploadMessage.content = 'No file!';
                    this.uploadMessage.type = this.messageTypes.warning;
                    return false;
                }
                if (this.includesExtension('.xlsx') || this.includesExtension('.csv')) {
                    this.uploadMessage.content = 'Sending...';
                    this.uploadMessage.type = this.messageTypes.info;
                    return true;
                }
                this.uploadMessage.content = 'Wrong extension!';
                this.uploadMessage.type = this.messageTypes.warning;
                return false;
            } catch (err) {
                this.uploadMessage.content = 'Can not check extension'
                this.uploadMessage.type = this.messageTypes.warning
                return false;
            }
        },
        includesExtension(ext: String) {
            let name = this.dataFile.name
            let n = name.length
            let m = ext.length
            if (n < m) {
                return false;
            }
            let ending = name.substring(n - m, n)
            if (ending.valueOf() == ext.valueOf()) {
                this.fileType = ext.valueOf()
                return true
            }
        },
        checkConfiguration() {
            if (this.fileConfiguration.decimalPick ==  this.fileConfiguration.delimiterPick) {
                this.uploadMessage.content = 'Not acceptable delimiter configuration!';
                this.uploadMessage.type = this.messageTypes.warning
                return false;
            }
            return true;
        },
        loadMaterialOptions() {
            
            const getUrl = 'http://localhost:5478/api/get_some_data';
            // await not needed: client doesn't have to wait for server response with current options
            axios.get(getUrl).
                then((res) => {
                    console.log(res)
                    this.materialOptions = JSON.parse(res.data)
                }, (error) => {
                    console.log(error)
                    this.uploadMessage.content = 'Can not load Material_ID hints!'
                    this.uploadMessage.type = this.messageTypes.warning
                })
            
        }
    }
}
</script>

<style scoped>

    .file-upload {
        margin: 20px;
    }

    .file-upload__wrapper {
        display: flex;
        flex-direction: column;
        width: 640px;
        border: 1px solid black;
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
        margin: 20px;
        font-size: 14px;
    }

    .file-upload__message--error {
        color: red;
    }

    .file-upload__message--success {
        color: green;
    }

    .file-upload__message--warning {
        color: orangered;
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
        font-size: 20px;
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
        color: green;
    }

    .dropdown__status--wrong {
        color: red;
    }

</style>