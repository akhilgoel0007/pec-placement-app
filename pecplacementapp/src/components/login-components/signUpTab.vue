<template>
    <div class="px-5 pb-5">
        <v-card-text>
            <v-text-field v-model="firstName" label="First Name*" :rules="firstNameRules" hide-details="auto"></v-text-field>
            <v-text-field v-model="lastName" label="Last Name*" class="mt-5" :rules="lastNameRules" hide-details="auto"></v-text-field>
            <v-text-field v-model="email" label="Email*" class="mt-5" :rules="usernameRules" hide-details="auto"></v-text-field>
            <v-text-field v-model="password" label="Password*" class="mt-5" :rules="passwordRules"></v-text-field>
        </v-card-text>
        <v-card-actions>
            <v-btn @click="SignUpUser()" id="recaptcha" :disabled="checkDetails" color="black" class="white--text" style="width: 100%">Sign Up</v-btn>
        </v-card-actions>
    </div>
</template>

<script>

export default {
    data() {
        return {
            firstName: '',
            lastName: '',
            email: '',
            password: '',

            firstNameRules: [
                value => !!value || 'First Name is required.',
                value => /^[a-zA-Z]+$/.test(value) || 'Just first name is required.'
            ],

            lastNameRules: [
                value => !!value || 'Last Name is required.',
                value => /^[a-zA-Z]+$/.test(value) || 'Just last name is required.'
            ],

            usernameRules: [
                value => !!value || 'E-mail is required.',
                value => /.+@pec.edu.in/.test(value) || 'E-mail must be valid',
            ],
            
            passwordRules: [
                value => !!value || 'Password is required.',
            ],
        }
    },
    
    methods: {
        SignUpUser() {
            var Payload = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                password: this.password,
            }

            this.$store.dispatch('SignUpUser', Payload);
        },
    },

    computed: {
        checkDetails() {
            if(/^[a-zA-Z]+$/.test(this.firstName) && /^[a-zA-Z]+$/.test(this.lastName) && /.+@pec.edu.in/.test(this.email) && !!this.password) {
                return false;
            }

            return true;
        },
    }
}
</script>