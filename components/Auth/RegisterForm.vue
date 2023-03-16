<template>
    <v-container>
        <v-card style="background: #2c2d3f;">
            <v-col cols="12">
                <h2>Register</h2>
                <v-form @submit.prevent="registerUser">
                    <v-text-field
                        v-model="user.name"
                        label="Name"
                    ></v-text-field>
                    <v-text-field
                        v-model="user.email"
                        label="Email"
                    ></v-text-field>
                    <v-text-field
                        v-model="user.password"
                        type="password"
                        label="Password"
                    ></v-text-field>
                </v-form>
                <v-row>
                    <v-col cols="10">
                        <v-btn
                            block
                            style="background: linear-gradient(#e00083, #33005e);"
                            @click="onClickRegisterButton()"
                        >
                            Join
                        </v-btn>
                    </v-col>
                    <v-col cols="2">
                        <v-btn
                            block
                            outlined
                            color="#e00083" 
                            @click="onClickTransitionLoginButton()"
                        >
                            Sign in
                        </v-btn>                          
                    </v-col>
                </v-row>
            </v-col>
        </v-card>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            user:{
                name: "",
                email: "",
                password: ""
            }
        }
    },
    methods:{
        async onClickRegisterButton() {
            this.$axios.post("/api/register", this.user)
            .then((response) => {
                this.$auth.loginWith("local", {
                    data: this.user
                })
            })
        },
        async onClickTransitionLoginButton() {
            this.$router.push("/auth/login");
        }
    }
}
</script>