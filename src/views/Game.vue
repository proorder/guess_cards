<template>
  <div class="game">
    <div class="panel">
      <div>Время: {{ time }}</div>
      <div><a href="#" v-on:click="$router.go(-1)">Назад</a></div>
    </div>
    <div class="field">
      <div
        v-for="(el, key) in mymap"
        :key="key"
        class="card_container"
        :class="{ active: active.indexOf(key) !== -1 }"
        v-on:click="choice(key, el)"
      >
        <div class="card">
          <div class="card_front">
            <img :src="cover" />
          </div>
          <div class="card_back">
            <img :src="el.value" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    mymap: [],
    active: [],
    current: null,
    time: 0,
    timer: null,
    currentTimeOut: null
  }),
  methods: {
    addWinner() {
      let winners = localStorage.getItem("winners");
      winners = JSON.parse(winners);
      if (winners === null) winners = [];
      winners.push({ name: this.$store.getters.getName, time: this.time });
      localStorage.setItem("winners", JSON.stringify(winners));
    },
    choice(key, el) {
      if (
        this.active[this.active.length - 1] === key ||
        this.active.indexOf(key) !== -1
      ) {
        return;
      }
      if (this.current === el.value) {
        this.active.push(key);
        clearTimeout(this.currentTimeOut);
        this.currentTimeOut = null;
        if (this.active.length === 36) {
          this.addWinner();
          clearInterval(this.timer);
          alert("Congratulation!");
        }
        return;
      } else {
        this.current = el.value;
      }
      if (this.currentTimeOut !== null) {
        clearTimeout(this.currentTimeOut);
        this.currentTimeOut = null;
        this.active.pop();
      }
      this.active.push(key);
      this.currentTimeOut = setTimeout(() => {
        this.active.pop();
        this.currentTimeOut = null;
      }, 5000);
    }
  },
  created() {
    this.cover = require("../assets/cover.jpg");
    this.card_names = [
      "Sunflower2.png",
      "Squash.png",
      "Cactus1.png",
      "Iceshromm2.png",
      "Grave_Buster1.png",
      "Gatling_Pea1.png",
      "Cob_Cannon2.png",
      "Torchwood1.png",
      "Holographic_Tall_Nut2.png",
      "Stallia2.png",
      "Lord_Bamboo.png",
      "Pitaya2.png",
      "Chomper1.png",
      "Tall-nut2.png",
      "Explode-o-nut2.png",
      "Marigold1.png",
      "Melon-pult1.png",
      "Repeater1.png"
    ];
    let arr = [];
    for (let i = 0; i < 18; i++) {
      arr.push(i);
      arr.push(i);
    }
    this.mymap = arr;
    let arr_shuffle = [];
    while (arr.length > 0) {
      let index = parseInt(Math.random() * arr.length);
      arr_shuffle.push({
        value: require("../assets/PZ/" + this.card_names[arr[index]])
      });
      arr.splice(index, 1);
    }
    this.mymap = arr_shuffle;
    this.timer = setInterval(() => {
      this.time += 1;
    }, 1000);
    this.addWinner();
  }
};
</script>

<style lang="scss" scoped>
.field {
  display: grid;
  grid-template-columns: repeat(6, 100px);
  grid-template-rows: repeat(6, 120px);
  grid-gap: 5px;
  justify-content: center;
  align-content: center;
}
.card_container {
  perspective: 1000;
  width: 100px;
  height: 120px;
}
.card_container.active .card {
  transform: rotateY(180deg);
}
.card {
  transition: 0.6s;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  position: relative;
  & > div {
    width: 100px;
    height: 120px;
    backface-visibility: hidden;
    position: absolute;
    top: 0;
    left: 0;
  }
}
.card_front {
  z-index: 2;
}
.card_back {
  transform: rotateY(180deg);
}
.panel {
  display: flex;
  justify-content: space-around;
}
</style>
