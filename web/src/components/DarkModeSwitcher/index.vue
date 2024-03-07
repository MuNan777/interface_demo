<script lang="ts">
import { ref, defineComponent, onMounted } from "vue";
import useColorMode from "../../hooks/useColorMode";
export default defineComponent({
  setup() {
    const { colorMode, setColorMode } = useColorMode();
    const isChecked = ref(colorMode.value === 'light');
    const handleChange = () => {
      setColorMode(isChecked.value ? 'light' : 'dark');
    };
    return {
      isChecked,
      colorMode,
      handleChange
    }
  }
})
</script>

<template>
  <label :class="`relative m-0 block h-7.5 w-14 rounded-full ${colorMode === 'dark' ? 'bg-primary' : 'bg-stroke'}`">
    <input type="checkbox" v-model="isChecked" @change="handleChange"
      class="dur absolute top-0 z-50 m-0 h-full w-full cursor-pointer opacity-0" />
    <span :class="`absolute top-1/2 left-[3px] flex h-6 w-6 -translate-y-1/2 translate-x-0 items-center
        justify-center rounded-full bg-white shadow-switcher duration-75 ease-linear ${colorMode === 'dark'
    && '!right-[3px] !translate-x-full'}`">
      <span class="dark:hidden pt-1">
        <span class="i-lucide-sun-dim"></span>
      </span>
      <span class="hidden dark:inline-block pt-1">
        <span class="i-lucide-moon"></span>
      </span>
    </span>
  </label>
</template>