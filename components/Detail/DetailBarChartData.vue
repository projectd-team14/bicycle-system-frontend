<script>
import { HorizontalBar } from 'vue-chartjs'

export default {
    extends: HorizontalBar,
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
            var backgroundColor = "";
            var spots = this.$store.state.homeData.homeData;
            var labels = ["~1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12~"]

            for (let i = 0; i < spots.length; i++) {
                if (spots[i].id == this.$route.params.spots_id) {
                    borderColor = spots[i].border_color;
                    backgroundColor = spots[i].border_color;

                    break;
                }
            }

            if (typeof values.numberChartData !== 'undefined') {
                const spotData = values.numberChartData
                const dataset = {
                        label: spotData[0].label,
                        data: spotData[0].data,
                        borderColor: borderColor,
                        backgroundColor: backgroundColor,
                        lineTension: 0,
                        borderWidth: 3,
                        fill: false
                    }
                this.chartdata.labels = labels;
                this.chartdata.datasets = [];
                this.chartdata.datasets.push(dataset);
                this.renderChart(this.chartdata, this.options);
            }
        }
    }
}
</script>