<template>
    <v-container>    
        <v-row>
            <v-col :cols="12">
                <SpotRegister class="mx-auto" />
            </v-col>  
        </v-row>    
    </v-container>
</template>

<script>
import SpotRegister from "~/components/Settings/SpotRegister.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        SpotRegister
    }
}
</script>
