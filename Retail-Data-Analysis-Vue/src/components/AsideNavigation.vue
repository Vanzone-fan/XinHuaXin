<template>
    <div class=''>
        <el-container>
            <el-aside width="200px" height="80px" style="background-color: #EEF1F6">
                <el-menu :default-openeds="['1', '2', '3', '4']">
                    <el-submenu index="1">
                        <template slot="title">
                            <i class="el-icon-message"></i>
                            数据可视化界面
                        </template>
                        <router-link to="/products_popularity"> <el-menu-item index="1-1">商品热度top10</el-menu-item></router-link>
                        <router-link to="/user_activity"> <el-menu-item index="1-2">用户活跃度top20</el-menu-item></router-link>
                        <router-link to="/best_quality_users"> <el-menu-item index="1-3">优质用户top20</el-menu-item></router-link>
                        <router-link to="/worst_quality_users"> <el-menu-item index="1-4">劣质用户top20</el-menu-item></router-link>
                        <router-link to="/category_buy_rate"> <el-menu-item index="1-5">商品种类购买率top3</el-menu-item></router-link>
                        <router-link to="/user_buy_rate"> <el-menu-item index="1-6">用户购买率</el-menu-item></router-link>
                    </el-submenu>
                </el-menu>
            </el-aside>
        </el-container>
    </div>
</template>
