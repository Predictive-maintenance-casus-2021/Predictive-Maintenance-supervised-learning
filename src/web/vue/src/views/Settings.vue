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

      <form>
        <!--
      Minuten in de toekomst voorspellen
      Lookback
      Early stopping
      Epochs
      Shift
      -->
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
            class="border border-1 border-gray-500 rounded mt-2 mr-4"
            style="transform: scale(1.5)"
          />
          <label for="earlyStopping" class="text-lg"> true</label>
        </div>
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
          />
        </div>
        <button
          type="submit"
          class="text-lg bg-green-400 rounded shadow px-4 py-1 text-white hover:bg-green-500 mt-4"
        >
          Save
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
      predictMinFuture: 1,
      lookback: 0,
      patience: 0,
      epochs: 50,
      shift: 0,
    };
  },
};
</script>

<style scoped>
button:hover {
  transform: scale(1.05);
}
</style>
