<template>
    <v-app style="background: linear-gradient(to right, #fc00ff, #00dbde);">
        <v-main>
            <v-container>
                <Nuxt />
            </v-container>
        </v-main>
        <v-footer :absolute="!fixed" app>
            <span>&copy; {{ new Date().getFullYear() }}</span>
        </v-footer>
    </v-app>
</template>

<script>
export default {
    name: 'AuthLayout',
    data() {
        return {
            fixed: false,
        }
    },
}
</script>
