<template>
    <v-card class="mt-10" min-height="220">
        <v-card-title>
            <h2 class="mt-6 px-6">RESUME</h2>
        </v-card-title>
        <v-card-text>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Resume:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="resume !== null">{{ resume }}</v-card-subtitle>
                    <v-file-input v-else v-model="userResume" color="deep-purple accent-4" counter label="Resume" placeholder="Select your Resume" prepend-icon="mdi-paperclip" :show-size="1000">
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
import { mapGetters } from 'vuex'

export default {
    data() {
        return {
            userResume: null,
        }
    },

    methods: {
        update() {
            var payload = {
                "resume": this.userResume
            };

            this.$store.dispatch('updateProfile', payload);
        }
    },

    computed: {
        ...mapGetters({
            resume: "getResume"
        })
    }
}

</script>