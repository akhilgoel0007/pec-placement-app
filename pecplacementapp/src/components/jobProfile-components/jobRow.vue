<template>
    <div class="content display-flex flex-row">
        <div class="display-flex centerX centerY company-icon pt-4 pb-4" style="width: 7%;">
            <v-avatar size="40" color="#E0E0E0">
                <v-icon>mdi-account</v-icon>
            </v-avatar>
        </div>
        <div class="display-flex centerY profile-name" style="width: 33%;">
            {{ profileName }}
        </div>
        <div class="display-flex centerY company-name" style="width: 30%;;">
            {{ companyName }}
        </div>
        <div class="display-flex centerY location" style="width: 20%;">
            {{ location }}
        </div>
        <div class="display-flex centerX centerY status" style="width: 10%;">
            <v-avatar v-if="status" size="40" color="#CCFF90">
                <v-icon color="#00C853" size="20">mdi-lock-open</v-icon>
            </v-avatar>
            <v-avatar v-else size="40" color="#E0E0E0">
                <v-icon color="#212121" size="20">mdi-lock</v-icon>
            </v-avatar>
        </div>
    </div>    
</template>

<script>
export default {
    props: {
        companyIcon: { type: String, default: null },
        profileName: { type: String },
        companyName: { type: String },
        location: { type: String },
        status: { type: Boolean, default: true },
    }
}
</script>

<style scoped>

.profile-name, .company-name, .location {
    font-size: 15px;
    font-weight: 500;
}

.profile-name {
    color: #8E24AA;
}

.content {
    cursor: pointer;
    transition: background-color 0.2s ease;
    border-bottom: 1.5px solid #9E9E9E;
}

.content:hover {
    background-color: #F5F5F5;
}

</style>