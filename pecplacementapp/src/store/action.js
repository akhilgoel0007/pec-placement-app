import axios from 'axios';
import router from '../router/index';

export const LoginUser = ({ commit }, payload) => {
    axios.get("http://localhost:5000/user", {params: payload})
    .then(Response => {
        if(Response.status === 200) {
            if(Response.data['user']['is_active']) {
                commit("LOGIN", Response.data);
                router.push('dashboard');
            } else {
                alert("You are not allowed to log in. Your account is disabled");
            }
        }
    })
    .catch(error => {
        console.log(`Login error: ${error}`);
    })
}

export const SignUpUser = ({ commit }, payload) => {
    axios.post("http://localhost:5000/user/register", payload)
    .then(Response => {
        if(Response.status === 201) {
            commit("REGISTER", payload);
            router.push('dashboard');
        } else if(Response.status === 200) {
            alert("User with this email already exists.");
        }
    })
    .catch(error => {
        console.log(`Sign up error: ${error}`);
    })
}

export const updateProfile = ({ commit, getters }, payload) => {
    payload['email'] = getters.getEmail;

    axios.patch("http://localhost:5000/user/update", payload)
    .then(Response => {
        if(Response.status === 202) {
            commit("UPDATE_PROFILE", payload);
        }
    })
    .catch(error => {
        console.log(`Update Profile error: ${error}`);
    })
}

export const FetchJobOpenings = ({ commit }) => {
    axios.get("http://localhost:5000/alljobs")
    .then(Response => {
        if(Response.status === 200) {
            commit("STORE_ALL_JOB_OPENINGS", Response.data);
        }
    })
    .catch(error => {
        console.log(`Fetch job openings error: ${error}`);
    })
}

export const ShowJobOpening = ({ commit, getters }, payload) => {
    var payload2 = {
        "user_email": getters.getEmail,
        "company_id": payload.id
    }

    axios.all([
        axios.get("http://localhost:5000/job", { params: payload }),
        axios.get("http://localhost:5000/applicationstatus", { params: payload2 })
    ])
    .then(axios.spread((Response1, Response2) => {
        console.log(payload.id);
        if(Response1.status === 200) {
            Response1.data['job_opening']['id'] = payload.id;
            commit("STORE_JOB_OPENING", Response1.data);
        }

        if(Response2.status === 200) {
            commit("STORE_STATUS", Response2.data);
        }
    }))
    .then(() => {
        router.push('/jobview');
    })
    .catch(error => {
        console.log(`Show job opening error: ${error}`);
    })
}

export const CreateOpening = (context, payload) => {
    axios.post("http://localhost:5000/job/register", payload)
    .then(Response => {
        if(Response.status === 201) {
            alert("Job Ceated");
        }
    })
    .catch(error => {
        console.log(`create job opening error: ${error}`);
    })
}

export const ApplyForJob = (context, payload) => {
    axios.post("http://localhost:5000/applyforopening", payload)
    .then(Response => {
        if(Response.status === 201) {
            alert("Applied Successfully!");
        }
    })
    .catch(error => {
        console.log(`Apply job opening error: ${error}`);
    })
}

export const FetchAllStudents = ({ commit }) => {
    axios.get("http://localhost:5000/allusers")
    .then(Response => {
        if(Response.status === 200) {
            commit("STORE_ALL_STUDENTS", Response.data);
        }
    })
    .catch(error => {
        console.log(`Fetch all students error: ${error}`);
    })
}

export const ToggleActiveState = ({ commit }, payload) => {
    axios.patch("http://localhost:5000/user/update", payload)
    .then(Response => {
        if(Response.status === 202) {
            commit("UPDATE_USER", payload);
        }
    })
    .catch(error => {
        console.log(`Update Active Toggle User error: ${error}`);
    })
}

export const ToggleJobActiveState = ({ commit }, payload) => {
    axios.patch("http://localhost:5000/job/update", payload)
    .then(Response => {
        if(Response.status === 202) {
            commit("UPDATE_JOB", payload);
        }
    })
    .catch(error => {
        console.log(`Update Active Toggle Job error: ${error}`);
    })
}

export const ShowAllApplications = ({ commit }, payload) => {
    axios.get("http://localhost:5000/companyallapplications", {params: payload})
    .then(Response => {
        if(Response.status === 200) {
            commit("STORE_ALL_APPLICANTS", Response.data);
            router.push('showallapplicants');
        }
    })
    .catch(error => {
        console.log(`All applicants error: ${error}`);
    })
}