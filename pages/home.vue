<template>
    <v-container>
        <v-row>
            <v-col :cols="10">
                <MonthChart class="mx-auto" />
            </v-col>
            <v-col :cols="2">
                <CongestionChart class="mx-auto" />
            </v-col>  
        </v-row>    
        <v-row>
            <v-col :cols="6">
                <SpotsMap class="mx-auto" />
            </v-col> 
            <v-col :cols="6">
                <DayChart class="mx-auto" />
            </v-col>  
        </v-row>    
    </v-container>
</template>

<script>
import MonthChart from "~/components/Dashboard/ViolationChart.vue";
import CongestionChart from "~/components/Dashboard/CongestionChart.vue";
import DayChart from "~/components/Dashboard/DayChart.vue";
import SpotsMap from "~/components/Dashboard/SpotsMap.vue";

export default {
    name: "IndexPage",
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        MonthChart,
        CongestionChart,
        DayChart,
        SpotsMap
    }
}
</script>
