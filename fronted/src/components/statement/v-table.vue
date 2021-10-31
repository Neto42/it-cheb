<template>

  <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
    <vTAbleThead v-bind:column="column"/>

    <tbody v-for="result in results">
    <tr>
      <td>{{ result.email_user }}</td>
      <td>{{ result.city }}</td>
      <td>{{ result.gender }}</td>
      <td>{{ result.age }}</td>
      <td>{{ result.social }}</td>
      <td>{{ result.complaint }}</td>
      <td>{{ result.date }}</td>
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