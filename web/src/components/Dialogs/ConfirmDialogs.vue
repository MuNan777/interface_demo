<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import Dialogs from './index.vue'

export default defineComponent({
  props: {
    type: {
      type: String as () => 'danger' | 'success' | 'warning',
      default: 'danger',
      required: true
    },
    show: {
      type: Boolean,
      required: true
    },
  },
  components: {
    Dialogs
  },
  emits: ['confirm', 'update:show'],
  setup(props, { emit }) {
    const handleConfirm = () => {
      emit('confirm', true)
      emit('update:show', false)
    }
    const handleCancel = () => {
      emit('update:show', false)
    }

    const getBtnColor = () => {
      switch (props.type) {
        case 'danger':
          return 'bg-danger hover:bg-danger1'
        case 'success':
          return 'bg-success hover:bg-success1'
        case 'warning':
          return 'bg-warning hover:bg-warning1'
        default:
          return 'bg-primary hover:bg-primary1'
      }
    }

    return {
      getBtnColor,
      handleConfirm,
      handleCancel
    }
  },
})
</script>
<template>
  <Dialogs v-model:show="show">
    <template #pre>
      <div class="justify-center flex pb-3 sm:justify-start sm:pb-0">
        <span v-if="type === 'success'" class="i-lucide-badge-check w-15 h-15 text-success"></span>
        <span v-if="type === 'success'" class="i-lucide-badge-alert w-15 h-15 text-danger"></span>
        <span v-if="type === 'success'" class="i-lucide-badge-alert w-15 h-15 text-warning"></span>
      </div>
    </template>
    <template #content>
      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
        <h3 class="text-base font-semibold leading-6" id="modal-title">
          <slot name="title"></slot>
        </h3>
        <div class="mt-2">
          <slot name="body"></slot>
        </div>
      </div>
    </template>
    <template #footer>
      <div>
        <button type="button" @click="handleConfirm"
          :class="['inline-flex w-full justify-center rounded-md px-5 sm:ml-5 py-2  text-sm font-semibold text-white shadow-lg m:ml-3 sm:w-auto', getBtnColor()]">
          Confirm
        </button>
      </div>
      <div>
        <button type="button" @click="handleCancel"
          class=" mt-3 inline-flex w-full justify-center rounded-md text-strokedark bg-white px-5 sm:ml-5 py-2 text-sm font-semibold text-right shadow-lg hover:bg-bodydark hover:text-white sm:mt-0 sm:w-auto">
          Cancel
        </button>
      </div>
    </template>
  </Dialogs>
</template>
