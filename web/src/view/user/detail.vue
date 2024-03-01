<script lang="ts">
import { computed, defineComponent, onMounted, ref, watch } from 'vue'
import Dialogs from '../../components/Dialogs/index.vue'
import ValidatorForm, { InputItem } from '../../components/ValidatorForm/index.vue'
import { IUser } from '../../api/user'

export default defineComponent({
  components: {
    Dialogs,
    ValidatorForm
  },
  props: {
    show: {
      type: Boolean,
      required: true
    },
    disabled: {
      type: Boolean,
      default: false
    },
    user: {
      type: Object as () => Partial<IUser>,
      required: true
    }
  },
  emits: ['update:show', 'confirm'],
  setup(props, { emit }) {
    const VFRef = ref<any>(null)
    const innerUser = ref<Partial<IUser>>(props.user)
    onMounted(() => {
      innerUser.value = props.user
    })
    watch(() => props.user, (newVal) => {
      innerUser.value = newVal
    })
    // 表单项
    const inputList = computed<InputItem[]>(() => [
      {
        label: 'Name',
        name: 'name',
        type: 'text',
        message: 'Valid name, 3-20 characters',
        validator: /^\w{3,20}$/,
        placeholder: 'Please input name',
        required: true,
        iconClass: 'i-lucide-user',
        disabled: props.disabled
      },
      {
        label: 'Gender',
        name: 'gender',
        type: 'slot',
        message: 'Valid gender',
        validator: (value: any) => value === 0 || value === 1,
        placeholder: 'Please input gender',
        required: true,
        disabled: props.disabled
      },
    ])
    // 取消
    const handleCancel = () => {
      emit('update:show', false)
    }
    // 确认
    const handleConfirm = async () => {
      const res = await VFRef.value.validator()
      if (res) {
        emit('confirm', res)
      }
    }
    return {
      innerUser,
      inputList,
      VFRef,
      handleCancel,
      handleConfirm
    }
  }
})
</script>
<template>
  <Dialogs :show="show">
    <template #content>
      <div class="border-b pb-3 mb-3">
        <span class="font-bold text-primary text-lg">
          {{ disabled ? 'Detail' : user && user.uid ? 'Edit' : 'Create' }}
        </span>
      </div>
      <ValidatorForm v-if="show" ref="VFRef" :inputList="inputList" v-model:data="innerUser">
        <template #gender="{ value, item, setValue }">
          <select @change="(e) => setValue(item.name, Number((e.target as any)?.value))" :value="value"
            :disabled="item.disabled" :style="{ border: item.disabled ? 'none' : '' }"
            class='w-full border-2 rounded-md bg-gray-2 dark:bg-meta-4 px-3 py-2 focus:outline-none focus:border-primary'>
            <option value="0">male</option>
            <option value="1">female</option>
          </select>
        </template>
      </ValidatorForm>
    </template>
    <template #footer>
      <template v-if="!disabled">
        <div>
          <button type="button" @click="handleConfirm"
            class="bg-primary hover:bg-primary1 inline-flex w-full justify-center rounded-md px-5 sm:ml-5 py-2  text-sm font-semibold text-white shadow-lg m:ml-3 sm:w-auto">
            Confirm
          </button>
        </div>
        <div>
          <button type="button" @click="handleCancel" class="mt-3 inline-flex w-full justify-center rounded-md text-strokedark bg-white px-5 sm:ml-5 py-2
            text-sm font-semibold text-right shadow-lg hover:bg-bodydark hover:text-white sm:mt-0 sm:w-auto">
            Cancel
          </button>
        </div>
      </template>
      <template v-else>
        <div>
          <button type="button" @click="handleCancel"
            class="mt-3 inline-flex w-full justify-center rounded-md text-strokedark bg-white px-5 sm:ml-5 py-2 text-sm font-semibold text-right shadow-lg hover:bg-bodydark hover:text-white sm:mt-0 sm:w-auto">
            Close
          </button>
        </div>
      </template>
    </template>
  </Dialogs>
</template>