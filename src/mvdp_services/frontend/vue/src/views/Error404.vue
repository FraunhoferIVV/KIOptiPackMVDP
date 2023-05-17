<template>
    <h2>Error: File not found</h2>

    <img src="../assets/404.jpg">

    <p>I am sorry, something went wrong here.</p>
    <p>The path you were asking for could not be found.</p>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({})
</script>

<style scoped lang="scss">
@import '../assets/styles/style.scss';

h2 {
  color: #{$warning}
}

</style>