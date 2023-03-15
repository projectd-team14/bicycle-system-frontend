<template>
    <div>
    <v-card>
        <div>
            <h2>ログイン状態:{{ $auth.loggedIn }}</h2>
            <p>{{ $store.state.homeData["homeData"] }}</p>
        </div>
    </v-card>
    </div>
</template>

<script>
export default {
    name: "IndexPage",
    middleware: "auth",
}
</script>
