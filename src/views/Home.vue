<template>
  <div id="app">
    <div id="nav">
      <input v-model="name" v-on:keyup="key" />
      <a href="#" v-on:click="newGame">Новая игра</a> |
      <router-link to="/rating">Рейтинг игроков</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    name
  }),
  methods: {
    key(e) {
      if (e.keyCode === 13) this.newGame();
    },
    newGame() {
      if (this.name === "") {
        alert("Введите имя");
        return;
      }
      this.$store.commit("name", this.name);
      this.$router.push("/game");
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
