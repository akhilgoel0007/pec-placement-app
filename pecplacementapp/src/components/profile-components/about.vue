<template>
    <v-card class="mb-10" min-height="300">
        <div class="user-profile display-flex flex-row pa-5">
            <div class="user-image display-flex centerX centerY" style="width: 20%;">
                <div class="image-wrapper" style="width: 200px; height: 200px;">
                    <v-avatar size="200" color="grey">
                        <v-icon x-large>
                            mdi-account
                        </v-icon>
                    </v-avatar>
                </div>
            </div>
            <div class="user-data px-5" style="width: 80%;">
                <v-row class="ma-0 pb-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>Name:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-title>{{firstName}} {{lastName}}</v-card-title>
                    </v-col>
                </v-row>
                <v-row class="ma-0 pb-0 pt-1">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>Date Of Birth:</v-subheader>
                    </v-col>
                    <v-col cols="10" class="display-flex centerY">
                        <v-card-subtitle v-if="dateOfBirth !== null">{{ dateOfBirth }}</v-card-subtitle>
                        <input v-else v-model="userDOB" type="date" data-date-inline-picker="true" style="outline: none;"/>
                    </v-col>
                </v-row>
                <v-row class="ma-0 pa-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>Gender:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-subtitle v-if="gender !== null">{{ gender }}</v-card-subtitle>
                        <v-radio-group v-model="userGender" row>
                            <v-radio label="Male" value="male"></v-radio>
                            <v-radio label="Female" value="female"></v-radio>
                        </v-radio-group>
                    </v-col>
                </v-row>
            </div>
        </div>
        <v-card-actions class="px-8 pb-5">
            <v-btn class="ma-2" color="info" @click="update()">Update</v-btn>
            <v-btn class="ma-2 white--text" color="error" @click="update()">
                Upload Picture
                <v-icon class="ml-2" dark>mdi-cloud-upload</v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    data() {
        return {
            userDOB: null,
            userGender: null,
        }
    },

    methods: {
        update() {
            var payload = {
                'Gender': this.userGender,
                'DateOfBirth': this.userDOB
            };

            this.$store.dispatch('updateProfile', payload);
        }
    },

    computed: {
        ...mapGetters({
            firstName: "getFirstName",
            lastName: "getLastName",
            gender: "getGender",
            dateOfBirth: "getDateOfBirth"
        })
    }
}

</script>