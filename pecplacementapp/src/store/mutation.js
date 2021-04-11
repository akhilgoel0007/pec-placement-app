export const REGISTER = (state, Data) => {
    state.firstName = Data['first_name'];
    state.lastName = Data['last_name'];
    state.email = Data['email'];
}

export const LOGIN = (state, Data) => {
    state.admin = Data['user']['admin'];
    state.cg = Data['user']['current_cg'];
    state.email = Data['user']['email'];
    state.batch = Data['user']['batch'];
    state.branch = Data['user']['branch'];
    state.gender = Data['user']['gender'];
    state.github = Data['user']['github_url'];
    state.resume = Data['user']['resume'];
    state.address = Data['user']['address'];
    state.lastName = Data['user']['last_name'];
    state.backLogs = Data['user']['total_backlogs'];
    state.semester = Data['user']['semester'];
    state.linkedIn = Data['user']['linkedin_url'];
    state.firstName = Data['user']['first_name'];
    state.studentID = Data['user']['student_id'];
    state.marksheet = Data['user']['cg_marksheet'];
    state.dateOfBirth = Data['user']['date_of_birth'];
    state.marksheet10 = Data['user']['marksheet_10'];
    state.marksheet12 = Data['user']['marksheet_12'];
    state.schoolName10 = Data['user']['school_name_10'];
    state.schoolName12 = Data['user']['school_name_12'];
    state.percentage10 = Data['user']['percentage_10'];
    state.percentage12 = Data['user']['percentage_12'];
    state.contactNumber = Data['user']['phone_number'];
}

export const UPDATE_PROFILE = (state, Data) => {
    if("current_cg" in Data) {
        state.cg = Data["current_cg"];
    }

    if("batch" in Data) {
        state.batch = Data["batch"];
    }

    if("branch" in Data) {
        state.branch = Data["branch"];
    }

    if("student_id" in Data) {
        state.studentID = Data["student_id"];
    }

    if("gender" in Data) {
        state.gender = Data["gender"];
    }

    if("github_url" in Data) {
        state.github = Data["github_url"];
    }

    if("linkedin_url" in Data) {
        state.linkedIn = Data["linkedin_url"];
    }

    if("resume" in Data) {
        state.resume = Data["resume"];
    }

    if("address" in Data) {
        state.address = Data["address"];
    }

    if("total_backlogs" in Data) {
        state.backLogs = Data["total_backlogs"];
    }

    if("semester" in Data) {
        state.semester = Data["semester"];
    }

    if("phone_number" in Data) {
        state.contactNumber = Data["phone_number"];
    }

    if("date_of_birth" in Data) {
        state.dateOfBirth = Data["date_of_birth"];
    }

    if("cg_marksheet" in Data) {
        state.marksheet = Data["cg_marksheet"];
    }

    if("school_name_10" in Data) {
        state.schoolName10 = Data["school_name_10"];
    }

    if("percentage_10" in Data) {
        state.percentage10 = Data["percentage_10"];
    }

    if("marksheet_10" in Data) {
        state.marksheet10 = Data["marksheet_10"];
    }

    if("school_name_12" in Data) {
        state.schoolName12 = Data["school_name_12"];
    }

    if("percentage_12" in Data) {
        state.percentage12 = Data["percentage_12"];
    }

    if("marksheet_12" in Data) {
        state.marksheet12 = Data["marksheet_12"];
    }

}

export const STORE_ALL_JOB_OPENINGS = (state, Data) => {
    state.jobOpenings = Data['all_job_opening'];
}

export const STORE_ALL_STUDENTS = (state, Data) => {
    state.allStudents = Data['all_users'];
}

export const STORE_JOB_OPENING = (state, Data) => {
    state.currentJobOpening = Data['job_opening'];
}

export const STORE_STATUS = (state, Data) => {
    if(Data["status"] === "applied") {
        state.applied = true;
    } else {
        state.applied = false;
    }
}

export const UPDATE_USER = (state, Data) => {
    state.allStudents.forEach(student => {
        if(student['email'] === Data['email']) {
            student['is_active'] = Data['is_active']?1:0;
        }
    });
}

export const UPDATE_JOB = (state, Data) => {
    console.log(Data);
    state.jobOpenings.forEach(job => {
        if(job['id'] === Data['id']) {
            job['is_active'] = Data['is_active']?1:0;
        }
    });
}

export const STORE_ALL_APPLICANTS = (state, Data) => {
    state.allApplicants = Data["all_applied_users"];
}

export const STORE_MY_APPLICATIONS = (state, Data) => {
    state.myApplications = Data["all_applications"];
}