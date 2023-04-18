<template>
    <v-container>
        <v-row>
            <v-col :cols="2">
                <v-row>
                    <v-col :cols="12">
                        <CameraList class="mx-auto" />
                    </v-col>   
                    <v-col :cols="12">
                        <BackButton class="mx-auto" />
                    </v-col>             
                </v-row>            
            </v-col>
            <v-col :cols="10">
                <v-row>
                    <v-col :cols="12">
                        <CameraView class="mx-auto" />
                    </v-col>
                    <v-col :cols="8">
                        <CameraSwitch class="mx-auto" />
                    </v-col> 
                    <v-col :cols="4">
                        <CameraDelete class="mx-auto" />
                    </v-col> 
                </v-row>            
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CameraList from "~/components/List/CameraList.vue";
import CameraView from "~/components/Setting/CameraView.vue";
import CameraSwitch from "~/components/Setting/CameraSwitch.vue";
import CameraDelete from "~/components/Setting/CameraDelete.vue";
import BackButton from "~/components/Setting/BackButton.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        CameraList,
        CameraView,
        CameraSwitch,
        CameraDelete,
        BackButton
    }
}
</script>
