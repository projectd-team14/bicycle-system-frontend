<template>
    <v-card
        class="mx-auto"
        max-height="600"
        style="background: linear-gradient(#14F3FF, #6E00B2);"
    > 
        <v-card-item>
            <v-card-title class="headline">Spot registration</v-card-title>
            <v-col cols="12">
                <v-form>
                    <v-text-field
                        v-model="spot.spots_name"
                        label="name"
                    ></v-text-field>
                    <v-text-field
                        v-model="spot.spots_address"
                        label="address"
                    ></v-text-field>
                    <v-text-field
                        v-model="spot.spots_url"
                        label="url"
                    ></v-text-field>
                    <v-text-field
                        v-model="spot.spots_max"
                        label="max"
                    ></v-text-field>
                    <v-text-field
                        v-model="spot.spots_over_time"
                        label="over time"
                    ></v-text-field>
                    <v-select 
                        v-model="spot.spots_status"
                        label="status"
                        :items="items"
                    >
                    </v-select>
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
            spot: {
                spots_name: "",
                spots_address: "",
                spots_url: "",
                spots_max: 0,
                spots_over_time: 0,
                spots_status: "自転車"
            },
            items: ["自転車", "バイク", "全てを管理"]
        }
    },
    methods: {
        onClickRegisterButton() {
            this.$axios.post("/api/store_spot/" + this.$auth.user.id, this.spot)
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