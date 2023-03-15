<template>
    <RegisterForm class="mx-auto" />
</template>

<script>
import RegisterForm from "~/components/Auth/RegisterForm.vue";

export default {
    layout: "AuthLayout",
    components: {
        RegisterForm
    },
};
</script>