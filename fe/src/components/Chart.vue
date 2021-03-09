<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  props: ["chartdata", "options"],
  mounted() {
    const chartData = {
      datasets: [
        {
          backgroundColor: "#fc6c71",
          label: "NL/DE flow",
          data: this.chartdata,
        },
      ],
    };
    const options = {
      scales: {
        xAxes: [
          {
            type: "time",
            time: {
              unit: "hour",
              round: "hour",
              displayFormats: {
                hour: "D-MM-YYYY h:mm",
              },
            },
            offset: true,
          },
        ],
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
      parsing: {
        xAxisKey: "index",
        yAxisKey: "value",
      },
    };
    this.renderChart(chartData, options);
  },
};
</script>

<style></style>
