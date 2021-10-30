<template>
  <nav class="navbar is-success" role="navigation" aria-label="main navigation">
    <Navbar />
  </nav>
  <router-view/>
</template>

<script>
import Navbar from "./components/Navbar";

export default {
  components: {
    Navbar
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

</style>
