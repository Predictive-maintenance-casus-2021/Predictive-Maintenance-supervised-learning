<template>
  <div class="w-full h-full">
    <canvas id="line-chart" width="full" height="full"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js"

export default {
  name: 'LineChart',
  props: {
    labels: Array,
    datasets: Array,
  },
  mounted() {
    let ctx = document.getElementById("line-chart");
    new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Cooler condition", "Valve condition", "Internal pump leakage", "Hydraulic accumulator"],
        datasets: [
        {
          label: "Cooler condition",
          data: [100, 100, 100, 20, 20, 3],
          borderColor: 'rgb(255,93,93)',
          backgroundColor: 'rgba(255,117,117,0.5)',
        },
        {
          label: "Valve condition",
          data: [100, 100, 90, 80, 73, 73],
          borderColor: 'rgb(122,248,122)',
          backgroundColor: 'rgba(151,255,151,0.5)',
        },
        {
          label: "Internal pump leakage",
          data: [0, 0, 0, 1, 1, 2],
          borderColor: 'rgb(125,125,255)',
          backgroundColor: 'rgba(166,166,255,0.5)',
        },
        {
          label: "Hydraulic accumulator",
          data: [130, 115, 115, 100, 90, 90],
          borderColor: 'rgb(211,255,122)',
          backgroundColor: 'rgba(250,255,144,0.5)',
        },
      ]
      },
      options: {
        scales: {
          yAxes: [{
            display: true,
            ticks: {
                suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
                // OR //
                beginAtZero: true   // minimum value will be 0.
            }
          }]
        }
      }
    })
  }
}

</script>