<template>
    <div class="wrapper">
        <h1 class="file-upload-title">Hochladen einer XLSX- oder CSV-Datei</h1>
        <div class="file-upload-wrapper">
            <form class="file-upload-item">
                <input type="file" @change="readFile" />
                <label for="file-uploader" class="file-upload"> <p>{{uploadMessage}}</p></label>
            </form>
            <form class="file-upload-item" id="radio-list">
                <div class="radio-list-item" id="delimiter">
                    <p>Trennzeichen</p>
                    <div v-for="(delim, ind) in fileDelimiters" :key="ind">
                        <input
                            v-model="fileConfiguration.delimiterPick"
                            type="radio" name="delimiter"
                            :id="delim.id"
                            :value="delim.value">
                        <label :for="delim.id">{{ delim.name }}</label>
                    </div>
                </div>
                <div class="radio-list-item" id="decimal">
                    <p>Dezimaltrennzeichen</p>
                    <div v-for="(delim, ind) in decimalDelimiters" :key="ind">
                        <input
                            v-model="fileConfiguration.decimalPick"
                            type="radio" name="decimal"
                            :id="delim.id"
                            :value="delim.value">
                        <label :for="delim.id">{{ delim.name }}</label>
                    </div>
                </div>
            </form>
            <button class="file-upload-item" @click="submitFile">Hochladen</button>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios';

export default {
    data() {
        return {
            dataFile: {} as File,
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
                this.dataFile = target.files![0];
            } catch (err) {
                this.uploadMessage = 'Datei nicht gelesen';
            }
        },
        submitFile() {  // add delimiter options!!! // finish posting!
            if (this.checkExtension() && this.checkConfiguration()) {
                const formData = new FormData()
                formData.append('file', this.dataFile)
                const postUrl = ''
                axios.post(postUrl, formData)
                    .then((res) => {
                            console.log(res.status);
                            this.uploadMessage = "Datei erfolgreich hochgelanden";
                        }, (res) => {
                            console.log(res.status);
                            this.uploadMessage = "Fehler beim Hochladen";
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

    .wrapper {
        margin: 20px;
    }

    .file-upload-wrapper {
        display: flex;
        flex-direction: column;
        width: 360px;
        border: 1px solid black;
        border-radius: 5px;
        padding: 10px;
    }

    #radio-list {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }

    .file-upload-item {
        margin-bottom: 15px;
        font-size: 14px;
    }
</style>