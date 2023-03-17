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
            return this.$store.getters["spotData/getSpotData"];
        }
    },
    watch: {
        getHomeData(values) {
            var borderColor = "";
            var spots = this.$store.state.homeData.homeData;

            for (let i = 0; i < spots.length; i++) {
                if (spots[i].id == this.$route.params.spots_id) {
                    borderColor = spots[i].border_color;

                    break;
                }
            }
            
            const spotData = values.situationChartData
            const dataset = {
                    label: spotData[2].label,
                    data: spotData[2].data,
                    borderColor: borderColor,
                    lineTension: 0,
                    borderWidth: 3,
                    fill: false
                }
            this.chartdata.labels = spotData[2].labels;
            this.chartdata.datasets.push(dataset);
            this.renderChart(this.chartdata, this.options);
        }
    }
}
</script>