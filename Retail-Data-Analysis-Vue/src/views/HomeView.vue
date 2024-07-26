<template>
    <div>
        <top-nav></top-nav>

        <el-container>
            <aside-nav></aside-nav>

            <el-main height="">
                <img src="../../public/u794.png" alt="" />
                <p>Analysis</p>
            </el-main>
        </el-container>
    </div>
</template>
<script>
import axios from "axios";
export default {
    name: "HomeView",

};
</script>
<style scoped>
img {
    width: 40%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
p {
    font-size: 150px;
    font-weight: 700;
    letter-spacing: 25px;
    opacity: 0.3;
    font-family: "Courier New", Courier, monospace;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>
