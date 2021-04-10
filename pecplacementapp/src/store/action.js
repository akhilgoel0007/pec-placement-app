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
        console.log(`Login Error: ${error}`);
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
        console.log(`Sign up Error: ${error}`);
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
        console.log(`Update Profile Error: ${error}`);
    })
}