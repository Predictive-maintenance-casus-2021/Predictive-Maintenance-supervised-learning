<template>
  <div
    class="absolute h-full w-24 left-0 top-0 bg-green-700 items-center justify-center py-5 shadow rounded-br-lg rounded-tr-lg"
  >
    <div class="align-center inline-grid gap-9">
      <button
        @click="home"
        v-on:click="pageName = 'home'"
        class="hover:scale-125 transition-transform transform"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-12 w-12 fill-current text-gray-200 drop-shadow-md hover:text-white"
          viewBox="0 0 20 20"
        >
          <path
            d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"
          />
        </svg>
      </button>

      <button class="hover:scale-125 transition-transform transform">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-12 w-12 fill-current text-gray-200 drop-shadow-md hover:text-white"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z"
            clip-rule="evenodd"
          />
        </svg>
      </button>

      <button class="hover:scale-125 transition-transform transform">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-12 w-12 fill-current text-gray-200 drop-shadow-md hover:text-white"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z"
            clip-rule="evenodd"
          />
        </svg>
      </button>

      <button
        @click="info"
        v-on:click="pageName = 'info'"
        class="hover:scale-125 transition-transform transform"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-12 w-12 fill-current text-gray-200 drop-shadow-md hover:text-white"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
            clip-rule="evenodd"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      pageName: this.pageName,
    };
  },
  methods: {
    home() {
      this.$http
        .get("/home")
        .then(() => {
          console.log("Go to home");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    info() {
      this.$http
        .get("/info")
        .then(() => {
          console.log("Go to info");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
