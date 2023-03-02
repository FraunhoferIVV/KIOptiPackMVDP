<template>
    <div class="file-upload">
        <h1 class="file-upload__title">Hochladen einer XLSX- oder CSV-Datei</h1>
        <div class="file-upload__wrapper">
            <div class="file-upload__item form-group">
                <input type="file" class="file-upload__input form-control" id="file-uploader" @change="readFile" />
                <label for="file-uploader" class="file-upload__input-label">{{uploadMessage}}</label>
            </div>
            <div class="file-upload__item radio-list">
                <div class="radio-list__item form-check" id="delimiter">
                    <p class="radio-list__item-name">Trennzeichen</p>
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
                    <p class="radio-list__item-name">Dezimaltrennzeichen</p>
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
                <label class="dropdown__description">Zugehörige Material-ID:
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
                <datalist id="materialID">
                    <option v-for="(option, ind) in materialOptions" :key="ind" :value="option"></option>
                </datalist>
                
            </div>
            <div class="file-upload__item">
                <button class="file-upload__submit-button btn btn-primary btn-lg" @click="submitFile">Hochladen</button>
            </div>
        </div>
    </div>
</template>


<script lang="ts">
import axios from 'axios';

export default {
    data() {
        return {
            dataFile: {} as File,
            fileType: 'csv',
            uploadMessage: 'Noch keine Datei ausgewählt',
            fileDelimiters: [{
                    name: 'Semikolon',
                    value: 'semicolon',
                    id: 'delimiters-semicolon'
                }, {
                    name: 'Komma',
                    value: 'comma',
                    id: 'delimiters-comma'
                }],
            decimalDelimiters: [{
                    name: 'Punkt',
                    value: 'point',
                    id: 'decimals-point'
                }, {
                    name: 'Komma',
                    value: 'comma',
                    id: 'decimals-comma'
                }],
            fileConfiguration: {
                delimiterPick: 'semicolon',
                decimalPick: 'point', 
            },
            materialOptions: ['Verpackung1', 'Verpackung2', 'Verpackung3'],
            materialID: ''
        }
    },
    computed: {
        displayOkMaterialId() {
            return this.materialID == '' || this.materialOptions.includes(this.materialID)
        }
    },
    methods: {
        readFile(event: Event) {
            try {
                const target = event.target as HTMLInputElement;
                this.dataFile = target.files![0]; // File Object
                this.uploadMessage = '';
            } catch (err) {
                this.uploadMessage = 'Datei nicht gelesen';
            }
        },
        submitFile() { 
            if (this.checkExtension() && this.checkConfiguration()) {
                // build post data
                let formData = new FormData()
                // add dataFile
                formData.append('dataFile', this.dataFile) 
                // extra formData for fileConfig
                //let formDataConfig = new FormData()
                formData.append('dataDelimiter', this.fileConfiguration.delimiterPick)
                formData.append('decimalDelimiter', this.fileConfiguration.decimalPick)
                // add fileConfig
                //formData.append('fileConfig', "formDataConfig")
                // add materialId if exists
                if (this.displayOkMaterialId)
                    formData.append('materialID', this.materialID)
                //
                for (var pair of formData.entries()) {
                    console.log(pair[0]+ ', ' + pair[1]); 
                }
                // post formData
                const postUrl = 'http://localhost:5478/api/post_some_data';
                axios.post(postUrl, formData)
                    .then((res) => {
                            console.log(res.status);
                            this.uploadMessage = "Datei erfolgreich hochgelanden";
                        }, (res) => {
                            console.log(res.status);
                            this.uploadMessage = 'Fehler beim Hochladen';
                        })
            }

        },
        checkExtension() {
            try {
                if (this.dataFile.name && this.dataFile.name.includes('.xlsx') || this.dataFile.name.includes('.csv')) {
                    this.uploadMessage = 'Senden...';
                    return true;
                }
                this.uploadMessage = 'Falsche Dateierweiterung!';
                return false;
            } catch (err) {
                this.uploadMessage = 'Keine Datei vorhanden!';
                return false;
            }
        },
        checkConfiguration() {
            if (this.fileConfiguration.decimalPick ==  this.fileConfiguration.delimiterPick) {
                this.uploadMessage = 'Nicht akzeptierbare Trennzeichenkonfiguration';
                return false;
            }
            return true;
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
    .file-upload__input-label {
        margin: 5px 0 0 5px;
        font-size: 18px;
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