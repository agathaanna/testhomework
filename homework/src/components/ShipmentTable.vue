<template>
  <div>
    <b-table
    variant="dark"
      id="my-table"
      :items="shipments"
      :fields="fields"
      :per-page="perPage"
      :current-page="currentPage"
    ></b-table>
    <b-container
      v-if="!shipments.length"
      class="center w-100 d-flex justify-content-center align-items-center"
      style="height: 20rem"
    >
      No Data
    </b-container>
    <b-pagination
    align="right"
    class="pt-3 dark"
      v-if="shipments.length"
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
  </div>
</template>

<script>
import moment from "moment";
export default {
  name: "ShipmentTable",
  props: {
    shipments: Array,
  },
  data() {
    return {
      perPage: 10,
      currentPage: 1,
      fields: [
        { key: "shipment_id" },
        { key: "weight_(kg)" },
        { key: "distance_(km)" },
        {
          key: "pickup_time",
          formatter: (value) => {
            return moment(value).format("MM-DD-yyyy");
          },
        },
        {
          key: "drop_off_time",
          formatter: (value) => {
            return moment(value).format("MM-DD-yyyy");
          },
        },
        { key: "CO2_emission" },
      ],
    };
  },
  computed: {
    rows() {
      return this.shipments.length;
    },
  },
};
</script>

<style scoped>
</style>
