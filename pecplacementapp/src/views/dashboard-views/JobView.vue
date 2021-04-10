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
                <div class="profile-name mx-4 mt-5 mb-4 display-flex centerX">Marketing And Business Development</div>
                <div class="company-name ma-2 display-flex centerX">Embeddded Control Systems</div>
                <div class="location ma-1 display-flex centerX">Remote</div>
            </v-card>
            <v-card tile min-height="400" width="60%" class="ma-3">
                <v-card-title class="ml-2">Opening Overview</v-card-title>
                <center><hr style="width: 95%;"></center>
                <div class="category display-flex flex-row">
                    <div class="category-heading">Category</div>
                    <div class="category-content">6 month / 1 year Internship</div>
                </div>
                <div class="compensation display-flex flex-row">
                    <div class="compensation-heading">CTC</div>
                    <div class="compensation-content">₹  10,000.00 - ₹  15,000.00 per Month</div>
                </div>
                <div></div>
            </v-card>
        </div>
        <div class="other-info">
            <v-card tile min-height="400" class="ma-3">
                <v-card-title class="ml-2">Job Description</v-card-title>
                <center><hr style="width: 98%;"></center>
                <v-card-text class="px-5 pt-4 pb-4">Job Description goes here</v-card-text>

                <v-card-title class="ml-2 mt-10">Eligibility Criteria & Evaluation Result</v-card-title>
                <center><hr style="width: 98%;"></center>
                <v-card-text>
                    <div class="criteria display-flex flex-row">
                        <div class="criteria-head">Backlog</div>
                        <div class="criteria-content">Backlogs Allowed</div>
                        <div class="criteria-status">No backlogs</div>
                    </div>
                    <div class="criteria display-flex flex-row">
                        <div class="criteria-head">Course Eligibility</div>
                        <div class="criteria-content">Some Criteria</div>
                        <div class="criteria-status">Criteria satisfied</div>
                    </div>
                    <div class="criteria display-flex flex-row">
                        <div class="criteria-head">Academic Eligibility</div>
                        <div class="criteria-content">Some Criteria</div>
                        <div class="criteria-status">UG - Required: 59.5% , Actual: 84.6%</div>
                    </div>
                </v-card-text>
                <v-card-actions class="mt-10 pb-10 display-flex centerX centerY">
                    <v-btn x-large @click="Login()" rounded :disabled="checkEligibility" color="success" class="white--text" style="width: 150px;">
                        <v-icon class="mr-2 ml-2" dark>mdi-text-box-plus</v-icon>
                        Apply
                    </v-btn>
                </v-card-actions>
            </v-card>
        </div>
    </div>
</template>
<script>

export default {
    name: "jobView",
    data() {
        return {

        }
    },

    methods: {
        
    },

    computed: {
        checkEligibility() {
            return false;
        }
    }
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