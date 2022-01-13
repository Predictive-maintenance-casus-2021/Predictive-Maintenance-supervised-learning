<script>
import { Line } from 'vue-chartjs';

export default {
  name: "LineChart",
  extends: Line,
  props: ['data'],
  mounted() {
    this.renderChart(this.data)
  }
}
</script>