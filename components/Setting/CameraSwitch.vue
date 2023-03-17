<template>
    <div>
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
        }
    }
}
</script>