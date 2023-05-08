<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

</script>

<template>
  <header>
    <div class="headline">
        <img src="./assets/kioptipack-logo.svg" alt=""  style="float: left;">
        <h1>Minimum Viable Dataspace Participant</h1>
        <img src="./assets/ivv-logo.png" alt="" style="float: right;">
    </div>

    <ul class="nav nav-tabs">
      <li class="nav-item"><RouterLink class="nav-link" to="/">Start</RouterLink></li>
      <li class="nav-item"><RouterLink class="nav-link" to="/upload">Upload</RouterLink></li>
      <li class="nav-item"><RouterLink class="nav-link" to="/edit_values">Edit values</RouterLink>
    </ul>
  </header>

  <div class="content">
    <RouterView />
  </div>

  <div class="footline">
    <span>© Fraunhofer Institut für Verfahrenstechnik und Verpackung IVV, 2023</span>
    <img src="./assets/LOGO_BMBF.png" height="52" alt="BMWK">
    <img src="./assets/LOGO_FONA.jpg" height="48" alt="FONA">
  </div>

</template>

<style lang="scss">
 @import './assets/styles/style.scss';
 @import 'bootstrap/scss/bootstrap.scss';
</style>
