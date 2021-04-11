 <template>    
    <div class="pt-10 pb-10" style="margin: 0px 80px;">
        <v-card tile min-height="450">
            <div class="display-flex flex-row pt-8">
                <div class="user-image display-flex centerX centerY" style="width: 25%;">
                    <div class="user-image-wrapper display-flex flex-column">
                        <div class="image-wrapper" style="width: 200px; height: 200px;">
                            <v-avatar size="200" color="grey">
                                <v-icon x-large>
                                    mdi-account
                                </v-icon>
                            </v-avatar>
                        </div>
                        <div class="display-flex centerX centerY mt-3" style="font-weight: bold; font-size: 20px;">
                            <span>{{firstName}} {{lastName}}</span>
                        </div>
                        <div class="display-flex centerX centerY mt-1">
                            <div v-if="isAdmin" class="designation px-2">
                                ADMIN
                            </div>
                            <div v-else class="designation px-2">
                                STUDENT
                            </div>
                        </div>
                    </div>
                </div>
                <div class="user-details pa-4" style="width: 75%;">
                    <div class="display-flex flex-column">
                        <div class="display-flex mx-2 mt-2 mb-6" style="border-bottom: 1px solid black; font-size: 20px; font-weight: bold;">Contact Details</div>
                        <div class="display-flex flex-column ma-2">
                            <div class="display-flex flex-row mb-2">
                                <div style="width: 20%;">Mobile</div>
                                <div style="width: 40%; text-align: center;">{{ contactNumber }}</div>
                                <!-- <div style="width: 40%; text-align: center;">Change Number</div> -->
                            </div>
                            <div class="display-flex flex-row">
                                <div style="width: 20%;">Email</div>
                                <div style="width: 40%; text-align: center;">{{ email }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="display-flex flex-column" style="margin-top: 50px;">
                        <div class="display-flex mx-2 mb-6" style="border-bottom: 1px solid black; font-size: 20px; font-weight: bold;">Password</div>
                        <div class="display-flex flex-row ma-2">
                            <div style="width: 20%;">Password</div>
                            <div style="width: 40%; text-align: center;">*************</div>
                            <!-- <div style="width: 40%; text-align: center;">Change Password</div> -->
                        </div>
                    </div>
                </div>
            </div>
        </v-card>
    </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
    name: "myAccount",
    data() {
        return {
            userNewPassword: null,
            userContactNumber: null,
        }
    },

    methods: {
        update() {
            //
        }
    },

    computed: {
        ...mapGetters({
            email: "getEmail",
            isAdmin: "getAdmin",
            lastName: "getLastName",
            firstName: "getFirstName",
            contactNumber: "getContactNumber"
        })
    }
}

</script>
<style scoped>

.designation {
    color: #9E9E9E;
    font-size: 12px;
    font-weight: bold;
    border-radius: 5px;
    border: 2px solid #9E9E9E;
}

</style>