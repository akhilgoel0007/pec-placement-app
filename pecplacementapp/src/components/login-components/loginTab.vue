<template>
    <div class="px-5 pb-5">
        <v-card-text>
            <v-text-field v-model="email" label="Email" :rules="emailRules" hide-details="auto"></v-text-field>
            <v-text-field v-model="password" label="Password" class="mt-5" :rules="passwordRules"></v-text-field>
        </v-card-text>
        <v-card-actions>
            <v-btn @click="Login()" :disabled="checkDetails" color="black" class="white--text" style="width: 100%">Login</v-btn>
        </v-card-actions>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: '',
            password: '',
            emailRules: [
                value => !!value || 'E-mail is required.',
                value => /.+@pec.edu.in/.test(value) || 'E-mail must be valid',
            ],

            passwordRules: [
                value => !!value || 'Password is required.',
            ]
        }
    },
    
    methods: {
        Login() {
            var Payload = {
                email: this.email,
                password: this.password
            };

            this.$store.dispatch('LoginUser', Payload);
        }
    },

    computed: {
        checkDetails() {
            if(/.+@pec.edu.in/.test(this.email) && !!this.password) {
                return false;
            }

            return true;
        }
    }
}

</script>