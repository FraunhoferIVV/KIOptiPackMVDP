<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <nav>
      <RouterLink class="nav-item" to="/">Home</RouterLink>
      <RouterLink class="nav-item" to="/upload">Upload</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
  nav {
    background-color: #25be6b;
    padding: 30px;

  }
  .nav-item{
    color: #260F43;
    margin-right: 50px;
  }
</style>
