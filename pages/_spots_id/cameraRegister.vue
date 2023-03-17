<template>
    <v-container>    
        <v-row>
            <v-col :cols="2">
                <CameraList class="mx-auto" />
            </v-col> 
            <v-col :cols="10">
                <CameraRegister class="mx-auto" />
            </v-col>  
        </v-row>    
    </v-container>
</template>

<script>
import CameraList from "~/components/List/CameraList.vue";
import CameraRegister from "~/components/Setting/CameraRegister.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        CameraList,
        CameraRegister
    }
}
</script>