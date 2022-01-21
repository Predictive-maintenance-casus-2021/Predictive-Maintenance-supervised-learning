<template>
  <div class="w-full h-full">
    <canvas
      id="line-chart"
      width="full"
      height="full"
      v-show="this.data.cooler_condition"
    ></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "LineChart",
  data() {
    return {
      data: {
        cooler_condition: [],
        valve_condition: [],
        internal_pump_leakage: [],
        hydraulic_accumulator: [],
      },
    };
  },
  computed: {
    labels() {
      let labels = [];
      for (let i = 0; i < this.data.cooler_condition.length; i++) {
        labels.push(i);
      }

      return labels;
    },
  },
  mounted() {
    this.loadData();
  },
  methods: {
    loadData() {
      this.$http.get("/api/predictions/history").then((response) => {
        this.data = response.data;

        this.makeChart();
      });
    },
    makeChart() {
      console.log("Loading chart...");
      let ctx = document.getElementById("line-chart");
      let chart = new Chart(ctx, {
        type: "line",
        data: {
          labels: this.labels,
          datasets: [
            {
              label: "Cooler condition",
              data: this.data.cooler_condition,
              borderColor: "rgb(255,93,93)",
              backgroundColor: "rgba(255,117,117,0.5)",
            },
            {
              label: "Valve condition",
              data: this.data.valve_condition,
              borderColor: "rgb(122,248,122)",
              backgroundColor: "rgba(151,255,151,0.5)",
            },
            {
              label: "Internal pump leakage",
              data: this.data.internal_pump_leakage,
              borderColor: "rgb(125,125,255)",
              backgroundColor: "rgba(166,166,255,0.5)",
            },
            {
              label: "Hydraulic accumulator",
              data: this.data.hydraulic_accumulator,
              borderColor: "rgb(211,255,122)",
              backgroundColor: "rgba(250,255,144,0.5)",
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          responsive: true,
          scales: {
            yAxes: [
              {
                display: true,
                ticks: {
                  min: 0, // minimum will be 0, unless there is a lower value.
                  // OR //
                  beginAtZero: true, // minimum value will be 0.
                  stepSize: 10,
                },
              },
            ],
          },
        },
      });

      setInterval(() => {
        this.loadData();

        this.updateChart(chart);
      }, 30 * 1000);
    },
    updateChart(chart) {
      chart.data.labels = this.labels;
      chart.data.datasets.forEach((dataset) => {
        let label = dataset.label.replace(/\s+/g, "_").toLowerCase();

        dataset.data = this.data[label];
      });

      chart.update();
    },
  },
};
</script>
