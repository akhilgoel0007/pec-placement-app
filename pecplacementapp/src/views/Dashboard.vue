<template>
    <div class="main-wrapper">
        <v-app-bar class="px-10" app color="primary" dark>
            <div class="display-flex flex-row">
                <span class="mx-4 mt-1 mb-1">
                    <router-link to="/jobprofiles" class="white--text" style="text-decoration: none;">
                        JOB PROFILES
                    </router-link>
                </span>
                <span class="mx-4 mt-1 mb-1">
                    <router-link to="/dashboard" class="white--text" style="text-decoration: none;">
                        MY PROFILE
                    </router-link>
                </span>
                <span v-if="isAdmin" class="mx-4 mt-1 mb-1">
                    <router-link to="/jobentry" class="white--text" style="text-decoration: none;">
                        NEW OPENING
                    </router-link>
                </span>
            </div>
            <v-spacer></v-spacer>
            <v-menu offset-y rounded="0">
                <template v-slot:activator="{attrs, on}">
                    <v-btn text v-bind="attrs" v-on="on">
                        <span class="mr-2">{{ firstName }} {{ lastName }}</span>
                        <v-icon>mdi-account</v-icon>
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item>
                        <v-list-item-title>
                            <router-link to="/account" class="black--text" style="text-decoration: none;">
                                My Account
                            </router-link>
                        </v-list-item-title>
                    </v-list-item>
                    <v-list-item v-if="isAdmin">
                        <v-list-item-title>
                            <router-link to="/studentprofiles" class="black--text" style="text-decoration: none;">
                                All Students
                            </router-link>
                        </v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-title>Log Out</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-app-bar>
        <div style="height: 100%;">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>

import { mapGetters } from 'vuex'

export default {
    data() {
        return {
            //
        }
    },

    methods: {

    },

    computed: {
        ...mapGetters({
            isAdmin: "getAdmin",
            lastName: "getLastName",
            firstName: "getFirstName"
        })
    }
}

</script>

<style scoped>

.main-wrapper {
    height: 100%;
    background-color: #F5F5F5;
}

</style>