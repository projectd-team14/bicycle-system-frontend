<template>
    <v-card
        class="mx-auto"
        max-height="705"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">自転車設定<v-icon>mdi-minus</v-icon>{{ this.cameraName }}</v-card-title>
            <v-col cols="12">               
            </v-col>
        </v-card-item>
    </v-card>
</template>
  
<script>
export default {
    data() {
        return {
            cameraName: "None",
        }
    },
    mounted() {
        var camerasData = this.$store.state.cameraData.cameraData;

        for (let i = 0; i < camerasData.length; i++) {
            if (camerasData[i].cameras_id == this.$route.params.cameras_id) {
                this.cameraName = camerasData[i].cameras_name;

                break;
            }
        }
    },
    methods: {
    }
}
</script>