<template>
    <v-card
        class="mx-auto"
        max-height="705"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">台数分布</v-card-title>
            <div style="height: 350px;">
                <DetailBarChartData :styles="chartStyles" /> 
            </div>               
        </v-card-item>
    </v-card>
</template>
  
<script>
import DetailBarChartData from '~/components/Detail/DetailBarChartData.vue'
  
export default {
    components: {
        DetailBarChartData
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