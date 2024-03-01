<script lang="ts">
import { computed, defineComponent, onMounted, onUpdated, ref, Ref } from 'vue'

export type ValidatorHandle<T extends Record<string, unknown>> = (value: any, values: T) => boolean | Promise<boolean>;

type ValidatorType = string | number | Array<any> | RegExp | ValidatorHandle<any>

export interface InputItem {
  label?: string, // 标签
  name: string, // 字段名
  type?: HTMLInputElement['type'] | 'slot', // 类型
  message: string, // 提示信息
  validator: ValidatorType, // 验证器
  placeholder?: string, // 占位符
  iconClass?: string, // 图标类名
  required?: boolean, // 是否必填
  disabled?: boolean, // 是否禁用
}

type ValidatorHandleType = () => Promise<false | any>

export interface IValidatorFormRef { validator: ValidatorHandleType }

export default defineComponent({
  props: {
    inputList: {
      type: Array as () => InputItem[],
      required: true
    },
    data: {
      type: Object as () => Record<string, any>,
      required: true
    },
  },
  setup(props, { emit }) {
    const innerData = computed(() => props.data);
    const validMap = ref<Record<string, ValidatorType>>({})
    const showMsgMap = ref<Record<string, boolean>>({})
    const init = () => {
      const sMap: Record<string, boolean> = {};
      const vMap: Record<string, ValidatorType> = {};
      props.inputList.forEach((item) => {
        vMap[item.name] = item.validator
        sMap[item.name] = false
      })
      showMsgMap.value = sMap
      validMap.value = vMap
    }
    onMounted(() => {
      init();
    })

    const validator: ValidatorHandleType = async () => {
      const keys = Object.keys(innerData.value)
      let status = true
      const values: Record<string, any> = {}
      const labelList: string[] = []
      console.log(123)
      for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        const value = innerData.value[key]
        const validator = validMap.value[key]
        values[key] = value
        if (typeof validator === 'function') {
          const result = await validator(value, innerData.value)
          if (!result) {
            status = false
            labelList.push(key)
          }
        } else if (typeof validator === 'string') {
          if (!validator === value) {
            status = false
            labelList.push(key)
          }
        } else if (validator instanceof RegExp) {
          if (!validator.test(value as string)) {
            status = false
            labelList.push(key)
          }
        } else if (Array.isArray(validator)) {
          if (!validator.includes(value)) {
            status = false
            labelList.push(key)
          }
        }
      }
      for (let label of labelList) {
        showMsgMap.value[label] = true
      }
      if (status) {
        return values
      }
      return false
    }
    const setValue = (name: string, value: any | null) => {
      showMsgMap.value[name] = false
      emit('update:data', { ...innerData.value, [name]: value })
    }
    return {
      innerData,
      showMsgMap,
      setValue,
      validator
    }
  }

})
</script>
<template>
  <template v-for="item of inputList" :key="item.name">
    <div class="mb-5">
      <label v-if="!item.disabled" class="hidden mb-2.5 sm:block font-medium text-black dark:text-white">
        {{ item.label }}
      </label>
      <div class="relative flex items-center">
        <span v-if="item.disabled" class="font-medium mr-2.5 min-w-30 text-black dark:text-white">
          {{ item.label }}
        </span>
        <template v-if="item.type !== 'slot'">
          <input :type="item.type" :placeholder="item.disabled ? '' : item.placeholder" :required="item.required"
            :value="innerData[item.name]" @change="(e) => setValue(item.name, (e.target as any)?.value)"
            :disabled="item.disabled" :style="{ border: item.disabled ? 'none' : '' }"
            class='w-full border-2 rounded-md bg-gray-2 dark:bg-meta-4 px-3 py-2 focus:outline-none focus:border-primary' />
          <span v-show="item.iconClass" :class="`${item.iconClass} absolute right-3 top-1/2 translate-y-[-50%]`"></span>
        </template>
        <template v-else>
          <slot :name="item.name" :value="innerData[item.name]" :item="item" :setValue="setValue" />
        </template>
      </div>
      <span :class="`${showMsgMap[item.name] ? 'bleak' : 'hidden'}`">
        <span
          :class="` transition-opacity opacity-0 ${showMsgMap[item.name] ? 'opacity-100' : 'opacity-0'} mt-2 text-sm text-danger`">
          {{ item.message }}
        </span>
      </span>
    </div>
  </template>
</template>
