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
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">Таблицы</a>
        <div class="navbar-dropdown">
          <router-link class="navbar-item" to="/statement">
            Заявка
          </router-link>
          <router-link class="navbar-item" to="/table">
            Вывод
          </router-link>
        </div>
      </div>
      <router-link class="navbar-item" to="/faq">FAQ</router-link>
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