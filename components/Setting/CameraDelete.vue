<template>
    <v-row>
        <v-col cols="12">
            <v-card
                class="mx-auto"
                max-height="600"
                style="background: #2c2d3f;"
            > 
                <v-card-item>
                        <v-col cols="12">
                            <v-btn
                                block
                                outlined
                                color="#e00083" 
                                @click="onClickDeleteButton()"
                            >
                                Delete
                            </v-btn> 
                        </v-col>                        
                </v-card-item>
            </v-card>
            <v-snackbar
                v-model="snackBar"
                multi-line
                color="secondary"
            >
                {{ snackText }}
            </v-snackbar>  
        </v-col>            
    </v-row>
</template>
  
<script>
export default {
    data() {
        return {
            snackText: "",
            snackBar: false
        }
    },
    methods: {
        onClickDeleteButton() {
            this.$axios.get("/api/delete_camera/" + this.$route.params.cameras_id)
            .then((response) => {
                const spotsId = String(response.data.spots_id);
                this.onLoadCameraData(spotsId);
                this.$router.push("/" + spotsId + "/spotDetail");
            })
        },
        async onLoadCameraData(spotsId) {
            this.$store.dispatch("cameraData/onLoadCameraData", {
                spotsId: spotsId
            });
        }
    }
}
</script>