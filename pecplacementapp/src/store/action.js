import axios from 'axios';
import router from '../router/index';

export const LoginUser = ({ commit }, payload) => {
    
    axios.get("http://localhost:5000/user", {params: payload})
    .then(Response => {
        if(Response.status === 200) {
            commit("LOGIN", Response.data);
            router.push('dashboard');
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

export const ShowJobOpening = ({ commit }, payload) => {
    axios.get("http://localhost:5000/job", {params: payload})
    .then(Response => {
        if(Response.status === 200) {
            commit("STORE_JOB_OPENING", Response.data);
        }
    })
    .then(() => {
        router.push('/jobview');
    })
    .catch(error => {
        console.log(`Show job opening error: ${error}`);
    })
}