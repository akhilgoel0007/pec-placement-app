<template>
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
                        v-for="job in jobOpenings"
                        :key="job.id"
                        :jobID="job.id"
                        :companyIcon="job.company_icon"
                        :profileName="job.profile_name"
                        :companyName="job.company_name"
                        :location="job.location"
                        :status="job.is_active"
                    />
                </div>
            </div>
        </v-card>
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
import JobRow from "../../components/jobProfile-components/jobRow";

export default {
    name: "jobProfiles",
    components: { JobRow },
    data() {
        return {
            //
        }
    },

    methods: {
    },

    computed: {
        ...mapGetters({
            jobOpenings: "getAllJobOpenings"
        }),
    },

    mounted() {
        this.$store.dispatch("FetchJobOpenings");
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