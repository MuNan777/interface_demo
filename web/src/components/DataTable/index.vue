<script lang="ts">
import { watch } from 'fs';
import { computed, defineComponent, ref } from 'vue'

export interface ITHeaderItem {
  name: string; // 字段名
  type: 'text' | 'slot' // 类型
  label: string | (() => string) // 标签
  handler?: (value: any) => string // 处理函数
}

export default defineComponent({
  props: {
    headers: {
      type: Array as () => ITHeaderItem[],
      required: true,
    },
    data: {
      type: Array as () => any[],
      required: true,
    }
  },
  setup(props) {
    const innerHeaders = ref<ITHeaderItem[]>(props.headers)
    const innerData = computed(() => props.data)
    return {
      innerData,
      innerHeaders,
    }
  },
})
</script>
<template>
  <div class="max-w-full overflow-x-auto">
    <div class="min-w-[1024px] table-auto">
      <div class="w-full bg-gray-2 text-left dark:bg-meta-4 flex justify-between">
        <template v-for="item of innerHeaders" :key="item.name">
          <div class='flex-1 py-4 px-4 font-medium text-black dark:text-white'>
            {{ typeof item.label === 'function' ? item.label() : item.label }}
          </div>
        </template>
      </div>
      <div>
        <template v-for="item of innerData" :key="item.id">
          <div
            class="flex justify-between border-b box-border border-[#eee] text-black dark:text-white dark:border-strokedark">

            <template v-for="header of innerHeaders" :key="header.name">
              <div class='flex-1 py-4 px-4'>
                <template v-if="header.type === 'text'">
                  {{ header.handler ? header.handler(item[header.name]) : item[header.name] }}
                </template>
                <template v-else>
                  <slot :name="header.name" :item="item"></slot>
                </template>
              </div>
            </template>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>
