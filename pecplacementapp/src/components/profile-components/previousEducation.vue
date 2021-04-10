<template>
    <v-card class="mt-10 mb-10" min-height="300">
        <v-card-title>
            <h2 class="mt-6 px-6">
                PREVIOUS EDUCATION
            </h2>
        </v-card-title>
        
        <v-card-text class="pa-5">
            <div>
                <v-row class="ml-1 mb-2">
                    <v-col cols="12">
                        <h1>Class 12<sup>th</sup></h1>
                    </v-col>
                </v-row>
                <v-row class="mt-0 mb-0 ml-3 mr-0 pa-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>School Name:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-subtitle v-if="schoolName12 !== null">{{ schoolName12 }}</v-card-subtitle>
                        <v-text-field v-else v-model="userSchoolName12" label="School Name"></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="mt-0 mb-0 ml-3 mr-0 pa-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>Percentage:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-subtitle v-if="percentage12 !== null">{{ percentage12 }}</v-card-subtitle>
                        <v-text-field v-else v-model="userPercentage12" label="Percentage"></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="mt-0 mb-0 ml-3 mr-0 pa-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>Marksheet:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-subtitle v-if="marksheet12 !== null">{{ marksheet12 }}</v-card-subtitle>
                        <v-file-input v-else v-model="userMarksheet12" color="deep-purple accent-4" counter label="Marksheet" placeholder="Select your Marksheet" prepend-icon="mdi-paperclip" :show-size="1000">
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
            </div>
            <div>
                <v-row class="ml-1 mt-5 mb-2">
                    <v-col cols="12">
                        <h1>Class 10<sup>th</sup></h1>
                    </v-col>
                </v-row>
                <v-row class="mt-0 mb-0 ml-3 mr-0 pa-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>School Name:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-subtitle v-if="schoolName10 !== null">{{ schoolName10 }}</v-card-subtitle>
                        <v-text-field v-else v-model="userSchoolName10" label="School Name"></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="mt-0 mb-0 ml-3 mr-0 pa-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>Percentage:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-subtitle v-if="percentage10 !== null">{{ percentage10 }}</v-card-subtitle>
                        <v-text-field v-else v-model="userPercentage10" label="Percentage"></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="mt-0 mb-0 ml-3 mr-0 pa-0">
                    <v-col cols="2" class="display-flex centerY">
                        <v-subheader>Marksheet:</v-subheader>
                    </v-col>
                    <v-col cols="10">
                        <v-card-subtitle v-if="marksheet10 !== null">{{ marksheet10 }}</v-card-subtitle>
                        <v-file-input v-else v-model="userMarksheet10" color="deep-purple accent-4" counter label="Marksheet" placeholder="Select your Marksheet" prepend-icon="mdi-paperclip" :show-size="1000">
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
            </div>
        </v-card-text>
        <v-card-actions v-if="updateRequired" class="px-8 pb-5">
            <v-btn class="ma-2" color="info" @click="update()">Update</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    data() {
        return {
            userSchoolName10: null,
            userPercentage10: null,
            userMarksheet10: null,
            userSchoolName12: null,
            userPercentage12: null,
            userMarksheet12: null,
        }
    },

    methods: {
        update() {
            var payload = {};

            if(this.userSchoolName10) {
                payload['school_name_10'] = this.userSchoolName10;
            }

            if(this.userPercentage10) {
                payload['percentage_10'] = this.userPercentage10;
            }

            if(this.userMarksheet10) {
                payload['marksheet_10'] = this.userMarksheet10;
            }

            if(this.userSchoolName12) {
                payload['school_name_12'] = this.userSchoolName12;
            }

            if(this.userPercentage12) {
                payload['percentage_12'] = this.userPercentage12;
            }

            if(this.userMarksheet12) {
                payload['marksheet_12'] = this.userMarksheet12;
            }
            
            if(!(Object.keys(payload).length === 0 && payload.constructor === Object)) {
                this.$store.dispatch('updateProfile', payload);
            }
        }
    },

    computed: {
        ...mapGetters({
            schoolName10:"getSchoolName10",
            percentage10: "getPercentage10",
            marksheet10: "getMarksheet10",
            schoolName12:"getSchoolName12",
            percentage12: "getPercentage12",
            marksheet12: "getMarksheet12",
        }),

        updateRequired() {
            return (!this.schoolName10 || !this.percentage10 || !this.marksheet10 || !this.schoolName12 || !this.percentage12 || this.marksheet12)?true:false;
        }
    }
}

</script>