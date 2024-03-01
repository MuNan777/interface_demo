<script lang="ts">
import { computed, defineComponent } from 'vue'
import { useRequestStore } from '../../store/request'
export default defineComponent({
  setup() {
    const requestStore = useRequestStore()
    const buildBgColor = (type: string) => {
      switch (type) {
        case 'success':
          return 'bg-success'
        case 'warning':
          return 'bg-warning'
        case 'error':
          return 'bg-danger'
        default:
          return 'bg-success'
      }
    }
    const alerts = computed(() => {
      if (requestStore.alerts) {
        const keys = Object.keys(requestStore.alerts)
        if (keys.length > 0) {
          return keys.map(key => requestStore.alerts[Number(key)])
        }
        return []
      }
    })
    const handleClose = (id?: number) => {
      if (id) {
        requestStore.deleteAlert(id)
      }
    }
    return {
      alerts,
      buildBgColor,
      handleClose
    }
  }
})
</script>
<template>
  <div class="fixed z-99999 bottom-4 left-4">
    <div>
      <template v-for="alert of alerts" :key="alert">
        <div
          :class="`mb-2 font-regular relative block w-full rounded-lg p-4 text-base leading-5 text-white opacity-100 ${alert.type && buildBgColor(alert.type)}`"
          data-dismissible="alert">
          <div class="mr-12">{{ alert.message }}</div>
          <div class="absolute top-2.5 right-3 w-max rounded-lg transition-all hover:bg-white hover:bg-opacity-20"
            data-dismissible-target="alert">
            <button role="button" class="w-max rounded-lg p-1" data-alert-dimissible="true"
              @click="() => handleClose(alert.id)">
              <span class=" i-lucide-x text-white"></span>
            </button>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>