<template>
    <div class="wrapper">
        <h1 class="file-title">Hochladen einer XLSX- oder CSV-Datei</h1>
        <form class="file-form">
            <input class="file-form-item" id="file-uploader" type="file" @change="readFile" />
            
            <button class="file-form-item" @click="submitFile">Hochladen</button>
            <label for="file-uploader" class="file-upload">{{uploadMessage}}</label>
        </form>
    </div>
</template>

<script lang="ts">
import axios from 'axios';



export default {
    data() {
        return {
            dataFile: {} as File,
            uploadMessage: ''
        }
    },
    methods: {
        readFile(event: Event) {
            try {
                const target = event.target as HTMLInputElement;
                this.dataFile = target.files![0];
            } catch (err) {
                console.log("Error accepting the file");
            }
            if (!this.dataFile) {
                this.uploadMessage="Keine Datei!"
                return;
            }
            if (this.checkExtension()) {
                console.log('posting...')
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
            } else {
                this.uploadMessage = 'Falsche Dateierweiterung!';
            }
        },
        submitFile() {  // add delimiter options!!! // finish posting!
            
        },
        checkExtension() {
            if (this.dataFile.name && this.dataFile.name!.includes('.xlsx') || this.dataFile.name!.includes('.csv')) {
                this.uploadMessage = 'Senden...';
                return true;
            }
            return false;
        }

    }
}
</script>

<style scoped>

    .wrapper {
        margin: 20px;
    }
    .file-form {
        display: flex;
        flex-direction: column;
        width: 360px;
        border: 1px solid black;
        border-radius: 5px;
        padding: 10px;
    }

    .file-form-item {
        margin-bottom: 15px;
        font-size: 14px;
    }
</style>