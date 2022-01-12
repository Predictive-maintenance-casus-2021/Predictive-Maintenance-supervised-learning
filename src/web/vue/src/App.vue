<template>
  <div id="app">
    <!--- The menu on the left --->
    <div>

    </div>
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Vue is working on the server!" />
    <NavigationBar></NavigationBar>
  </div>
</template>

<script>
// ToDo: get rid of
// Test imports
import HelloWorld from "./components/HelloWorld.vue";

// All imports
import NavigationBar from "./components/NavBar.vue";


export default {
  name: "App",
  components: {
    NavigationBar,
    HelloWorld
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
