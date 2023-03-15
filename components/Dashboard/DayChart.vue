<template>
    <v-card
        class="mx-auto"
        max-height="420"
        style="background: linear-gradient(#14F3FF, #6E00B2);"
    > 
        <v-card-item>
            <v-card-title class="headline">駐輪場状況</v-card-title>
            <div style="height: 350px;">
                <DayChartData :styles="chartStyles" /> 
            </div>               
        </v-card-item>
    </v-card>            
</template>
  
<script>
import DayChartData from '~/components/Dashboard/DayChartData.vue'
  
export default {
    components: {
        DayChartData
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