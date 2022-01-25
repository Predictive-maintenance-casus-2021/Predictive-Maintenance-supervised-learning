<template>
  <div class="home">
    <h1 class="text-4xl text-gray-900 font-bold mb-6">Dashboard</h1>
    <div class="grid grid-cols-5 gap-10 mb-12">
      <!--General-->
      <div
        class="relative h-32 flex flex-col justify-center p-10 rounded-lg shadow-xl overflow-hidden"
        :class="{
          'bg-red-200 text-red-900': severe_warnings > 0,
          'bg-yellow-200 text-yellow-900':
            warnings > 0 && severe_warnings === 0,
          'bg-green-200 text-green-900':
            severe_warnings === 0 && warnings === 0,
        }"
      >
        <span class="block text-5xl font-medium">{{
          warnings_and_severe_warnings
        }}</span>
        <span class="text-lg block font-medium">verwachte errors</span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="absolute h-52 w-52 opacity-20"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          style="right: -15%"
        >
          <path
            v-if="severe_warnings > 0"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
          <path
            v-else-if="warnings > 0"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
          />
        </svg>
      </div>

      <!--Cooler condition-->
      <div
        class="relative border border-1 h-32 flex flex-col justify-center p-10 rounded-lg shadow-xl overflow-hidden"
        :class="{
          'text-red-700': predictions.cooler_condition === 3,
          'text-yellow-700': predictions.cooler_condition === 20,
          'text-green-700': predictions.cooler_condition === 100,
        }"
      >
        <span class="relative block text-5xl font-medium"
          >{{ predictions.cooler_condition
          }}<span class="absolute top-0 text-xl italic">%</span>
        </span>
        <span class="text-lg block font-medium">cooler condition</span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="absolute h-52 w-52 opacity-20"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          style="right: -15%"
        >
          <path
            v-if="predictions.cooler_condition === 3"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
          <path
            v-else-if="predictions.cooler_condition === 20"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
          />
        </svg>
      </div>

      <!--Valve condition-->
      <div
        class="relative border border-1 h-32 flex flex-col justify-center p-10 rounded-lg shadow-xl overflow-hidden"
        :class="{
          'text-red-700': predictions.valve_condition === 73,
          'text-yellow-700':
            predictions.valve_condition === 90 ||
            predictions.valve_condition === 80,
          'text-green-700': predictions.valve_condition === 100,
        }"
      >
        <span class="relative block text-5xl font-medium"
          >{{ predictions.valve_condition
          }}<span class="absolute top-0 text-xl italic">%</span></span
        >
        <span class="text-lg block font-medium">valve condition</span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="absolute h-52 w-52 opacity-20"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          style="right: -15%"
        >
          <path
            v-if="predictions.valve_condition === 73"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
          <path
            v-else-if="
              predictions.valve_condition === 90 ||
              predictions.valve_condition === 80
            "
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
          />
        </svg>
      </div>

      <!--Internal pump leakage-->
      <div
        class="relative border border-1 h-32 flex flex-col justify-center p-10 rounded-lg shadow-xl overflow-hidden"
        :class="{
          'text-red-700': predictions.internal_pump_leakage === 2,
          'text-yellow-700': predictions.internal_pump_leakage === 1,
          'text-green-700': predictions.internal_pump_leakage === 0,
        }"
      >
        <span class="block text-5xl font-medium">{{
          predictions.internal_pump_leakage
        }}</span>
        <span class="text-lg block font-medium">internal pump leakage</span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="absolute h-52 w-52 opacity-20"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          style="right: -15%"
        >
          <path
            v-if="predictions.internal_pump_leakage === 2"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
          <path
            v-else-if="predictions.internal_pump_leakage === 1"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
          />
        </svg>
      </div>

      <!--Hydraulic accumulator-->
      <div
        class="relative border border-1 h-32 flex flex-col justify-center p-10 rounded-lg shadow-xl overflow-hidden"
        :class="{
          'text-red-700': predictions.hydraulic_accumulator === 90,
          'text-yellow-700':
            predictions.hydraulic_accumulator === 115 ||
            predictions.hydraulic_accumulator === 100,
          'text-green-700': predictions.hydraulic_accumulator === 130,
        }"
      >
        <span class="relative block text-5xl font-medium"
          >{{ predictions.hydraulic_accumulator
          }}<span class="absolute top-0 text-xl italic">bar</span></span
        >
        <span class="text-lg block font-medium">hydraulic accumulator</span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="absolute h-52 w-52 opacity-20"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          style="right: -15%"
        >
          <path
            v-if="predictions.hydraulic_accumulator === 90"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
          <path
            v-else-if="
              predictions.hydraulic_accumulator === 115 ||
              predictions.hydraulic_accumulator === 100
            "
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
          />
        </svg>
      </div>
    </div>

    <h2 class="text-3xl text-gray-900 font-bold mb-6">Data visualisaties</h2>
    <div class="w-full rounded border border-1 shadow-xl" style="height: 53vh">
      <LineChart
        style="
          margin-top: 1vh;
          height: 48vh;
          padding-left: 2vh;
          padding-right: 2vh;
        "
      />
      <a class="flex justify-center italic">*Tijd in minuten</a>
    </div>
  </div>
</template>

<script>
import LineChart from "../components/LineChart.vue";

export default {
  name: "Home",
  components: { LineChart },
  data() {
    return {
      predictions: {},
    };
  },
  mounted() {
    this.loadData();

    setInterval(() => {
      this.loadData();
    }, 5000);
  },
  methods: {
    loadData() {
      this.$http.get("/api/predictions").then((response) => {
        this.predictions = response.data;
      });
    },
  },
  computed: {
    warnings() {
      let warnings = 0;

      if (this.predictions.cooler_condition === 20) {
        warnings += 1;
      }
      if (
        this.predictions.valve_condition === 80 ||
        this.predictions.valve_condition === 90
      ) {
        warnings += 1;
      }
      if (this.predictions.internal_pump_leakage === 1) {
        warnings += 1;
      }
      if (
        this.predictions.hydraulic_accumulator === 100 ||
        this.predictions.hydraulic_accumulator === 115
      ) {
        warnings += 1;
      }

      return warnings;
    },
    severe_warnings() {
      let severe_warnings = 0;

      if (this.predictions.cooler_condition === 3) {
        severe_warnings += 1;
      }
      if (this.predictions.valve_condition === 73) {
        severe_warnings += 1;
      }
      if (this.predictions.internal_pump_leakage === 2) {
        severe_warnings += 1;
      }
      if (this.predictions.hydraulic_accumulator === 90) {
        severe_warnings += 1;
      }

      return severe_warnings;
    },
    warnings_and_severe_warnings() {
      if (this.severe_warnings > 0) {
        return this.severe_warnings;
      }

      return this.warnings;
    },
  },
};
</script>
