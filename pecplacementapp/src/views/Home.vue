<template>
    <div class="Home display-flex flex-row" style="height: 100%;">
        <div class="icon display-flex centerX centerY">
            <div style="border-radius: 2px;">
                <img src="../assets/PecIcon.jpg" style="width: 300px; height: 300px;">
            </div>
        </div>
        <div class="auth-wrapper display-flex centerY centerX">
            <v-card style="width: 50%; opacity: 0.97">
                <v-card-title class="text-center justify-center py-6">PEC Placement App</v-card-title>
                <v-tabs v-model="tab" center-active centered>
                    <v-tab>Login</v-tab>
                    <v-tab>Register</v-tab>
                </v-tabs>
                <v-tabs-items v-model="tab">
                    <v-tab-item>
                        <LoginTab />
                    </v-tab-item>
                    <v-tab-item>
                        <SignUpTab />
                    </v-tab-item>
                </v-tabs-items>
            </v-card>
        </div>
    </div>
</template>

<script>

import LoginTab from "../components/login-components/loginTab";
import SignUpTab from "../components/login-components/signUpTab";

export default {
    name: "Home",
    components: { LoginTab, SignUpTab },
    data() {
        return {
            tab: null,
        }
    },
}

</script>
<style scoped>
.icon {
    width: 30%;
    background-color: #f8f8f8;
}

.auth-wrapper {
    width: 70%;
    background-image: url("../assets/PECDSA.jpeg");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

</style>