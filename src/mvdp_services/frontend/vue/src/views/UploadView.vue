<template>
    <div class="file-upload">
        <h1 class="file-upload__title">Hochladen einer XLSX- oder CSV-Datei</h1>
        <div class="file-upload__wrapper">
            <div class="file-upload__item form-group">
                <input type="file" class="file-upload__input form-control" id="file-uploader" @change="readFile" />
                <label for="file-uploader" class="file-upload__input-label"> <p>{{uploadMessage}}</p></label>
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
            <button class="file-upload__item file-upload__submit-button btn btn-primary btn-lg" @click="submitFile">Hochladen</button>
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
            uploadMessage: '',
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
            }
        }
    },
    methods: {
        readFile(event: Event) {
            try {
                const target = event.target as HTMLInputElement;
                this.dataFile = target.files![0]; // File Object
            } catch (err) {
                this.uploadMessage = 'Datei nicht gelesen';
            }
        },
        submitFile() { 
            if (this.checkExtension() && this.checkConfiguration()) {
                let formData = new FormData()
                formData.append('file', this.dataFile) 
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
        padding: 10px;
        font-size: 18px;
    }

    .file-upload__input-label {
        margin: 5px 0 0 5px;
        font-size: 18px;
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
</style>