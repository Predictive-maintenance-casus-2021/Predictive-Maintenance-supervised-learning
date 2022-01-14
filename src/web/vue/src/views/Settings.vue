<template>
  <div>
    <h1 class="text-4xl text-gray-900 font-bold">Settings</h1>
    <div class="flex justify-center">
      <div
        class="border border-1 shadow-xl rounded mt-8 w-5/6 h-2/3 absolute"
      >
        <div class="mt-4 ml-4">
          <a class="flex justify-center text-2xl font-medium"
            >Algemene informatie</a
          >
          <a class="flex justify-center text-lg"
            >Inzien / inladen / ontwerpen modellen</a
          >
        </div>
      </div>
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
      earlyStopping: false,
      epochs: 50,
      shift: 0,
    };
  },
};
</script>

<style scoped></style>
