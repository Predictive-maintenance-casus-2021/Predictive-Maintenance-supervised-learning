<template>
  <div id="app">
    <!--- The menu on the left --->
    <NavBar />
    <InfoPage v-if="pageName === 'info'"> </InfoPage>
  </div>
</template>

<script>
// All imports
import InfoPage from "./pages/InfoPage";
import NavBar from "./components/NavBar";

export default {
  name: "App",
  data: function () {
    return {
      pageName: this.pageName,
    };
  },
  components: {
    NavBar,
    InfoPage,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
