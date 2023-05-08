<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

</script>

<template>
  <header>
    <nav>
      <RouterLink class="nav-item" to="/">Start</RouterLink>
      <RouterLink class="nav-item" to="/upload_values">Upload values</RouterLink>
      <RouterLink class="nav-item" to="/edit_values">Edit values</RouterLink>
      <!--
      <RouterLink class="nav-item" to="/upload_material">Upload material</RouterLink>
      -->
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
