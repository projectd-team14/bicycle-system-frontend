<template>
    <v-row>
        <v-col cols="8">
            <v-card
                class="mx-auto"
                max-height="600"
                style="background: #2c2d3f;"
            > 
                <v-card-item>
                    <v-card-title class="headline">動作設定</v-card-title>
                    <v-col cols="12">
                        <v-row>
                            <v-col cols="6">
                                <v-btn
                                    block
                                    style="background: linear-gradient(#e00083, #33005e);"
                                    @click="onClickStartButton()"
                                >
                                    ON
                                </v-btn>
                            </v-col>
                            <v-col cols="6">
                                <v-btn
                                    block
                                    style="background: linear-gradient(#e00083, #33005e);"
                                    @click="onClickStopButton()"
                                >
                                    OFF
                                </v-btn>                          
                            </v-col>                        
                        </v-row>                        
                    </v-col>
                </v-card-item>
            </v-card>
        </v-col>
        <v-col cols="4">
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
        </v-col>
    </v-row>
</template>
  
<script>
export default {
    data() {
        return{
        }
    },
    methods: {
        onClickStartButton() {
            this.$axios.get("/api/start/" + this.$route.params.cameras_id)
            .then((response) => {
                console.log(response.data);
            })
        },
        onClickStopButton() {
            this.$axios.get("/api/stop/" + this.$route.params.cameras_id)
            .then((response) => {
                console.log(response.data);
            })
        },
        onClickDeleteButton() {
            this.$axios.get("/api/delete_camera/" + this.$route.params.cameras_id)
            .then((response) => {
                console.log(response);
            })
        }
    }
}
</script>