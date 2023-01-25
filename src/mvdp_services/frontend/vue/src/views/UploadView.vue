<template>
    <div style="border-style:solid">
      <input type="file" ref="file" @change="readFile()" />
      <div v-if="Image">
        <img :src="preview" />
      </div>
    </div>
</template>

<script lang="ts">
export default {
    data() {
        return {
            example: null,
            Image: false,
            preview: null
        }
    },
    methods: {
    readFile() {
      this.example = this.$refs.file.files[0];
      if (
        this.example.name.includes(".png") ||
        this.example.name.includes(".jpg")
      ) {
        this.Image = true;
        this.preview = URL.createObjectURL(this.example);
      } else {
        this.Image = false;
      }
    }
  }
}
</script>

<style scoped>
    .imgBox {
        height: 100px;
        width: 100px;
    }
</style>