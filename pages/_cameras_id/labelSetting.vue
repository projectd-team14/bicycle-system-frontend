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
                        <LabelSetting class="mx-auto" />
                    </v-col>
                </v-row>            
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CameraList from "~/components/List/CameraList.vue";
import LabelSetting from "~/components/Setting/LabelSetting.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        CameraList,
        LabelSetting
    }
}
</script>
