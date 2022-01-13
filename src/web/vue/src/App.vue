<template>
  <div id="app" class="font-sans flex h-screen w-screen">
    <navigation />

    <div class="w-full mt-4 px-4 lg:px-32">
      <router-view />
    </div>
  </div>
</template>

<script>
import Navigation from "./components/Navigation";

export default {
  components: {
    Navigation,
  },
};
</script>
