<template>
    <div id="app">
        <router-view v-if="loadingFlag" />
        <loading v-else />
    </div>
</template>

<script>
import Loading from "./components/Loading.vue";
import axios from "axios";
export default {
    components: { Loading },
    data() {
        return {
            loadingFlag: true,
        };
    },
    methods: {},
};
</script>

<style></style>
