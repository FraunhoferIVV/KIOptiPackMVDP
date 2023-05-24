<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

</script>

<template>
  <header>
    <div class="headline">
        <img src="./assets/kioptipack-logo.svg" alt=""  style="float: left;">
        <h1>{{ title }}</h1>
        <img src="./assets/ivv-logo.png" alt="" style="float: right;">
    </div>

    <ul class="nav nav-tabs">
      <li class="nav-item"><RouterLink class="nav-link" to="/">Start</RouterLink></li>
      <li class="nav-item"><RouterLink class="nav-link" to="/upload_file">Upload</RouterLink></li>
      <li class="nav-item"><RouterLink class="nav-link" to="/edit_data">Edit</RouterLink></li>
      <li class="nav-item"><RouterLink class="nav-link" to="/system_status">System Status</RouterLink></li>
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

<script lang="ts">
import {constants} from "@/constants";
import axios from "axios";
import {defineComponent} from "vue";

export default defineComponent({

  mounted() {
    this.set_title()
  },
  data() {
    return {
      title: 'Minimum Viable Dataspace Participant loading…'
    }
  },
  methods: {
    async set_title() {
      axios({
        method: 'get',
        url: constants.restBaseUrl + 'api/frontend_config',
        timeout: 2000
      }).then((res) => {
        this.title = res.data.title
        window.setTimeout(this.set_title, 5*60*1000)
      }, (error) => {
        console.log('Can not establish connection to server to update title')
        console.log(error)
        window.setTimeout(this.set_title, 10000)
      })
    }
  }
})
</script>