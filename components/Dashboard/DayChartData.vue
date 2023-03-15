<script>
import { Line } from 'vue-chartjs'

export default {
    extends: Line,
    data(){
        return {
            chartdata: {
                labels: [],
                datasets: []
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    labels: {
                        fontColor: "rgba(255, 255, 255, 10)"
                    }
                },
                scales: {
                    xAxes: [
                        {
                            ticks: {
                                fontColor: "rgba(255, 255, 255, 10)"
                            }
                        }
                    ],
                    yAxes: [
                        {
                            ticks: {
                                fontColor: "rgba(255, 255, 255, 10)"
                            }
                        }
                    ]
                }
            }
        }
    },
    computed: {
        getHomeData: function() {
            return this.$store.getters["homeData/getHomeData"];
        }
    },
    watch: {
        getHomeData(values) {
            this.chartdata.labels = [...Array(24)].map((_, i) => i);

            for (let i = 0; i < values.length; i++) {
                const dataset = {
                    label: values[i].name,
                    data: values[i].count_day1,
                    borderColor: values[i].border_color,
                    lineTension: 0,
                    borderWidth: 3,
                    fill: false
                }
                this.chartdata.datasets.push(dataset);
                this.renderChart(this.chartdata, this.options);
            }  
        }
    }
}
</script>