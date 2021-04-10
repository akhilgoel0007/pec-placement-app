<template>
    <v-card class="mt-10 mb-10" min-height="300">
        <v-card-title><h2 class="mt-6 px-6">CURRENT/ONGOING COURSE</h2></v-card-title>
        <v-card-text class="pa-5">
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Current CG:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="cg !== null">{{ cg }}</v-card-subtitle>
                    <v-text-field v-else v-model="userCG" label="Current CG"></v-text-field>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Total Backlogs:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="backLogs !== null">{{ backLogs }}</v-card-subtitle>
                    <v-text-field v-else v-model="userBackLogs" label="Total Backlogs"></v-text-field>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Marksheet:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="marksheet !== null">{{ marksheet }}</v-card-subtitle>
                    <v-file-input v-else v-model="userMarkSheet" color="deep-purple accent-4" counter label="MarkSheet" placeholder="Select your marksheet" prepend-icon="mdi-paperclip" :show-size="1000">
                        <template v-slot:selection="{ index, text }">
                        <v-chip v-if="index < 2" color="deep-purple accent-4" dark label small>
                            {{ text }}
                        </v-chip>

                        <span v-else-if="index === 2" class="overline grey--text text--darken-3 mx-2">
                            +{{ files.length - 2 }} File(s)
                        </span>
                        </template>
                    </v-file-input>
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
    data() {
        return {
            userCG: null,
            userBackLogs: null,
            userMarkSheet: null,
        }
    },

    methods: {
        update() {
            var payload = {
                "CG": this.userCG,
                "BackLogs": this.userBackLogs,
                "Marksheet": this.userMarkSheet
            };

            this.$store.dispatch('updateProfile', payload);
        }
    },

    computed: {
        ...mapGetters({
            cg: "getCG",
            backLogs: "getBacklogs",
            marksheet: "getMarksheet",
        })
    }
}

</script>