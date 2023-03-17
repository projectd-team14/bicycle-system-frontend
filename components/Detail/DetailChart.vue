<template>
    <v-card
        class="mx-auto"
        max-height="705"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title
                class="headline"
                style="width: 15%;"
            >
                <v-select
                    v-model="chartType" 
                    :items="items"
                    @change="onClickSelectButton(chartType)"
                >
                </v-select>
            </v-card-title>
            <div v-if="chartType=='１日'" style="height: 350px;">
                <DetailDayChartData :styles="chartStyles" /> 
            </div>
            <div v-else-if="chartType=='１週間'" style="height: 350px;">
                <DetailWeekChartData :styles="chartStyles" /> 
            </div>
            <div v-else-if="chartType=='１ヶ月'" style="height: 350px;">
                <DetailOneMonthChartData :styles="chartStyles" /> 
            </div>
            <div v-else-if="chartType=='３ヶ月'" style="height: 350px;">
                <DetailThreeMonthChartData :styles="chartStyles" /> 
            </div>
        </v-card-item>
    </v-card>
</template>
  
<script>
import DetailDayChartData from '~/components/Detail/DetailDayChartData.vue'
import DetailWeekChartData from '~/components/Detail/DetailWeekChartData.vue'
import DetailOneMonthChartData from '~/components/Detail/DetailOneMonthChartData.vue'
import DetailThreeMonthChartData from '~/components/Detail/DetailThreeMonthChartData.vue'

export default {
    components: {
        DetailDayChartData,
        DetailWeekChartData,
        DetailOneMonthChartData,
        DetailThreeMonthChartData
    },
    data() {
        return{
            height: 100,
            chartType: "１日",
            items: ["１日", "１週間", "１ヶ月", "３ヶ月"]
        }
    },
    computed: {
        chartStyles() {
            return{
                height: `${this.height}%`,
                position:'relative'
            }
        }
    },
    methods: {
        onClickSelectButton(chartType) {

        }
    }
}
</script>