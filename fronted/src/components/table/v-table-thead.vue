<template>
  <thead class="table-info">
  <tr>
    <th>{{ column.street }}</th>
    <th>{{ column.object_type }}</th>
    <th>{{ column.result }}</th>
  </tr>
  </thead>
</template>

<script>
export default {
  name: "v-table-thead",
  props: [
    'column'
  ]
}
</script>

<style scoped>

</style>