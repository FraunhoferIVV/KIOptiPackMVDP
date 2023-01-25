<template>
    <div style="border-style:solid">
      <input type="file" ref="file" @change="readFile" />
      <button @click="submitFile">Upload!</button>
    </div>
</template>

<script lang="ts">
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
        submitFile() {
            if (this.dataFile.name.includes('.xlsx') || this.dataFile.name.includes('.csv')) {
                this.correctExtension = true;
                console.log('Correct file extension!')
                console.log(this.dataFile)
            } else {
                this.correctExtenstion = false
                console.log('Wrong file extension!')
            }
        }
    }
}
</script>

