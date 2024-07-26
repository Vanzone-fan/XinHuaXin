import Category_buy_rate from "@/views/category_buy_rate.vue";
import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

// 异步加载视图组件
const Home = () => import("../views/HomeView.vue");
const ProductsPopularity = () =>
    import("../views/product_popularity_top10.vue");
const UserActivity = () => import("../views/user_activity_top20.vue");
const BestQualityUsers = () => import("../views/best_quality_users.vue");
const WorstQualityUsers = () => import("../views/worst_quality_users.vue");
const CategoryBuyRate = () => import("../views/category_buy_rate.vue");
const UserBuyRate = () => import("../views/user_buy_rate.vue")
const routes = [
    { path: "/", redirect: "/home" }, // 重定向根路径到 home

    { path: "/home", name: "home", component: Home },
    {
        path: "/products_popularity",
        name: "products_popularity",
        component: ProductsPopularity,
    },
    {
        path: "/user_activity",
        name: "user_activity",
        component: UserActivity,
    },
    {
        path: "/best_quality_users",
        name: "best_quality_users",
        component: BestQualityUsers,
    },
    {
        path: "/worst_quality_users",
        name: "worst_quality_users",
        component: WorstQualityUsers,
    },
    {
        path: "/category_buy_rate",
        name: "category_buy_rate",
        component: CategoryBuyRate,
    },
    {
        path:"/user_buy_rate",
        name:"user_buy_rate",
        component:UserBuyRate
    },

];

const router = new VueRouter({
    mode: "history", // 使用 HTML5 History 模式，可以去掉 hash (#) 符号
    routes,
});

export default router;
