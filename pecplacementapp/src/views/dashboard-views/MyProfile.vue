<template>
    <div class="pt-10 pb-10" style="margin: 0px 80px;">
        <About />
        <StudentDetails />
        <ContactDetails />
        <AdditionalInfo />
        <AcademicExcellance />
        <PreviousEducation />
        <Resume />
    </div>
</template>

<script>
import About from "../../components/profile-components/about";
import StudentDetails from "../../components/profile-components/studentDetails";
import ContactDetails from "../../components/profile-components/contactDetails";
import AdditionalInfo from "../../components/profile-components/additionalInfo";
import AcademicExcellance from "../../components/profile-components/academicExcellance"
import PreviousEducation from "../../components/profile-components/previousEducation"
import Resume from "../../components/profile-components/resume"

export default {
    name: "myProfile",
    components: {
        About,
        Resume,
        StudentDetails,
        ContactDetails,
        AdditionalInfo,
        PreviousEducation,
        AcademicExcellance
    },

    data() {
        return {
            //
        }
    },
}

</script>