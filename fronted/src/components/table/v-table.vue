<template>

  <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
    <vTAbleThead v-bind:column="column"/>

    <tbody v-for="result in results">
    <tr>
      <td>{{ result.street }}</td>
      <td>{{ result.object_type }}</td>
      <td>{{ result.rezult }}</td>
    </tr>
    </tbody>
  </table>

</template>

<script>
import vTAbleThead from './v-table-thead'

export default {
  name: "v-table",
  components: {
    vTAbleThead
  },

  props: [
    'results',
    'column'
  ],
}
</script>

<style scoped>

</style>