<script lang="ts">
import { ref, watch, defineComponent } from 'vue'

export default defineComponent({
  props: {
    show: {
      type: Boolean,
      required: true
    }
  },
  emits: ['update:show'],
  setup(props, { emit }) {
    const handleMarkClick = () => {
      emit('update:show', false)
    }
    return {
      handleMarkClick
    }
  },
})
</script>
<template>
  <div v-show="show" class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-bodydark2 bg-opacity-75 transition-opacity"></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
        @click="handleMarkClick">
        <div
          class="relative transform rounded-lg bg-gray-2 dark:bg-meta-4 text-left shadow-xl transition-all w-full mx-2 sm:w-full sm:max-w-lg">
          <div class="bg-gray-2 dark:bg-meta-4 px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="w-full">
                <div>
                  <slot name="pre"></slot>
                </div>
                <div>
                  <slot name="content"></slot>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray dark:bg-bodydark2 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
            <slot name="footer"></slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
