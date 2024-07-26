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
          user_activity: [], // 存储从 API 获取的产品数据
      };
  },
  methods: {
    initUserChart() {
      const userChart = echarts.init(this.$refs.chart);


      const userIds = this.user_activity.map(item => item.user_id.toString());
      const counts = this.user_activity.map(item => item.count);

      const option = {

        tooltip: {},
        xAxis: {
          type: 'category',
          data: userIds,
          name: '用户ID', // 横坐标名称
          axisLabel: {
            rotate: 45, // 旋转角度以防止标签重叠
            interval: 0 // 强制显示所有标签
          }
        },
        yAxis: {
          type: 'value',
          name: '活跃指标' // 纵坐标名称
        },
        series: [{
          name: '活跃度',
          type: 'bar',
          data: counts,
          label: {
            show: true,
            position: 'top' // 显示每个柱的值
          }
        }]
      };
      userChart.setOption(option);
    }
  },

  mounted() {
      axios
          .get("http://localhost:5000/user_activity")
          .then((res) => {
              this.user_activity=res.data.data;
              console.log(this.user_activity);
              this.showFlag = true; // 数据加载成功，显示图表
              this.$nextTick(() => {
                  this.initUserChart(); // 数据加载成功后初始化图表
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
