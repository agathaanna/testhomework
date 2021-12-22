<template>
  <div>
    <b-navbar navbar-dark bg-dark toggleable="lg" type="dark" variant="dark">
       <b-navbar-brand class="px-5" href="#">CO2 Emission Analytics</b-navbar-brand>
    </b-navbar>
    <b-container class="pt-5 shadow-none p-3 mb-5 bg-light rounded" style="height:100vh">
      
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <DateRange @apply-filter="applyFilter" />
          <hr class="my-5"/>
          <ShipmentTable :shipments="shipments" />
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ShipmentTable from "./components/ShipmentTable.vue";
import DateRange from "./components/DateRange.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    ShipmentTable,
    DateRange,
  },
  data() {
    return {
      shipments: [],
    };
  },
  methods: {
    applyFilter: function (e) {
      axios
        .get(
          `http://127.0.0.1:3000/shipment?start_date=${e.startDate}&end_date=${e.endDate}`
        )
        .then((response) => {
          this.shipments = response.data;
          
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
