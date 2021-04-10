<template>
    <!-- Change the Job Description Editor using ToastUI -->
    
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

                <!-- Company Name -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        Company Name:
                    </div>
                    <div class="input-content">
                        <v-text-field v-model="companyName" label="Company Name"></v-text-field>
                    </div>
                </div>

                <!-- Location -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        Job Location:
                    </div>
                    <div class="input-content">
                        <v-text-field v-model="location" label="Job Location"></v-text-field>
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

                <!-- Backlogs requirement BARRIER -->
                <div class="input-field-wrapper display-flex flex-row">
                    <div class="input-heading display-flex centerY">
                        Allow Backlogs:
                    </div>
                    <div class="input-content display-flex flex-row">
                        <div class="criteria-choice">
                            <v-radio-group v-model="backlogAllowed" row>
                                <v-radio label="Yes" value="true"></v-radio>
                                <v-radio label="No" value="false"></v-radio>
                            </v-radio-group>
                        </div>
                        <div class="criteria-choice-input" v-if="backlogAllowed === 'true'">
                            <div class="display-flex flex-row" style="width: 100%;">
                                <div class="criteria-input-heading display-flex centerY">
                                    Maximum Backlogs:
                                </div>
                                <div class="criteria-input-content">
                                    <v-text-field v-model="maxBacklogs" label="Maximum Backlogs Allowed"></v-text-field>
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
                <v-btn :disabled="!allowToCreateOpening" @click="createOpening()" class="ma-2 white--text" color="success">
                    <v-icon class="mr-4 ml-2" dark>mdi-briefcase-plus</v-icon>
                    Create Opening
                </v-btn>
                <v-btn @click="resetForm()" class="ma-2 white--text" color="error">
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
            location: null,
            cgRequired: null,
            profileName: null,
            companyName: null,
            maxBacklogs: null,
            classification: null,
            jobDescription: null,
            backlogAllowed: null,
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
            this.location = null;
            this.cgRequired = null;
            this.profileName = null;
            this.companyName = null;
            this.maxBacklogs = null;
            this.backlogAllowed = null;
            this.classification = null;
            this.jobDescription = null;
            this.min10Percentage = null;
            this.min12Percentage = null;
            this.applicationOpenDate = null;
            this.percentage10Required = null;
            this.percentage12Required = null;
            this.applicationCloseDate = null;
        },

        createOpening() {
            var payload = {
                location: this.location,
                profile_name: this.profileName,
                company_name: this.companyName,
                offer_type: this.classification,
                job_description: this.jobDescription,
                application_open_date: this.applicationOpenDate,
                application_close_date: this.applicationCloseDate
            };

            if(this.cgRequired === 'true') {
                payload['min_cg'] = this.minCG;
            }

            if(this.backlogAllowed === 'true') {
                payload['max_backlogs'] = this.maxBacklogs;
            }

            if(this.percentage12Required === 'true') {
                payload['min_12_percentage'] = this.min12Percentage;
            }

            if(this.percentage10Required === 'true') {
                payload['min_10_percentage'] = this.min10Percentage;
            }
            
            if(this.classification === "Internship") {
                payload['duration'] = this.duration;
                payload['stipend'] = this.stipend;
                if(this.ctc) {
                    payload['ctc'] = this.ctc;
                }
            } else if(this.classification === "FullTime") {
                payload['duration'] = "full_time";
                payload['ctc'] = this.ctc;
            }

            this.$store.dispatch("CreateOpening", payload);
        },

        checkValue(condition, value) {
            if(condition === 'true') {
                if(value) {
                    return true;
                } else {
                    return false;
                }
            } else if(condition === 'false') {
                return true;
            } else {
                return false;
            }
        },
    },

    computed: {
        ...mapGetters({
            durationOptions: "getDurationOptions",
        }),

        allowToCreateOpening() {
            if(this.profileName && this.companyName && this.jobDescription && this.applicationCloseDate && this.applicationOpenDate && this.location) {
                if(this.classification === "Internship") {
                    if(this.stipend && this.duration) {
                        console.log( this.checkValue(this.backlogAllowed, this.maxBacklogs));
                        if(this.checkValue(this.cgRequired, this.minCG) && this.checkValue(this.backlogAllowed, this.maxBacklogs) && this.checkValue(this.percentage12Required, this.min12Percentage) && this.checkValue(this.percentage10Required, this.min10Percentage)) {
                            return true;
                        } else {
                            return false;
                        }
                    } else {
                        return false;
                    }
                } else if(this.classification === "FullTime") {
                    if(this.ctc) {
                        if(this.checkValue(this.cgRequired, this.minCG) && this.checkValue(this.backlogAllowed, this.maxBacklogs) && this.checkValue(this.percentage12Required, this.min12Percentage) && this.checkValue(this.percentage10Required, this.min10Percentage)) {
                            return true;
                        } else {
                            return false;
                        }
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            } else {
                return false;
            }
        },
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