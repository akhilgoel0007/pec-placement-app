<template>
    <!-- Add Routes in Job Rows to their specific openings.-->

    <div class="pt-10 pb-10" style="margin: 0px 80px;">
        <v-card tile min-height="550">
            <div class="profiles-listing display-flex flex-column pa-6">
                <div class="mt-7 listing-heading display-flex flex-column" style="height: 40px;">
                    <div class="heading display-flex flex-row">
                        <div class="headers display-flex centerX centerY" style="width: 40%;">Job Profile</div>
                        <div class="headers display-flex centerY" style="width: 30%; ">Company</div>
                        <div class="headers display-flex centerY" style="width: 20%;">Location</div>
                        <div class="headers display-flex centerX centerY" style="width: 10%;">Status</div>
                    </div>
                </div>
                <div class="listing-content display-flex flex-column">
                    <JobRow
                        v-for="(job, index) in jobOpenings"
                        :key="index"
                        :companyIcon="job.companyIcon"
                        :profileName="job.profileName"
                        :companyName="job.companyName"
                        :location="job.location"
                        :status="job.status"
                    />
                </div>
            </div>
        </v-card>
    </div>
</template>
<script>
import JobRow from "../../components/jobProfile-components/jobRow";

export default {
    name: "jobProfiles",
    components: { JobRow },
    data() {
        return {
            jobOpenings: [
                {
                    "companyIcon": null,
                    "profileName": "Marketing And Business Development",
                    "companyName": "Embeddded Control Systems",
                    "location": "Remote",
                    "status": true
                },
                {
                    "companyIcon": null,
                    "profileName": "Business Development Trainee",
                    "companyName": "Tenerife Innovations Private Limited",
                    "location": "Noida & Gurgaon",
                    "status": false
                }
            ]
        }
    },

    methods: {
        
    }
}

</script>
<style scoped>
.heading {
    height: 100%;
    border-bottom: 2px solid #9E9E9E;
}

.headers {
    color: #616161;
    font-size: 18px;
    font-weight: 500;
    text-align: center;
}

</style>