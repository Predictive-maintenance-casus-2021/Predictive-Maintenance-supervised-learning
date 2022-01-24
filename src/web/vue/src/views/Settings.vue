<template>
  <div>
    <h1 class="text-4xl text-gray-900 font-bold mb-8">Settings</h1>

    <div class="max-w-4xl">
      <div class="flex mb-8">
        <button
          class="bg-green-400 rounded shadow px-4 py-1 text-white hover:bg-green-500 mr-4"
        >
          Import
        </button>
        <button
          class="bg-green-400 rounded shadow px-4 py-1 text-white hover:bg-green-500"
        >
          Export
        </button>
      </div>

      <form @submit.prevent="train">
        <!--
      Minuten in de toekomst voorspellen
      Lookback
      Early stopping
      Epochs
      Shift
      -->
        <h2>Data settings</h2>
        <div class="flex items-center mb-2">
          <label
            for="lookback"
            class="w-1/4 mr-4 text-lg font-medium text-gray-900"
            >Lookback</label
          >
          <input
            type="number"
            id="lookback"
            name="lookback"
            class="border border-1 border-gray-500 rounded w-full px-3 py-1"
            v-model.number="history_window"
          />
        </div>
        <div class="flex mb-2">
          <label
            for="future"
            class="w-1/4 mr-4 text-lg font-medium text-gray-900"
            >Future</label
          >
          <input
            type="number"
            id="future"
            name="future"
            class="border border-1 border-gray-500 rounded w-full px-3 py-1"
            v-model.number="future_window"
          />
        </div>
        <div class="flex mb-2">
          <label
            for="shift"
            class="w-1/4 mr-4 text-lg font-medium text-gray-900"
            >Shift</label
          >
          <input
            type="number"
            id="shift"
            name="shift"
            class="border border-1 border-gray-500 rounded w-full px-3 py-1"
            v-model.number="shift"
          />
        </div>
        <div class="flex mb-2">
          <label
            for="random_state"
            class="w-1/4 mr-4 text-lg font-medium text-gray-900"
            >Random state</label
          >
          <input
            type="number"
            id="random_state"
            name="random_state"
            class="border border-1 border-gray-500 rounded w-full px-3 py-1"
            v-model.number="random_state"
          />
        </div>

        <h2>Train settings</h2>
        <div class="flex mb-2">
          <label
            for="epochs"
            class="w-1/4 mr-4 text-lg font-medium text-gray-900"
            >Epochs</label
          >
          <input
            type="number"
            id="epochs"
            name="epochs"
            class="border border-1 border-gray-500 rounded w-full px-3 py-1"
            v-model.number="epochs"
          />
        </div>
        <div class="flex mb-2">
          <label
            for="patience"
            class="w-1/4 mr-4 text-lg font-medium text-gray-900"
            >Patience</label
          >
          <input
            type="number"
            id="patience"
            name="patience"
            class="border border-1 border-gray-500 rounded w-full px-3 py-1"
            v-model.number="patience"
          />
        </div>
        <div class="flex mb-2">
          <label
            for="earlyStopping"
            class="mr-20 text-lg font-medium text-gray-900"
            >EarlyStopping</label
          >
          <input
            type="checkbox"
            id="earlyStopping"
            name="earlyStopping"
            checked="checked"
            disabled="true"
            class="border border-1 border-gray-500 rounded mt-2 mr-4 cursor-not-allowed"
            style="transform: scale(1.5)"
          />
          <label for="earlyStopping" class="text-lg"> true</label>
        </div>
        <button
          type="submit"
          class="text-lg bg-green-400 rounded shadow px-4 py-1 text-white hover:bg-green-500 mt-4"
        >
          Train
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Settings",
  data() {
    return {
      history_window: 15,
      future_window: 30,
      shift: 1,
      random_state: 0,
      epochs: 25,
      patience: 5,
    };
  },
  methods: {
    train() {
      this.$http
        .post("/api/model/create", {
          history_window: parseInt(this.history_window),
          future_window: parseInt(this.future_window),
          shift: parseInt(this.shift),
          random_state: parseInt(this.random_state),
          epochs: parseInt(this.epochs),
          patience: parseInt(this.patience),
        })
    },
  },
};
</script>

<style scoped>
button:hover {
  transform: scale(1.05);
}
</style>
