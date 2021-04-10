<template>
    <v-card class="mt-10 mb-10" min-height="300">
        <v-card-title>
            <h2 class="mt-6 px-6">
                STUDENT DETAILS
            </h2>
        </v-card-title>
        <v-card-text class="pa-5">
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Student ID:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="studentID !== null">{{ studentID }}</v-card-subtitle>
                    <v-text-field v-model="userSID" v-else label="Student ID"></v-text-field>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Batch:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="batch !== null">{{ batch }}</v-card-subtitle>
                    <v-text-field v-model="userBatch" v-else label="Batch"></v-text-field>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Branch:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="branch !== null">{{ branch }}, Department of {{ branch }}</v-card-subtitle>
                    <v-select v-else v-model="userBranch" :items="branchOptions" label="Branch" dense></v-select>
                </v-col>
            </v-row>
            <v-row class="ma-0 pa-0">
                <v-col cols="2" class="display-flex centerY">
                    <v-subheader>Semester:</v-subheader>
                </v-col>
                <v-col cols="10">
                    <v-card-subtitle v-if="semester !== null">{{ semester }}</v-card-subtitle>
                    <v-select v-else v-model="userSemester" :items="semesterOptions" label="Semester" dense></v-select>
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
            userSID: null,
            userBatch: null,
            userBranch: null,
            userSemester: null,
        }
    },

    methods: {
        update() {
            var payload = {
                'SID': this.userSID,
                'Batch': this.userBatch,
                'Branch': this.userBranch,
                'Semester': this.userSemester
            };
            
            this.$store.dispatch('updateProfile', payload);
        }
    },

    computed: {
        ...mapGetters({
            batch: "getBatch",
            branch: "getBranch",
            semester: "getSemester",
            studentID: "getStudentID",
            branchOptions: "getBranchOptions",
            semesterOptions: "getSemesterOptions",
        })
    }
}

</script>