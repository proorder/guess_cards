<template>
  <div class="rating">
    <h1>This is a rating page</h1>
    <ul>
      <li v-for="(el, key) in winners" :key="key">
        Name: {{ el.name }}, Time: {{ el.time }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data: () => ({
    winners: []
  }),
  created() {
    let winners = localStorage.getItem("winners");
    this.winners = JSON.parse(winners);
  }
};
</script>
