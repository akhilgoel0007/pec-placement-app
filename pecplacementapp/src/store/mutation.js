export const MUTATION = (state, Data) => {
    // state manipulation
    console.log(state);
    console.log(Data);
}

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