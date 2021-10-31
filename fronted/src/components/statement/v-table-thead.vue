<template>
  <thead class="table-info">
  <tr>
    <th>{{ column.email_user }}</th>
    <th>{{ column.city }}</th>
    <th>{{ column.gender }}</th>
    <th>{{ column.age }}</th>
    <th>{{ column.social }}</th>
    <th>{{ column.complaint }}</th>
    <th>{{ column.date }}</th>
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