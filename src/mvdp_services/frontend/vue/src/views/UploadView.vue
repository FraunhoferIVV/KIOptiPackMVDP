<template>
    <div class="file-upload">
        <h1 class="file-upload__title">Hochladen einer XLSX- oder CSV-Datei</h1>
        <div class="file-upload__wrapper">
            <form class="file-upload__item">
                <input type="file" class="file-upload__input" id="file-uploader" @change="readFile" />
                <label for="file-uploader" class="file-upload__input-label"> <p>{{uploadMessage}}</p></label>
            </form>
            <form class="file-upload__item radio-list">
                <div class="radio-list__item" id="delimiter">
                    <p class="radio-list__item-name">Trennzeichen</p>
                    <div class="radio-field" v-for="(delim, ind) in fileDelimiters" :key="ind">
                        <input class="radio-field__input-circle"
                            v-model="fileConfiguration.delimiterPick"
                            type="radio" name="delimiter"
                            :id="delim.id"
                            :value="delim.value">
                        <label class="radio-field__label" :for="delim.id">{{ delim.name }}</label>
                    </div>
                </div>
                <div class="radio-list__item" id="decimal">
                    <p class="radio-list__item-name">Dezimaltrennzeichen</p>
                    <div class="radio-field" v-for="(delim, ind) in decimalDelimiters" :key="ind">
                        <input class="radio-field__input-circle"
                            v-model="fileConfiguration.decimalPick"
                            type="radio" name="decimal"
                            :id="delim.id"
                            :value="delim.value">
                        <label class="radio-field__label" :for="delim.id">{{ delim.name }}</label>
                    </div>
                </div>
            </form>
            <button class="file-upload__item file-upload__submit-button" @click="submitFile">Hochladen</button>
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
                //formData.append('file', this.dataFile)
                const postUrl = 'http://localhost:5478/api/post_some_data';

                axios.post(postUrl, 
                //formData
                {
  "machine": "string",
  "name": "string",
  "measurement_id": "58c297d8-a15c-11ed-b25d-d89ef316c36d",
  "value": "string",
  "timestamp": "2023-01-31T12:57:15.825Z",
  "unit": ""
})
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
        width: 360px;
        border: 1px solid black;
        border-radius: 5px;
        padding: 10px;
    }

    .radio-list {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }

    .file-upload__item {
        margin-bottom: 15px;
        font-size: 14px;
    }
</style>