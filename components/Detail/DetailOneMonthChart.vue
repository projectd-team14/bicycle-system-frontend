<template>
    <v-card
        class="mx-auto"
        max-height="705"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">詳細データ</v-card-title>
            <div style="height: 350px;">
                <DetailOneMonthChartData :styles="chartStyles" /> 
            </div>               
        </v-card-item>
    </v-card>
</template>
  
<script>
import DetailOneMonthChartData from '~/components/Detail/DetailOneMonthChartData.vue'
  
export default {
    components: {
        DetailOneMonthChartData
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