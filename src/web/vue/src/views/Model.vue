<template>
  <div>
    <h1 class="text-4xl text-gray-900 font-bold mb-6">Model</h1>

    <!-- Selection module -->
    <div class="flex shadow-xl border border-1 mb-24 mt-12 w-2/6">
      <a class="ml-4 mt-2 text-normal">Selecteer functie:</a>
      <select class="bg-gray-100 border border-2 rounded ml-6 mt-2 mb-2 w-52" v-model="selected">
        <option disabled value="">Alstublieft selecteer</option>
        <option>Cooler condition</option>
        <option>Valve condition</option>
        <option>Internal pump leakage</option>
        <option>Hydraulic accumulator</option>
      </select>
      <button class="w-16 rounded font-medium shadow-xl ml-12 mt-2 mb-2 bg-green-200 hover:bg-green-400 hover:border-1">
        Load
      </button>
    </div>

    <!-- Model information -->
    <div class="flex">
      <div
        class="w-72 border border-1 shadow-xl rounded mr-56"
        style="overflow: hidden; position: relative;"
      >
        <p
          class="ml-4 font-medium text-xl mt-4"
          :class="{
            'text-green-500': feature.accuracy >= 0.8,
            'text-red-500': feature.accuracy <= 0.5,
            'text-yellow-500':
              feature.accuracy > 0.5 && feature.accuracy < 0.8,
          }"
        >
          {{ feature.name }}
        </p>
        <div class="ml-4 mt-6 space-y-2 text-xl">
          <p>Precision: {{ feature.precision }}</p>
          <p>Recall: {{ feature.recall }}</p>
          <p>Accuracy: {{ feature.accuracy }}</p>
          <p>F1-score: {{ feature.f1Score }}</p>
        </div>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="absolute h-72 w-72 mt-4 opacity-20"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          style="right: -12.5%; transform:rotate(20deg)"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 21h7a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v11m0 5l4.879-4.879m0 0a3 3 0 104.243-4.242 3 3 0 00-4.243 4.242z"
          />
        </svg>
      </div>

      <!-- Image of the model -->
      <div class="border border-1 shadow-xl rounded mr-96">
        <img src="@/assets/cooler_condition.png" alt="none" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Model",
  data() {
    return {
      feature: {
        name: "Cooler condition",
        precision: [1, 1, 1],
        recall: [1, 1, 1],
        accuracy: 1.0,
        f1Score: [1, 1, 1],
      },
    };
  },
};
</script>

<style scoped>
button:hover {
  transform: scale(1.1);
}
</style>
