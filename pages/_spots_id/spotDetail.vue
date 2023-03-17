<template>
    <v-container>
        <v-row>
            <v-col :cols="2">
                <v-row>
                    <v-col :cols="12">
                        <CameraList class="mx-auto" />
                    </v-col>            
                </v-row>            
            </v-col>
            <v-col :cols="10">
                <v-row>
                    <v-col :cols="12">
                        <DetailDayChart class="mx-auto" />
                    </v-col>
                </v-row> 
                <v-row>
                    <v-col :cols="12">
                        <DetailWeekChart class="mx-auto" />
                    </v-col>
                </v-row>  
                <v-row>
                    <v-col :cols="12">
                        <DetailOneMonthChart class="mx-auto" />
                    </v-col>
                </v-row>   
                <v-row>
                    <v-col :cols="12">
                        <DetailThreeMonthChart class="mx-auto" />
                    </v-col>
                </v-row>            
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CameraList from "~/components/List/CameraList.vue";
import DetailDayChart from "~/components/Detail/DetailDayChart.vue";
import DetailWeekChart from "~/components/Detail/DetailWeekChart.vue";
import DetailOneMonthChart from "~/components/Detail/DetailOneMonthChart.vue";
import DetailThreeMonthChart from "~/components/Detail/DetailThreeMonthChart.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        CameraList,
        DetailDayChart,
        DetailWeekChart,
        DetailOneMonthChart,
        DetailThreeMonthChart
    }
}
</script>