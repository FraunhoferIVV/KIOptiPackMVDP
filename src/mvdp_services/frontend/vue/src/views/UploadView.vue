<template>
    <div style="border-style:solid">
      <input type="file" ref="file" @change="readFile" />
      <button @click="submitFile">Upload!</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios';

export default {
    data() {
        return {
            dataFile: null,
            correctExtension: false
        }
    },
    methods: {
        readFile() {
            this.dataFile = this.$refs.file.files[0];
        },
        submitFile() {  // add delimiter options!!! // finish posting! // handle post-promise!
            if (this.dataFile.name.includes('.xlsx') || this.dataFile.name.includes('.csv')) {
                this.correctExtension = true;
                console.log('posting...')
                const formData = new FormData()
                formData.append('file', this.dataFile)
                const headers = {}
                const https = ''
                axios.post(https, formData, {headers })
                    .then((res) => {
                        res.data.files;
                        res.status;
                    })
            } else {
                this.correctExtenstion = false
                console.log('Wrong file extension!')
            }
        }
    }
}
</script>

