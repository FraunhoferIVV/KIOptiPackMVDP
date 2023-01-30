<template>
    <div class="wrapper">
        <h1 class="file-upload-title">Hochladen einer XLSX- oder CSV-Datei</h1>
        <div class="file-upload-wrapper">
            <form class="file-upload-form file-upload-item">
                <input type="file" @change="readFile" />
                <label for="file-uploader" class="file-upload"> <p>{{uploadMessage}}</p></label>
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
        },
        submitFile() {  // add delimiter options!!! // finish posting!
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
                this.uploadMessage = 'Keine Datei oder falsche Dateierweiterung!';
            }
        },
        checkExtension() {
            try {
                if (this.dataFile.name && this.dataFile.name.includes('.xlsx') || this.dataFile.name.includes('.csv')) {
                    this.uploadMessage = 'Senden...';
                    return true;
                }
            } catch (err) {
                return false;
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

    .file-upload-wrapper {
        display: flex;
        flex-direction: column;
        width: 360px;
        border: 1px solid black;
        border-radius: 5px;
        padding: 10px;
    }
    /* .file-upload-form {
    
    }    */

    .file-upload-item {
        margin-bottom: 15px;
        font-size: 14px;
    }
</style>