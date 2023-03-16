<template>
    <v-container>
        <v-row>
            <v-col :cols="2">
                <SpotDetail class="mx-auto" />
            </v-col>  
        </v-row>
    </v-container>
</template>

<script>
import SpotDetail from "~/components/Detail/SpotDetail.vue";

export default {
    layout: "HomeLayout",
    middleware: "auth",
    components: {
        SpotDetail
    }
}
</script>
