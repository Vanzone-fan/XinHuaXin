<template>
    <div>
        <el-container>
            <el-header style="">
                <span style="">Retail Data Analysis</span>
            </el-header>
        </el-container>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            
        }
    },
    methods:{

    },
    mounted() {
    }
}
</script>

<style scoped>
.el-header {
    height: 80px;
    background-color: rgb(64, 158, 255);
    position: relative;
    display: flex;
    align-items: center;
}

.el-header > span {
    color: #fff;
    font-size: 35px;
    font-weight: 700;
    font-family: 'Harmony OS', Courier, monospace;
}
</style>