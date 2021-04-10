<template>
    <v-card class="mt-10 mb-10" min-height="300">
        <v-card-title><h2 class="mt-6 px-6">CONTACT DETAILS</h2></v-card-title>
        <v-card-text class="pa-5">
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Contact Number:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="contactNumber !== null">{{ contactNumber }}</v-card-subtitle>
                    <v-text-field v-else v-model="userContactNumber" label="Contact Number"></v-text-field>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Email:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle>{{ email }}</v-card-subtitle>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Permanent Address:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="address !== null">{{ address }}</v-card-subtitle>
                    <v-text-field v-else v-model="userAddress" label="Address"></v-text-field>
                </v-col>
            </v-row>
        </v-card-text>
        <v-card-actions class="px-8 pb-5">
            <v-btn class="ma-2" color="info" @click="update()">Update</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    data() {
        return {
            userContactNumber: null,
            userAddress: null,
        }
    },

    methods: {
        update() {
            var payload = {
                'ContactNumber': this.userContactNumber,
                'Address': this.userAddress
            };

            console.log(payload);
        }
    },

    computed: {
        ...mapGetters({
            email: "getEmail",
            address: "getAddress",
            contactNumber: "getContactNumber"
        })
    }
}

</script>