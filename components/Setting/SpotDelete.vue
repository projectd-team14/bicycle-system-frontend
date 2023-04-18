<template>
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
        <v-snackbar
            v-model="snackBar"
            multi-line
            color="secondary"
        >
            {{ snackText }}
        </v-snackbar> 
    </v-card> 
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
            this.$axios.get("/api/delete_spot/" + this.$route.params.spots_id)
            .then((response) => {
                this.onLoadhomeData();
                this.$router.push("/home");
            })
        },
        async onLoadhomeData() {
            this.$store.dispatch("homeData/onLoadHomeData", {
                usersId: this.$auth.user.id
            });
        }
    }
}
</script>