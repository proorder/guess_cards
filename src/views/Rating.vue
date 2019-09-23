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
    winners = JSON.parse(winners);
    winners.sort((a, b) => {
      if (a.time < b.time) {
        return 1;
      }
      if (a.time > b.time) {
        return -1;
      }
      return 0;
    });
    this.winners = winners;
  }
};
</script>
