<template>
    <v-container>    
        <v-row>
            <v-col :cols="12">
                <CameraRegister class="mx-auto" />
            </v-col>  
        </v-row>    
    </v-container>
</template>

<script>
import CameraRegister from "~/components/Settings/CameraRegister.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        CameraRegister
    }
}
</script>