<template>
    <v-card class="mt-10 mb-10" min-height="300">
        <v-card-title>
            <h2 class="mt-6 px-6">
                ADDITIONAL INFORMATION
            </h2>
        </v-card-title>

        <v-card-text class="pa-5">
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>LinkedIn:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="linkedIn !== null">{{ linkedIn }}</v-card-subtitle>
                    <v-text-field v-else v-model="userLinkedIn" label="LinkedIn Link"></v-text-field>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Github:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="github !== null">{{ github }}</v-card-subtitle>
                    <v-text-field v-model="userGithub" v-else label="Github Link"></v-text-field>
                </v-col>
            </v-row>
        </v-card-text>
        <v-card-actions class="px-8 pb-5">
            <v-btn class="ma-2" color="info" @click="update()">Update</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    props: {
        github: {type: String },
        linkedIn: { type: String },
    },

    data() {
        return {
            userGithub: null,
            userLinkedIn: null
        }
    },

    methods: {
        update() {
            var payload = {
                'Github': this.userGithub,
                'LinkedIn': this.userLinkedIn
            };

            this.$store.dispatch('updateProfile', payload);
        }
    },

    computed: {
        ...mapGetters({
            github: "getGithub",
            linkedIn: "getLinkedIn"
        })
    }
}

</script>