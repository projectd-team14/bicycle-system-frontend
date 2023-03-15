<template>
    <v-card
        class="mx-auto"
        max-height="600"
        style="background: linear-gradient(#14F3FF, #6E00B2);"
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
                            color="#00E5FF"
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
            this.$axios.post("/api/store_camera/" + this.$route.params.id, this.camera)
            .then((response) => {
                this.onLoadhomeData();
                this.$router.push("/home");
            })
        },
        onLoadhomeData() {
            this.$store.dispatch("homeData/onLoadhomeData", {
                usersId: this.$auth.user.id
            });
        }
    }
}
</script>