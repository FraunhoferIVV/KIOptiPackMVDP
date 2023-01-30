<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <nav>
      <RouterLink class="nav-item" to="/">Start</RouterLink>
      <RouterLink class="nav-item" to="/upload">Hochladen</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
  nav {
    background-color: #25be6b;
    padding: 10px;
    margin-bottom: 10px;

  }
  .nav-item{
    margin-right: 10px;
    padding: 5px 10px;
    color: #260F43;
    font-size: 24px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 5px;
  }
  .nav-item:hover {
    background-color: #6CDEC1;
    color: #4B1E83;
  }
</style>
