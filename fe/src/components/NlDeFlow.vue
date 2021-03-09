<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="flex-row">
      <div class="datepicker">
        <date-range-picker
          :from="$route.query.from"
          :to="$route.query.to"
          :panel="$route.query.panel"
          allowFrom="2020-03-09"
          :allowTo="allowTo"
          @update="update"
        />
      </div>
      <div v-if="showChart" class="chart"><Chart v-bind:chartdata="chartData" /></div>
    </div>
  </div>
</template>

<script>
import myApi from "../myApi.js";
import Chart from "@/components/Chart.vue";
export default {
  name: "NlDeFlow",
  components: { Chart },
  data() {
    return { 
      chartData: null,
      allowTo: new Date().toISOString(),
      showChart: false
      };
  },
  props: {
    msg: String,
  },
  methods: {
    getData(from, to) {
      myApi.get('/',{params: { start:from, end:to }}).then((response) => {
        this.chartData = response.data.map(i => ({x: i.index, y: i.value}))
        this.showChart = true
      });
    },
    update(values) {
      this.$router.push({
        query: Object.assign({}, this.$route.query, {
          to: values.to,
          from: values.from,
          panel: values.panel,
        }),
      });

      this.showChart = false

      this.getData(values.from, values.to);
    },
  },
};
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
.datepicker {
  width: 404px;
}
.flex-row {
  display: flex;
}
.chart {
  flex-grow: 1;
  max-width: 800px;
}
</style>
