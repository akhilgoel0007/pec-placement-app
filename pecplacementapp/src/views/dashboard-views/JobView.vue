<template>
    <div class="pt-12 pb-12" style="margin: 0px 100px;">
        <div class="display-flex flex-row">
            <v-card tile min-height="400" width="40%" class="ma-3">
                <div class="mt-10 image-wrapper display-flex centerX">
                    <v-avatar size="200" color="grey">
                        <v-icon x-large>
                            mdi-account
                        </v-icon>
                    </v-avatar>
                </div>
                <div class="profile-name mx-4 mt-5 mb-4 display-flex centerX">{{ jobOpening.profile_name }}</div>
                <div class="company-name ma-2 display-flex centerX">{{ jobOpening.company_name }}</div>
                <div class="location ma-1 display-flex centerX">{{ jobOpening.location }}</div>
            </v-card>
            <v-card tile min-height="400" width="60%" class="ma-3">
                <v-card-title class="ml-2">Opening Overview</v-card-title>
                <center><hr style="width: 95%;"></center>
                <div class="category display-flex flex-row">
                    <div class="category-heading">Category</div>
                    <div class="category-content">{{ jobOpening.offer_type }}</div>
                </div>
                <div v-if="jobOpening.stipend" class="compensation display-flex flex-row">
                    <div class="compensation-heading">Stipend</div>
                    <div class="compensation-content">{{ jobOpening.stipend }}</div>
                </div>
                <div v-if="jobOpening.ctc" class="compensation display-flex flex-row">
                    <div class="compensation-heading">CTC</div>
                    <div class="compensation-content">{{ jobOpening.ctc }}</div>
                </div>
            </v-card>
        </div>
        <div class="other-info">
            <v-card tile min-height="400" class="ma-3">
                <v-card-title class="ml-2">Job Description</v-card-title>
                <center><hr style="width: 98%;"></center>
                <v-card-text class="px-5 pt-4 pb-4">{{ jobOpening.job_description }}</v-card-text>

                <v-card-title class="ml-2 mt-10">Eligibility Criteria & Evaluation Result</v-card-title>
                <center><hr style="width: 98%;"></center>
                <v-card-text>
                    <div class="criteria display-flex flex-row">
                        <div class="criteria-head">Backlog</div>
                        <div v-if="jobOpening.max_backlogs" class="criteria-content">Maximum Backlogs Allowed: {{ jobOpening.max_backlogs }}</div>
                        <div v-else class="criteria-content">No Backlogs Allowed</div>
                        <div class="criteria-status">Backlogs: {{ backLogs }}</div>
                    </div>
                    <div v-if="jobOpening.min_cg" class="criteria display-flex flex-row">
                        <div class="criteria-head">Academic Eligibility</div>
                        <div class="criteria-content">Minimum Required CG: {{ jobOpening.min_cg }}</div>
                        <div class="criteria-status">CG: {{ minCG }}</div>
                    </div>
                    <div v-if="jobOpening.min_10_percentage" class="criteria display-flex flex-row">
                        <div class="criteria-head">Academic Eligibility</div>
                        <div class="criteria-content">Minimum 10th Percenatge: {{ jobOpening.min_10_percentage }}</div>
                        <div class="criteria-status">{{ percentage10 }}</div>
                    </div>
                    <div v-if="jobOpening.min_12_percentage" class="criteria display-flex flex-row">
                        <div class="criteria-head">Academic Eligibility</div>
                        <div class="criteria-content">Minimum 12th Percenatge: {{ jobOpening.min_12_percentage }}</div>
                        <div class="criteria-status">{{ percentage12 }}</div>
                    </div>
                </v-card-text>
                <v-card-actions class="mt-10 pb-10 display-flex centerX centerY">
                    <v-btn v-if="isAdmin" x-large @click="showAllApplications()" rounded color="primary" class="white--text">
                        <v-icon class="mr-2 ml-2" dark>mdi-text-box-plus</v-icon>
                        Show All Applications
                    </v-btn>
                    <v-btn x-large @click="applyForJob()" rounded :disabled="appliedStatus || checkEligibility" color="success" class="white--text" style="width: 150px;">
                        <v-icon class="mr-2 ml-2" dark>mdi-text-box-plus</v-icon>
                        <span v-if="appliedStatus">Applied</span>
                        <span v-else>Apply</span>
                    </v-btn>
                </v-card-actions>
            </v-card>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: "jobView",
    data() {
        return {
            //
        }
    },

    methods: {
        applyForJob() {
            var payload = {
                "user_email": this.email,
                "company_id": this.jobOpening.id
            }
            
            this.$store.dispatch("ApplyForJob", payload);
        },

        showAllApplications() {
            var payload = {
                'company_id': this.jobOpening.id
            }

            this.$store.dispatch("ShowAllApplications", payload);
        }
    },

    computed: {
        ...mapGetters({
            minCG: "getCG",
            email: "getEmail",
            isAdmin: "getAdmin",
            backLogs: "getBacklogs",
            percentage10: "getPercentage10",
            percentage12: "getPercentage12",
            appliedStatus: "getAppliedStatus",
            jobOpening: "getCurrentJobOpening"
        }),

        checkEligibility() {
            if(this.jobOpening.min_10_percentage) {
                if(parseInt(this.jobOpening.min_10_percentage) > parseInt(this.percentage10)) {
                    return true;
                }
            }

            if(this.jobOpening.min_12_percentage) {
                if(parseInt(this.jobOpening.min_12_percentage) > parseInt(this.percentage12)) {
                    return true;
                }
            }

            if(this.jobOpening.min_cg) {
                if(parseFloat(this.jobOpening.min_cg) > parseFloat(this.minCG)) {
                    return true;
                }
            }

            if(this.jobOpening.max_backlogs) {
                if(parseInt(this.jobOpening.max_backlogs) < parseInt(this.backLogs)) {
                    return true;
                }
            } else {
                if(this.backLogs !== 0) {
                    return true;
                }
            }

            return false;
        }
    },
}

</script>
<style scoped>
.profile-name {
    font-size: 19px;
    font-weight: 700;
}

.company-name {
    font-size: 17px;
    font-weight: 500;
}

.category, .compensation {
    width: 100%;
    margin: 10px 0px 10px 20px;
    padding: 10px;
}

.category-heading, .compensation-heading {
    width: 30%;
}

.category-content, .compensation-content {
    width: 70%;
}

.criteria {
    width: 100%;
    height: 40px;
    padding: 10px;
    font-size: 15px;
    color: #424242;
}

.criteria-head {
    width: 20%;
}

.criteria-content {
    width: 40%;
}

.criteria-status {
    width: 40%;
}
</style>