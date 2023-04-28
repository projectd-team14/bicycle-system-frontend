<template>
    <v-container>
        <v-row>
            <v-col :cols="2">
                <v-row>
                    <v-col :cols="12">
                        <CameraList class="mx-auto" />
                    </v-col>
                    <v-col :cols="12">
                        <SpotDelete class="mx-auto" />
                    </v-col>
                </v-row>            
            </v-col>
            <v-col :cols="10">
                <v-row>
                    <v-col :cols="12">
                        <DetailChart class="mx-auto" />
                    </v-col>
                    <v-col :cols="12">
                        <DetailBarChart class="mx-auto" />
                    </v-col>
                </v-row>            
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CameraList from "~/components/List/CameraList.vue";
import SpotDelete from "~/components/Setting/SpotDelete";
import DetailChart from "~/components/Detail/DetailChart.vue";
import DetailBarChart from "~/components/Detail/DetailBarChart.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        CameraList,
        SpotDelete,
        DetailChart,
        DetailBarChart
    }
}
</script>