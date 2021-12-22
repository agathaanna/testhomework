<template>
  <b-container>
    <b-row>
      <b-col cols="3"></b-col>
      <b-col
        ><date-range-picker
          ref="picker"
          style="width: 100%"
          v-model="dateRange"
          @update="updateValues"
        ></date-range-picker></b-col
      ><b-col>
        <b-button variant="outline-dark" v-on:click="clearDate"
          >Clear</b-button
        >
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import DateRangePicker from "vue2-daterange-picker";
import moment from "moment";

export default {
  components: {
    DateRangePicker,
  },
  name: "DateRange",
  data() {
    return {
      dateRange: {
        startDate: new Date(),
        endDate: new Date(),
      },
      methods: {
        dateFormat: (classes, date) => {
          if (!classes.disabled) {
            classes.disabled = date.getTime() < new Date();
          }
          return classes;
        },
      },
    };
  },
  methods: {
    clearDate: function () {
      

      this.dateRange = {
        startDate: null,
        endDate: null,
      };
    },
    updateValues: function (e) {
      const dateRanges = {
        startDate: moment(e.startDate).format("yyyy-MM-DD"),
        endDate: moment(e.endDate).format("yyyy-MM-DD"),
      };
      this.$emit("apply-filter", dateRanges);
    },
  },
};
</script>

<style scoped>
</style>
