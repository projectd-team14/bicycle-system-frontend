<script>
import { Line } from 'vue-chartjs'

export default {
    extends: Line,
    data(){
        return {
            chartdata: {
                chart: [],
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
    mounted() {
        const values =this.$store.getters["spotData/getSpotData"];
        this.createChart(values);
    },
    computed: {
        getHomeData: function() {
            return this.$store.getters["spotData/getSpotData"];
        }
    },
    watch: {
        getHomeData(values) {
            this.createChart(values);
        }
    },
    methods: {
        createChart(values) {
            var borderColor = "";
            var spots = this.$store.state.homeData.homeData;

            for (let i = 0; i < spots.length; i++) {
                if (spots[i].id == this.$route.params.spots_id) {
                    borderColor = spots[i].border_color;

                    break;
                }
            }

            if (typeof values.situationChartData !== 'undefined') {
                const spotData = values.situationChartData
                const dataset = {
                        label: spotData[0].label,
                        data: spotData[0].data,
                        borderColor: borderColor,
                        lineTension: 0,
                        borderWidth: 3,
                        fill: false
                    }
                this.chartdata.labels = spotData[0].labels;
                this.chartdata.datasets = [];
                this.chartdata.datasets.push(dataset);
                this.renderChart(this.chartdata, this.options);
            }
        }
    }
}
</script>