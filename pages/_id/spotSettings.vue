<template>
    <v-container>    
        <v-row>
            <v-col :cols="12">
                <SpotSettings class="mx-auto" />
            </v-col>  
        </v-row>    
    </v-container>
</template>

<script>
import SpotSettings from "~/components/Settings/SpotSettings.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        SpotSettings
    }
}
</script>