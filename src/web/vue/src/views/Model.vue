<template>
  <div>
    <h1 class="text-4xl text-gray-900 font-bold mb-6">Model prestaties</h1>

    <div class="flex justify-start">
      <div class="w-1/3 mr-16">
        <div
          class="w-full bg-white border border-1 px-6 py-4 rounded-lg shadow-xl"
        >
          <div class="flex justify-between items-center">
            <label class="text-base font-medium">Selecteer een model:</label>
            <select
              class="rounded-md border-gray-300 shadow-sm focus:border-green-200 focus:ring focus:ring-green-100 focus:ring-opacity-50"
              v-model="selected_model.name"
              @change="loadStats()"
            >
              <option value="cooler_condition">Cooler condition</option>
              <option value="valve_condition">Valve condition</option>
              <option value="internal_pump_leakage">
                Internal pump leakage
              </option>
              <option value="hydraulic_accumulator">
                Hydraulic accumulator
              </option>
            </select>
          </div>

          <div v-show="selected_model.name">
            <div
              class="w-full bg-gray-100 rounded-full mt-2 mb-4"
              style="height: 1px"
            ></div>
            <h2
              class="capitalize text-xl font-bold text-gray-900 mb-2"
              :class="{
                'text-green-500': this.stats.accuracy >= 80,
                'text-red-500': this.stats.accuracy <= 50,
                'text-yellow-500':
                  this.stats.accuracy > 50 && this.stats.accuracy < 80,
              }"
            >
              {{ selected_model.name.replace(/_/g, " ") }}
            </h2>
            <div>
              <div class="mb-2">
                <h3 class="text-lg font-medium text-gray-800">Accuracy:</h3>
                <p class="font-base text-gray-700">{{ stats.accuracy }}%</p>
              </div>
              <div class="mb-2">
                <h3 class="text-lg font-medium text-gray-800">Precision:</h3>
                <p class="font-base text-gray-700">
                  {{ stats.precision.join("%, ") }}%
                </p>
              </div>
              <div class="mb-2">
                <h3 class="text-lg font-medium text-gray-800">Recall:</h3>
                <p class="font-base text-gray-700">
                  {{ stats.recall.join("%, ") }}%
                </p>
              </div>
              <div class="mb-2">
                <h3 class="text-lg font-medium text-gray-800">F1-score:</h3>
                <p class="font-base text-gray-700">
                  {{ stats.f1_score.join("%, ") }}%
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="h-full">
        <div
          class="bg-white border border-1 rounded-lg shadow-xl overflow-hidden"
          v-show="selected_model.name"
        >
          <img
            class="h-2/5"
            :src="this.selected_model.img"
            :alt="
              this.selected_model.name.replace(/_/g, ' ') + ' confusion matrix'
            "
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Model",
  data() {
    return {
      selected_model: {
        name: "",
        img: "",
      },
      stats: {
        accuracy: 0,
        precision: [0],
        recall: [0],
        f1_score: [0],
      },
    };
  },
  methods: {
    loadStats() {
      this.$http
        .get("/api/stats/" + this.selected_model.name)
        .then((response) => {
          this.selected_model.img = response.request.responseURL + "/confusion";
          this.stats = response.data;
        });
    },
  },
};
</script>

<style scoped>
button:hover {
  transform: scale(1.1);
}
</style>
