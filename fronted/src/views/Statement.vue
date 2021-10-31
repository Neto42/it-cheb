<template>
  <v-table v-bind:results="allResults" v-bind:column="column"/>
</template>

<script>
import vTable from "../components/statement/v-table"
import {mapGetters, mapActions} from 'vuex'

export default {
  name: "Statement",

  components: {
    vTable
  },
  data() {
    return {
      column: {
        email_user: 'Почта',
        city: 'Город',
        gender: 'Пол',
        age: 'Возраст',
        social: 'Социальный статус',
        complaint: 'Жалоба',
        date: 'Дата',
      }
    }
  },
  computed: mapGetters(['allResults']),
  methods: mapActions(['results']),
  mounted() {
    this.results('statement/')
  }
}
</script>

<style scoped>

</style>