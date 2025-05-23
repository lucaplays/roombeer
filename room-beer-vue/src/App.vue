<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/cntrl">Control</router-link>
  </nav>
  <router-view />
</template>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
}

nav {
  padding: 30px;
  position: fixed;
  width: 100%;
  z-index: 1;
}

nav a {
  font-weight: bold;
  color: white;
  background-color: black;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
