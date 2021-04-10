<template>
    <!-- Change the Job Description Editor using ToastUI -->
    <!-- Add Job Functions -->
    <!-- Add Backlogs Allowed -->
    <!-- Add Allowed Branches -->
    
    <div class="pt-12 pb-12" style="margin: 0px 150px;">
        <v-card tile min-height="300">
            <v-card-title>
                <h2 class="px-6" style="margin: 40px auto; color: #9E9E9E">JOB OPENING</h2>
            </v-card-title>
            <v-card-text>

                <!-- Profile Name -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        Profile Name:
                    </div>
                    <div class="input-content">
                        <v-text-field v-model="profileName" label="Profile Name"></v-text-field>
                    </div>
                </div>

                <!-- Job Type -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        Classification:
                    </div>
                    <div class="input-content">
                        <v-radio-group v-model="classification" row>
                            <v-radio label="Internship Opening" value="Internship"></v-radio>
                            <v-radio label="Full Time Opening" value="FullTime"></v-radio>
                        </v-radio-group>
                    </div>
                </div>

                <!-- Job Duration -->
                <div class="input-field-wrapper display-flex flex-row" v-if="classification === 'Internship'">
                    <div class="input-heading display-flex centerY">
                        Duration:
                    </div>
                    <div class="input-content">
                        <v-select v-model="duration" :items="durationOptions" label="Duration" dense></v-select>
                    </div>
                </div>

                <!-- Job Compensation -->
                <div class="input-field-wrapper display-flex flex-row" v-if="classification === 'Internship'">
                    <div class="input-heading display-flex centerY">
                        Stipend:
                    </div>
                    <div class="input-content">
                        <v-text-field v-model="stipend" label="Stipend"></v-text-field>
                    </div>
                </div>

                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        <span>
                            CTC<span v-if="classification === 'Internship'">&nbsp;(Tentative)</span>:
                        </span>
                    </div>
                    <div class="input-content">
                        <v-text-field v-model="ctc" label="CTC"></v-text-field>
                    </div>
                </div>

                <!-- CG BARRIER -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        Minimum CG Criteria:
                    </div>
                    <div class="input-content display-flex flex-row">
                        <div class="criteria-choice">
                            <v-radio-group v-model="cgRequired" row>
                                <v-radio label="Yes" value="true"></v-radio>
                                <v-radio label="No" value="false"></v-radio>
                            </v-radio-group>
                        </div>
                        <div class="criteria-choice-input" v-if="cgRequired === 'true'">
                            <div class="display-flex flex-row" style="width: 100%;">
                                <div class="criteria-input-heading display-flex centerY">
                                    Minimum CG:
                                </div>
                                <div class="criteria-input-content">
                                    <v-text-field v-model="minCG" label="Minimum Required CG"></v-text-field>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- 12TH PERCENTAGE BARRIER -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        <span>
                            12<sup>th</sup>&nbsp;Percentage Criteria:
                        </span>
                    </div>
                    <div class="input-content display-flex flex-row">
                        <div class="criteria-choice">
                            <v-radio-group v-model="percentage12Required" row>
                                <v-radio label="Yes" value="true"></v-radio>
                                <v-radio label="No" value="false"></v-radio>
                            </v-radio-group>
                        </div>
                        <div class="criteria-choice-input" v-if="percentage12Required === 'true'">
                            <div class="display-flex flex-row" style="width: 100%;">
                                <div class="criteria-input-heading display-flex centerY">
                                    Minimum Percentage:
                                </div>
                                <div class="criteria-input-content">
                                    <v-text-field v-model="min12Percentage" label="Minimum Percentage"></v-text-field>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 10TH PERCENTAGE BARRIER -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        <span>
                            10<sup>th</sup>&nbsp;Percentage Criteria:
                        </span>
                    </div>
                    <div class="input-content display-flex flex-row">
                        <div class="criteria-choice">
                            <v-radio-group v-model="percentage10Required" row>
                                <v-radio label="Yes" value="true"></v-radio>
                                <v-radio label="No" value="false"></v-radio>
                            </v-radio-group>
                        </div>
                        <div class="criteria-choice-input" v-if="percentage10Required === 'true'">
                            <div class="display-flex flex-row" style="width: 100%;">
                                <div class="criteria-input-heading display-flex centerY">
                                    Minimum Percentage:
                                </div>
                                <div class="criteria-input-content">
                                    <v-text-field v-model="min10Percentage" label="Minimum Percentage"></v-text-field>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Application Opening Date -->
                <div class="input-field-wrapper display-flex flex-row mb-6 mt-4">
                    <div class="input-heading display-flex centerY">
                        Application Opening Date:
                    </div>
                    <div class="input-content">
                        <input v-model="applicationOpenDate" type="date" data-date-inline-picker="true" style="outline: none;"/>
                    </div>
                </div>

                <!-- Application Closing Date -->
                <div class="input-field-wrapper display-flex flex-row mb-6 mt-10">
                    <div class="input-heading display-flex centerY">
                        Application Closing Date:
                    </div>
                    <div class="input-content">
                        <input v-model="applicationCloseDate" type="date" data-date-inline-picker="true" style="outline: none;"/>
                    </div>
                </div>

                <!-- JOB DESCRIPTION -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        Job Description:
                    </div>
                    <div class="input-content">
                        <v-textarea v-model="jobDescription" clearable clear-icon="mdi-close-circle" label="Job Description"></v-textarea>
                    </div>
                </div>
            </v-card-text>
            <v-card-actions class="px-12 pb-10">
                <v-btn class="ma-2 white--text" color="success">
                    <v-icon class="mr-4 ml-2" dark>mdi-briefcase-plus</v-icon>
                    Create Opening
                </v-btn>
                <v-btn class="ma-2 white--text" color="error" @click="resetForm()">
                    <v-icon class="mr-2 ml-2" dark>mdi-cached</v-icon>
                    Reset Form
                </v-btn>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name: "jobEntry",
    data() {
        return {
            ctc: null,
            minCG: null,
            stipend: null,
            duration: null,
            cgRequired: null,
            profileName: null,
            classification: null,
            jobDescription: null,
            min10Percentage: null,
            min12Percentage: null,
            applicationOpenDate: null,
            percentage10Required: null,
            percentage12Required: null,
            applicationCloseDate: null,
        }
    },

    methods: {
        resetForm() {
            this.ctc = null;
            this.minCG = null;
            this.stipend = null;
            this.duration = null;
            this.cgRequired = null;
            this.profileName = null;
            this.classification = null;
            this.jobDescription = null;
            this.min10Percentage = null;
            this.min12Percentage = null;
            this.applicationOpenDate = null;
            this.percentage10Required = null;
            this.percentage12Required = null;
            this.applicationCloseDate = null;
        }
    },

    computed: {
        ...mapGetters({
            durationOptions: "getDurationOptions",
        })
    }
}
</script>
<style scoped>
.input-field-wrapper {
    width: 100%;
    padding: 5px 50px;
}

.input-heading {
    width: 30%;
    font-size: 19px;
}

.input-content {
    width: 70%;
}

.criteria-choice {
    width: 20%;
}

.criteria-choice-input {
    width: 80%;
}

.criteria-input-heading {
    width: 40%;
    margin-left: 30px;
    font-size: 19px;
}

.criteria-input-content {
    width: 40%;
}

</style>