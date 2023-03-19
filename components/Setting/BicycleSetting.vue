<template>
    <v-row>
        <v-col cols="12">
            <v-card
                class="mx-auto box"
                max-height="705"
                style="background: #2c2d3f;"
            > 
                <v-card-item>
                    <v-card-title class="headline">自転車設定<v-icon>mdi-minus</v-icon>{{ this.cameraName }}</v-card-title>
                    <v-row>
                        <template v-for="(bicycle, i) in bicycleImagesData">
                            <v-col cols="3">
                                <v-row>
                                    <v-col cols="12">
                                        <div class="mx-5">
                                            <img 
                                                id="img_source" 
                                                :src="bicycle.bicycles_url"
                                                style="width: 100%; height: 100%;"
                                            >  
                                        </div>
                                    </v-col>
                                </v-row>
                            </v-col>                        
                        </template>                        
                    </v-row>
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
            imageSrc: "",
            spots_id: 0,
            bicycleImagesData: []
        }
    },
    mounted() {
        const camerasData = this.$store.state.cameraData.cameraData;

        for (let i = 0; i < camerasData.length; i++) {
            if (camerasData[i].cameras_id == this.$route.params.cameras_id) {
                this.cameraName = camerasData[i].cameras_name;
                this.spots_id = camerasData[i].spots_id;

                break;
            }
        }

        const homeData = this.$store.state.homeData.homeData;
        let situationData = [];

        for (let i = 0; i < homeData.length; i++) {
            if (homeData[i].id == this.spots_id) {
                situationData = homeData[i].situation;

                break;
            }
        }

        for (let i = 0; i < situationData.length; i++) {
            for (let j = 0; j < situationData[i].bicycle.length; j++) {
                if (situationData[i].bicycle[j].cameras_id == this.$route.params.cameras_id) {
                    const data = {
                        labels_name: situationData[i].row,
                        bicycles_id: situationData[i].bicycle[j].id,
                        bicycles_status: situationData[i].bicycle[j].violatin_status,
                        bicycles_url: this.$config.fastURL + "/bicycle/?camera_id=" + this.$route.params.cameras_id + "&bicycle_id=" + situationData[i].bicycle[j].id
                    }

                    this.bicycleImagesData.push(data);
                }
            }
        }
        
        console.log(this.bicycleImagesData);
        // this.imageSrc = this.$config.fastURL + "/bicycle/?camera_id=" + this.$route.params.cameras_id + "&bicycle_id=1";
    },
    methods: {
    }
}
</script>

<style scoped>
.box {
    overflow-y: scroll;
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.box::-webkit-scrollbar {
    display:none;
}
</style>