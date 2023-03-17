<template>
    <div>
        <v-card
            class="mx-auto"
            max-height="600"
            style="background: #2c2d3f;"
        > 
            <v-card-item>
                <v-card-title class="headline">削除</v-card-title>
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
    </div>
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