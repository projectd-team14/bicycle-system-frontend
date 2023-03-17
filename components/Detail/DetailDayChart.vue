<template>
    <v-card
        class="mx-auto"
        max-height="705"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">詳細データ</v-card-title>
            <div style="height: 350px;">
                <DetailDayChartData :styles="chartStyles" /> 
            </div>               
        </v-card-item>
    </v-card>
</template>
  
<script>
import DetailDayChartData from '~/components/Detail/DetailDayChartData.vue'
  
export default {
    components: {
        DetailDayChartData
    },
    data() {
        return{
            height: 100
        }
    },
    computed:{
        chartStyles() {
            return{
                height: `${this.height}%`,
                position:'relative'
            }
        }
    }
}
</script>