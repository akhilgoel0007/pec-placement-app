<template>
  <v-app>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style>

.display-flex {
  display: flex;
}

.centerX {
  justify-content: center;
}

.centerY {
  align-items: center;
}

.flex-row {
  flex-flow: row nowrap;
}

.flex-column {
  flex-flow: column nowrap;
}
</style>