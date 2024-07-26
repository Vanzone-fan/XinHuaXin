<template>
  <div>
      <top-nav></top-nav>

      <el-container>
          <aside-nav></aside-nav>

          <el-main>
              <div
                  ref="chart"
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
  data() {
      return {
          showFlag: false, // 控制数据加载状态
          data: [], // 存储从 API 获取的产品数据
      };
  },
  methods: {

  },

  mounted() {
      axios
          .get("http://localhost:5000/most_categories_user")
          .then((res) => {
              this.data=res.data.data;
              console.log(this.data)
              this.showFlag = true; // 数据加载成功，显示图表
              this.$nextTick(() => {
                  
              });
          })
          .catch((error) => {
              console.error("获取数据时发生错误:", error);
              // 可以在这里处理错误，比如显示一个错误提示
          });
  },
};
</script>
<style></style>
