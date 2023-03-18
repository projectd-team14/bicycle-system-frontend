<template>
    <v-row>
        <v-col cols="12">
            <v-card
                class="mx-auto"
                max-height="770"
                style="background: #2c2d3f;"
            > 
                <v-card-item>
                    <v-card-title class="headline">動作設定<v-icon>mdi-minus</v-icon>{{ this.cameraName }}</v-card-title>
                    <v-col cols="12">
                        <iframe
                            width="100%"
                            height="680"
                            :src="this.cameraUrl"
                            title="YouTube video player"
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                            allowfullscreen
                        >
                        </iframe>                       
                    </v-col>
                </v-card-item>
            </v-card>
        </v-col>            
    </v-row>
</template>
  
<script>
export default {
    data() {
        return {
            cameraName: "None",
            cameraUrl: "", 
            camerasData: [],
            snackText: "",
            snackBar: false
        }
    },
    mounted() {
        if (typeof this.$store.state.cameraData.cameraData == 'undefined') {
            return;
        }

        var camerasData = this.$store.state.cameraData.cameraData;

        for (let i = 0; i < camerasData.length; i++) {
            if (camerasData[i].cameras_id == this.$route.params.cameras_id) {
                this.cameraName = camerasData[i].cameras_name;
                let url = camerasData[i].cameras_url;
                this.cameraUrl = url.replace('watch?v=', 'embed/');

                break;
            }
        }
    },
    methods: {
        onClickStartButton() {
            this.$axios.get("/api/start/" + this.$route.params.cameras_id)
            .then((response) => {
                this.snackText = response.data.message;
                this.snackBar = true;
            })
        },
        onClickStopButton() {
            this.$axios.get("/api/stop/" + this.$route.params.cameras_id)
            .then((response) => {
                this.snackText = response.data.message;
                this.snackBar = true;
            })
        },
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