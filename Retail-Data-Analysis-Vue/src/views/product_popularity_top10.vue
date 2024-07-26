<template>
    <div>
        <top-nav></top-nav>

        <el-container>
            <aside-nav></aside-nav>

            <el-main>
                <div
                    class="productChart"
                    ref="productChart"
                    style="width: 100%; height: 400px"
                    v-if="showFlag"
                ></div>
                <loading v-else></loading>
            </el-main>
        </el-container>
    </div>
</template>

<script>
import axios from "axios";
import * as echarts from "echarts";
import Loading from "@/components/Loading.vue";

export default {
    name: "ProductPopularityTop10",
    data() {
        return {
            showFlag: false, // 控制数据加载状态
            products_popularity: [], // 存储从 API 获取的产品数据
        };
    },
    methods: {
        initProductChart() {
            const productChart = echarts.init(this.$refs.productChart);
            const productIds = this.products_popularity.map((item) =>
                item.product_id.toString()
            );
            const counts = this.products_popularity.map((item) => item.count);

            const option = {

                tooltip: {},
                xAxis: {
                    type: "category",
                    data: productIds,
                    name: "ID", // X 轴名称
                    axisLabel: {
                        rotate: 45, // 旋转角度以防止标签重叠
                        interval: 0, // 强制显示所有标签
                    },
                },
                yAxis: {
                    type: "value",
                    name: "购买数量", // Y 轴名称
                },
                series: [
                    {
                        name: "销量",
                        type: "bar",
                        data: counts,
                        label: {
                            show: true,
                            position: "top", // 显示每个柱的值
                        },
                    },
                ],
            };

            productChart.setOption(option);
        },
    },

    mounted() {
        axios
            .get("http://localhost:5000/products_popularity")
            .then((res) => {
                this.products_popularity = res.data.data;
                console.log("产品受欢迎程度数据:", this.products_popularity);
                this.showFlag = true; // 数据加载成功，显示图表
                this.$nextTick(() => {
                    this.initProductChart(); // 数据加载成功后初始化图表
                });
            })
            .catch((error) => {
                console.error("获取数据时发生错误:", error);
                // 可以在这里处理错误，比如显示一个错误提示
            });
    },
};
</script>
<style>

</style>