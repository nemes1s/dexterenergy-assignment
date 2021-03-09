<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <date-range-picker :from="$route.query.from" :to="$route.query.to" :panel="$route.query.panel" @update="update"/>
    <div v-if="chartData.length">Chart</div>
  </div>
</template>

<script>
import myApi from '../myApi.js';
export default {
  name: 'NlDeFlow',
  data() {
    return { chartData: [] }
  },
  props: {
    msg: String,
  },
  methods: {
    getData () {
      myApi.get().then(response => this.chartData = response)
    },
    update(values) {
      this.$router.push({ query: Object.assign({}, this.$route.query, {
        to: values.to,
        from: values.from,
        panel: values.panel
      }) })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
