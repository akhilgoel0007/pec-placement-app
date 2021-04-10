<template>
    <div class="pt-10 pb-10" style="margin: 0px 80px;">
        <v-card tile min-height="550">
            <div class="profiles-listing display-flex flex-column pa-6">
                <div class="mt-7 listing-heading display-flex flex-column" style="height: 40px;">
                    <div class="heading display-flex flex-row">
                        <div class="headers display-flex centerX centerY" style="width: 30%;">Applicant Name</div>
                        <div class="headers display-flex centerY" style="width: 20%; ">Applicant ID</div>
                        <div class="headers display-flex centerY" style="width: 20%; ">Email ID</div>
                        <div class="headers display-flex centerY" style="width: 20%;">Semester</div>
                        <div class="headers display-flex centerX centerY" style="width: 10%;">Status</div>
                    </div>
                </div>
                <div class="listing-content display-flex flex-column">
                    <StudentRow
                        v-for="applicant in allApplicants"
                        :key="applicant.email"
                        :firstName="applicant.first_name"
                        :studentID="applicant.student_id"
                        :studentSemester="applicant.semester"
                        :lastName="applicant.last_name"
                        :studentEmail="applicant.email"
                        :isActive="applicant.is_active"
                    />
                </div>
            </div>
        </v-card>
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
import StudentRow from "../../components/jobProfile-components/studentRow";

export default {
    name: "showApplicants",
    components: { StudentRow },
    data() {
        return {
            //
        }
    },

    methods: {
    },

    computed: {
        ...mapGetters({
            allApplicants: "getAllApplicants"
        }),
    },
    
    mounted() {
        this.$store.dispatch("FetchAllStudents");
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