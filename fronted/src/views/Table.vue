<template>
    <v-table v-bind:results="allResults" :column="column"/>
</template>

<script>
import vTable from "../components/table/v-table"
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'Table',
  components: {
    vTable
  },
  data() {
    return {
      column: {
        street: 'Улица',
        object_type: 'Объект',
        result: 'Вывод',
      }
    }
  },
  computed: mapGetters(['allResults']),
  methods: mapActions(['results']),
  mounted() {
    this.results('network/rezult/')
  }
}
</script>

<style scoped>

</style>