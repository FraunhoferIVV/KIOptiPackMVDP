<template>
    <form style="border-style:solid">
      <input type="file" ref="file" @change="readFile" />
      <button @click="submitFile">Upload!</button>
    </form>
</template>

<script lang="ts">
import { FRAGMENT } from '@vue/compiler-core';
import axios from 'axios';



export default {
    data() {
        return {
            dataFile: {} as File,
            correctExtension: false
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
            if (!this.dataFile) {
                console.log("No file loaded!")
                return;
            }
            if ((this.dataFile.name.includes('.xlsx') || this.dataFile.name.includes('.csv'))) {
                this.correctExtension = true;
                console.log('posting...')
                const formData = new FormData()
                formData.append('file', this.dataFile)
                const postUrl = ''
                axios.post(postUrl, formData)
                    .then((res) => {
                        console.log(res.status);
                    })
            } else {
                this.correctExtension = false
                console.log('Wrong file extension!')
            }
        }
    }
}
</script>

