<template>
    <h2>System status</h2>

    <table style="margin-top: 30px;">
        <tr v-for="(value, key) in status">
            <td>{{ key }}</td>
            <td :style="{ color: value ? 'green' : 'red' }">{{ value }}</td>
        </tr>

    </table>
</template>


<script lang="ts">
import {constants} from "@/constants";
import axios from "axios";
import {defineComponent} from "vue";

export default defineComponent({

  mounted() {
    this.update_status()
  },
  unmounted() {
    window.clearTimeout(this.updater)
  },
  data() {
    return {
      status: null,
      updater: 0
    }
  },
  methods: {
    async update_status() {
      axios({
        method: 'get',
        url: constants.restBaseUrl + 'api/health_check',
        timeout: 5000
      }).then((res) => {
        this.status = res.data
      }, (error) => {
        console.log('Can not establish connection to server to update title')
        console.log(error)
      })
      this.updater = window.setTimeout(this.update_status, 10000)
    }
  }
})
</script>

<style lang="scss" scoped>
@import '../assets/styles/style.scss';
@import 'bootstrap/scss/bootstrap.scss';

td {
  border: 1px dotted gray;
  padding-right: 10px;
  padding-left: 5px;
}
</style>