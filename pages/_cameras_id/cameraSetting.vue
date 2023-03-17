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
                        <CameraView class="mx-auto" />
                    </v-col>
                    <v-col :cols="12">
                        <CameraSetting class="mx-auto" />
                    </v-col> 
                </v-row>            
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CameraList from "~/components/List/CameraList.vue";
import CameraView from "~/components/Setting/CameraView.vue";
import CameraSetting from "~/components/Setting/CameraSetting.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        CameraList,
        CameraView,
        CameraSetting
    }
}
</script>
