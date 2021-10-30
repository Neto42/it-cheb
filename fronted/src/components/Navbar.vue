<template>
  <div class="navbar-brand">
    <router-link class="navbar-item" to="/">
      <img src="../assets/logo.png"/>
      <strong>БлагоЧувашии</strong>
    </router-link>
  </div>

  <div class="navbar-menu">
    <div class="navbar-end">
      <router-link class="navbar-item" to="/">Главная</router-link>
      <router-link class="navbar-item" to="/about">FAQ</router-link>
      <router-link class="navbar-item" to="/contact">Контакты</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>

</style>