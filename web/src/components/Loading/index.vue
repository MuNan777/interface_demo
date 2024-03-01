<script lang="ts">
import { computed, defineComponent } from 'vue'
import { useRequestStore } from '../../store/request'
export default defineComponent({
  setup() {
    const requestStore = useRequestStore()
    const isLoading = computed(() => requestStore.isLoading())
    return {
      isLoading
    }
  }
})
</script>
<template>
  <div v-if="isLoading" class="fixed inset-0 bg-bodydark2 bg-opacity-75 transition-opacity">
    <div class="flex items-center justify-center w-full h-full">
      <div class="flex justify-center items-center space-x-1 text-sm text-gray-700">

        <svg fill='none' class="w-6 h-6 animate-spin" viewBox="0 0 32 32" xmlns='http://www.w3.org/2000/svg'>
          <path clip-rule='evenodd'
            d='M15.165 8.53a.5.5 0 01-.404.58A7 7 0 1023 16a.5.5 0 011 0 8 8 0 11-9.416-7.874.5.5 0 01.58.404z'
            fill='currentColor' fill-rule='evenodd' />
        </svg>


        <div>Loading ...</div>
      </div>
    </div>
  </div>
</template>