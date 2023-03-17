<template>
    <v-card
        class="mx-auto"
        max-height="600"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">カメラ登録</v-card-title>
            <v-col cols="12">
                <v-form>
                    <v-text-field
                        v-model="camera.cameras_name"
                        label="name"
                    ></v-text-field>
                    <v-text-field
                        v-model="camera.cameras_url"
                        label="url"
                    ></v-text-field>
                </v-form>
                <v-row>
                    <v-col cols="4">
                        <v-btn
                            block
                            style="background: linear-gradient(#e00083, #33005e);"
                            @click="onClickRegisterButton()"
                        >
                            Register
                        </v-btn>
                    </v-col>
                </v-row>
            </v-col>             
        </v-card-item>
    </v-card>            
</template>
  
<script>
export default {
    data() {
        return{
            camera: {
                cameras_name: "",
                cameras_url: "",
            }
        }
    },
    methods: {
        onClickRegisterButton() {
            this.$axios.post("/api/store_camera/" + this.$route.params.spots_id, this.camera)
            .then((response) => {
                this.onLoadhomeData();
                this.$router.push("/home");
            })
        },
        onLoadhomeData() {
            this.$store.dispatch("homeData/onLoadHomeData", {
                usersId: this.$auth.user.id
            });
        }
    }
}
</script>