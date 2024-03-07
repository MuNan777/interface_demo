<script lang="ts">
import { defineComponent } from 'vue'
import AlertList from './components/AlertList/index.vue'
import Loading from './components/Loading/index.vue'
export default defineComponent({
  components: {
    AlertList,
    Loading
  },
  setup() {
  },
})
</script>

<template>
  <div class="dark:bg-boxdark-2 dark:text-bodydark py-10 min-h-screen">
    <!-- 路由出口 -->
    <!-- 路由匹配到的组件将渲染在这里 -->
    <router-view></router-view>
    <AlertList></AlertList>
    <Loading></Loading>
  </div>
</template>
